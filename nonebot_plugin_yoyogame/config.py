from nonebot import get_driver,get_plugin_config
from pydantic import BaseModel, Extra

class ScopedConfig(BaseModel):
    ...

class Config(BaseModel):
    yoyogame: ScopedConfig = ScopedConfig()


global_config = get_driver().config
plugin_config = get_plugin_config(Config).yoyogame