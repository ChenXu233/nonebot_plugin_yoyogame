<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="./docs/NoneBotPlugin.svg" width="400" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# 悠悠

nonebot-plugin-yoyogame


<p align="center">
  <a href="https://pypi.python.org/pypi/nonebot-plugin-yoyogame">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-yoyogame.svg" alt="pypi">
  </a>
  
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
  
  <a href="https://qm.qq.com/q/Yty2yc9Bee">
    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-1128359833-orange?style=flat-square" alt="QQ Chat Group">
  </a>
</p>

_✨ 一个为 NoneBot2 开发悠悠游戏插件 ✨_

</div>

## 💿 安装

通过`pip`或`nb`安装；

通过 ** pip **安装

`pip install nonebot-plugin-yoyogame`

通过 ** nb **安装

`nb plugin install nonebot-plugin-yoyogame`

## ⚙ 配置
没有配置，因为现在几乎没啥功能喵

## 🗨命令

`/悠悠` 开始游戏

开始游戏后

你可以输入info和rule获取游戏信息和规则信息

这里放一个规则

| 技能名称 | 相应指令 | 技能花费 | 等级 | 说明                       |
|:-----:|:-----:|:-----:|:-----:|----------------------------------
| 悠悠     | yy       | -1       | 0    | 为自己增加能量             |
| 空炮     | kp       | 0        | 1    | 普通攻击(每隔一回合可使用) |
| 拐勾     | gg       | 1        | 2    | 攻击技能(atk)              |
| 防拐勾   | fgg      | 0        | 2    | 防御技能(dfn)              |
| 七星     | qx       | 2        | 3    | atk                        |
| 防七星   | fqx      | 0        | 3    | dfn                        |
| 反弹     | ft       | 1        | 4    | atk                        |
| 飞刀     | fd       | 3        | 5    | atk                        |
| 防飞刀   | ffd      | 0        | 5    | dfn                        |
| 核弹     | hd       | 7        | 6    | atk                        |

>附:1.攻击技能可被相应的防御技能或高等级的攻击技能抵挡
>2.空炮可被任何防御技能抵挡

## 📝更新日志

### 0.1.0

- 初步完成游戏功能

## 💪 目前支持的平台

| 平台 | 是否经过测试 | 是否能够正常工作 | 测试环境 |
|:-----:|:----:|:----:| :----: |
| Onebot | ✅ | ✅ | NapCat + Window11| 

⚠ **注意：** 目前插件只支持Onebot协议，其他协议暂不支持。

## 📦另外

### 🧐为什么要写这样一个小游戏？

说来话长，很早之前，大约是我初三的时候，同学间流行一个小游戏，就叫悠悠。每天下课就来一把，及其抽象。他们还开发出无数种玩法，什么悠悠：诸神黄昏。然后，我们就想，能不能在电脑上玩，没人和我玩的时候也能玩，于是作为我们班的编程第一把手萧垣老哥就开发了悠悠light版。它曾经~~风靡一时~~，后来因为技术力和时间所限，没有开发往下继续开发，最后就鸽子了。但是喵！现在，是一个高三结束的漫长暑假~~的结束~~，我在翻看过去的代码时，无意间发现了这个游戏，于是我就想，能不能写成Nonebot插件给大家玩，于是就有了这个插件。

### 🤔悠悠是什么意思？为什么要叫悠悠？

悠悠指的就是游戏中获得能量的方法的名字，用于指代这个游戏的名字（本来这个游戏是没有名字的，我们的天才同学用这个取了名）

叫悠悠是因为，我也不到啊，游戏内的各种手段方法的名字都是不知道谁传过来的,说不定哪里有个一样的游戏然后名字和出招名字不一样了。

### 🙃有什么好玩的？

网上玩因为没有手势感觉不到沙雕，但是你要是线下玩，就不会玩口述的，一定是带有抽象手势的，一旦你玩熟了，你就会发现你越悠越快，如果对面也熟练到能跟上节奏的话，俩个人悠着就会非常抽象，非常建议线下试试（虽然现在你可能不知道手势，但是后期游戏会更新手势的喵）

### 😳加入作者的 BUG 反馈群 ~~（🥵女装粉丝群）~~

[群连接](https://qm.qq.com/q/Yty2yc9Bee)

<details>
<summary>群二维码 点我展开</summary>

![7a4bd22dea47d25d9b632d4b2696d4cd](https://github.com/ChenXu233/nonebot_plugin_dialectlist/assets/91937041/61fd7010-e2b2-4f13-b209-9c0faf8a517f)

</details>

### 💕感谢
感谢我的老哥[萧垣](https://github.com/NTFago),他写了绝大部分的游戏代码
以及，感谢ddl写的Nonebot2,没有Nonebot,就没有这个抽象的插件（

### 🎀TODO

- [x] 添加游戏帮助

- [ ] 适配全平台

- [ ] 添加游戏记录

- [ ] 更好看的图片渲染

- [ ] 添加一些全新的可配置项

- [ ] 多人游戏

 待补充.....