from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.message import event_preprocessor
from nonebot.message import event_postprocessor
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot import get_driver
from .config import Config
import asyncio
from nonebot.plugin import PluginMetadata

config = Config.parse_obj(get_driver().config)
__plugin_meta__ = PluginMetadata(
    name="SUDO",
    description="以指定用户身份执行命令",
    usage="使用 /sudo 指令以指定用户身份执行命令",
    type="application",
    homepage="https://github.com/This-is-XiaoDeng/nonebot-plugin-sudo",
    config=Config,
    supported_adapters={"~onebot.v11"},
)
_sudo_original_user: dict[int, MessageEvent] = {}


@event_postprocessor
async def sudo_postprocessor(event: MessageEvent):
    if not hasattr(event, "_sudo_original_user"):
        return
    if event.user_id in _sudo_original_user.keys():
        _sudo_original_user.pop(event.user_id)


@event_preprocessor
async def sudo_command(event: MessageEvent):
    for command_start in get_driver().config.command_start:
        if event.raw_message.startswith(f"{command_start}sudo") and event.get_user_id() in list(config.sudoers):
            event._sudo_origin_user = event.user_id
            event.user_id = get_user_id(event)
            # 不建议在私聊使用 /sudo 指令，可能出现一些不可预料的 Bug
            if event.message_type == "private":
                while event.user_id in _sudo_original_user.keys():
                    await asyncio.sleep(0.1)
                _sudo_original_user[event.user_id] = event
            cmd_start = command_start if config.sudo_insert_cmdstart else ""
            change_message(event, cmd_start)
            break


def get_user_id(event: MessageEvent) -> int:
    message_start = event.message[0].data["text"]
    try:
        return message_start.strip().split(" ")[1]
    except IndexError:
        return event.message[1].data["qq"]


def change_message(event: MessageEvent, cmd_start) -> None:
    if tmp_message := " ".join(event.message[0].data["text"].split(" ")[2:]):
        event.message[0].data["text"] = cmd_start + tmp_message
    else:
        event.message.pop(0)
        event.message.pop(0)
        event.message[0].data["text"] = (
            cmd_start + event.message[0].data["text"].strip()
        )


async def handle_api_call(_bot: Bot, api: str, data: dict[str, any]):
    if (
        (api == "send_msg" and data["message_type"] == "private")
        or api in ["send_private_forward_msg", "send_private_msg"]
        and data["user_id"] in _sudo_original_user.keys()
    ):
        data["user_id"] = _sudo_original_user[data["user_id"]]._sudo_original_user


@get_driver().on_bot_connect
async def on_bot_connect(bot: Bot):
    bot.on_calling_api(handle_api_call)
