from nonebot import get_driver
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    pass

global_config = get_driver().config
plugin_config = Config(**global_config.dict())