from pydantic import Extra, BaseModel

class Config(BaseModel, extra = Extra.ignore):
    sudoers: list[str] = []
    sudo_insert_cmdstart: int = 0
