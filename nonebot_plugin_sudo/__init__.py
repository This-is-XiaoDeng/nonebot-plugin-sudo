from nonebot import get_driver
from nonebot.message import event_preprocessor
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.log import logger

@event_preprocessor
async def sudo_command(event: MessageEvent):
    for command_start in get_driver().config.command_start:
        if event.get_plaintext().startswith(f"{command_start}sudo"):
            if event.get_user_id() in list(get_driver().config.sudoers):
                # 修改用户信息
                event.user_id = event.user_id = int(
                    event.get_plaintext().strip().split(" ")[1])
                # 修改消息
                cmd_start = command_start if get_driver().config.sudo_insert_cmdstart else ""
                event.message[0].data["text"] = cmd_start + " ".join(
                    event.message[0].data["text"].split(" ")[2:])

if not hasattr(get_driver().config, "sudoers"):
    get_driver().config.sudoers = []
    logger.warning("SUDOERS 未设置，已初始化为 空列表")

if not hasattr(get_driver().config, "sudo_insert_cmdstart"):
    get_driver().config.sudoers = 0
    logger.warning("SUDO_INSERT_CMDSTART 未设置，已初始化为 假")

