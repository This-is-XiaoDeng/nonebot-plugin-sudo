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
        if str(event.get_message()).startswith(f"{command_start}sudo"):
            if event.get_user_id() in list(config.sudoers):
                # 修改用户信息
                event.user_id = int(
                    str(event.get_message()).strip().split(" ")[1].replace("[CQ:at,qq=", "").replace("]", ""))
                # 修改消息
                cmd_start = command_start if config.sudo_insert_cmdstart else ""
                event.message[0].data["text"] = cmd_start + Message(" ".join(
                    str(event.get_message()).split(" ")[2:]))


