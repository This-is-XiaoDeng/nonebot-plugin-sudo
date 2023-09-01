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
    supported_adapters={"~onebot.v11"}
)


@event_preprocessor
async def sudo_command(event: MessageEvent):
    for command_start in get_driver().config.command_start:
        if event.raw_message.startswith(f"{command_start}sudo"):
            if event.get_user_id() in list(config.sudoers):
                event.user_id = get_user_id(command_start, event)
                cmd_start = command_start if config.sudo_insert_cmdstart else ""
                change_message(
                    command_start,
                    event,
                    event.user_id,
                    cmd_start
                )
                break

def get_user_id(command_start: str, event: MessageEvent) -> int:
    message_start = event.message[0].data["text"]
    if (user_id := message_start.replace(f"{command_start}sudo", "").strip()) != "":
        return int(user_id)
    else:
        return event.message[1].data["qq"]

def change_message(command_start: str, event: MessageEvent, user_id: int, cmd_start) -> None:
    message_start = event.message[0].data["text"]
    if (user_id := message_start.replace(f"{command_start}sudo", "").strip()) != "":
        event.message[0].data["text"] = cmd_start + event.message[0].data["text"].replace(f"{command_start}sudo", "", 1).replace(f"{user_id}", "", 1).strip()
    else:
        event.message.pop(0)
        event.message.pop(0)
        try:
            event.message[0].data["text"] = cmd_start + event.message[0].data["text"].strip()
        except:
            pass
