from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    sudoers: list[str] = []
    sudo_insert_cmdstart: int = 0
    sudo_replace_sender_data: int = 1
