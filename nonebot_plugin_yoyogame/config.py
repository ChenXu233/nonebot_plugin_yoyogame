from nonebot import get_driver,get_plugin_config
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    pass

plugin_config = get_plugin_config(Config)