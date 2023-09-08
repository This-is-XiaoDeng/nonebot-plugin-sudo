from nonebot import get_driver
from nonebot.message import event_preprocessor
from nonebot.adapters.onebot.v11 import MessageEvent, Message
from nonebot.log import logger
from .config import Config
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

sudo = False
use_sudo = 0


@event_preprocessor
async def sudo_command(event: MessageEvent):
    global sudo
    global use_sudo
    sudo = False
    for command_start in get_driver().config.command_start:
        if event.raw_message.startswith(f"{command_start}sudo"):
            if event.get_user_id() in list(config.sudoers):
                event.user_id = get_user_id(event)
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


@Bot.on_calling_api
async def handle_api_call(bot: Bot, api: str, data: dict[str, any]):
    if (
        api == "send_msg"
        and sudo
        and data["message_type"] == "private"
        or api == "send_private_forward_msg"
    ):
        data["user_id"] = use_sudo
