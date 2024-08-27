from typing import Union


from nonebot import on_command
from nonebot.log import logger
from nonebot.typing import T_State
from nonebot.plugin import PluginMetadata
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, MessageEvent

from .yoyoutils import *
from .config import *

__plugin_meta__ = PluginMetadata(
    name="悠悠",
    description="我他妈当场直接开悠",
    usage=info,
    homepage="https://github.com/ChenXu233/nonebot_plugin_yoyogame",
    type="application",
    supported_adapters={"~onebot.v11"},
    # TODO: 增加插件依赖
    config=Config,
    extra={},
)

yoyogame = on_command(cmd ='悠一把',aliases={"yoyo","Yo","悠悠", "悠" },priority=4,block=True)

@yoyogame.handle()
async def _responser(matcher:Matcher,event:MessageEvent,bot:Bot,state:T_State):
    
    player = Player()
    computer = Computer()
    computer.set_opl(player)
    game = Game(p1=player,p2=computer)
    state['game'] = game
    await matcher.send(info)
    

@yoyogame.receive(id='1')
async def _processer(matcher:Matcher,event:MessageEvent,bot:Bot,state:T_State):
    cmd = event.get_plaintext()
    game:Game = state['game']
    if cmd == "rule":
        await matcher.reject(rule)
    elif cmd == "info":
        await matcher.reject(info)
    elif cmd == "quit":
        print("正在退出游戏……")
        await matcher.finish()
    elif cmd in signals:
        result, tip = game.update(signal=cmd)
        if result == 1:
            await matcher.finish(str(game)+f"\n本回合你出了：{game.p1.signal}, 电脑出了：{game.p2.signal}\n"+tip)
        else:
            await matcher.reject(str(game)+f"\n本回合你出了：{game.p1.signal}, 电脑出了：{game.p2.signal}\n"+tip)
            
    else:
        await matcher.reject("输入不合法，请重新输入！")
    
    
        