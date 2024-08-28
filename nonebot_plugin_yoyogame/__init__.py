from nonebot import require

require("nonebot_plugin_session")
require("nonebot_plugin_alconna")
require("nonebot_plugin_cesaa")



from nonebot import on_command
from nonebot.log import logger
from nonebot.typing import T_State
from nonebot.plugin import PluginMetadata, inherit_supported_adapters
from nonebot.params import Depends
from nonebot.matcher import Matcher
from nonebot.adapters import Event,Bot

import nonebot_plugin_saa as saa
from nonebot_plugin_session import Session,extract_session
from nonebot_plugin_alconna import (
    Alconna,
    on_alconna,
)

from .yoyoutils import *
from .config import *

__plugin_meta__ = PluginMetadata(
    name="悠悠",
    description="我他妈当场直接开悠",
    usage=info,
    homepage="https://github.com/ChenXu233/nonebot_plugin_yoyogame",
    type="application",
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_saa", "nonebot_plugin_alconna"
    ),
    config=Config,
    extra={},
)

yoyogame = on_alconna(
    Alconna("悠一把"),
    aliases={"yoyo", "Yo", "悠悠", "悠"},
    use_cmd_start=True,
    priority=4,
    block=True,
)
yoyogame = on_command(
    cmd="悠一把", aliases={"yoyo", "Yo", "悠悠", "悠"}, priority=4, block=True
)


@yoyogame.handle()
async def _responser(event: Event, bot: Bot, state: T_State,session: Session = Depends(extract_session)):

    gameid = str(session.id1) + str(session.id2)
    player = Player()
    computer = Computer()
    computer.set_opl(player)
    game = Game(p1=player, p2=computer)
    state[gameid] = game
    await saa.Text(info).send()


@yoyogame.receive("game")
async def _processer(matcher: Matcher, event: Event, bot: Bot, state: T_State,session: Session = Depends(extract_session)):
    cmd = event.get_plaintext()
    gameid = str(session.id1) + str(session.id2)
    game: Game = state[gameid]
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
            await saa.Text(
                str(game)
                + f"\n本回合你出了：{game.p1.signal}, 电脑出了：{game.p2.signal}\n"
                + tip
            ).finish(reply=True)
        else:
            await saa.Text(
                str(game)
                + f"\n本回合你出了：{game.p1.signal}, 电脑出了：{game.p2.signal}\n"
                + tip
            ).reject(reply=True)

    else:
        await saa.Text("输入不合法，请重新输入！").reject(reply=True)
