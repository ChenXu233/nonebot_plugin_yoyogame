# 《悠悠》基础版
import random

# 游戏信息
VER = "0.2.3内测版"
RES_VER = "YY202108040001"
## 判定等级：自己的等级>对手的等级，进攻成功；自己的等级=对手的等级，防御成功
judgement_level = {"yy": 0, "kp": 1, "gg": 2, "fgg": 2, "qx": 3, "fqx": 3, "ft": 4, "fd": 5, "ffd": 5, "hd": 6,}
## 每个招式对应的能量花费
costs = {"yy": -1, "kp": 0, "gg": 1, "fgg": 0, "qx": 2, "fqx": 0, "ft": 1, "fd": 3, "ffd": 0, "hd": 7,}
## 所有可行的动作
signals = ["yy", "kp", "gg", "fgg", "qx", "fqx", "ft", "fd", "ffd", "hd"]

##------------------------------------------------------------
def create_table():
    from pandas import DataFrame
    from terminaltables import AsciiTable
    actions = DataFrame({
        "技能名称": ["悠悠", "空炮", "拐勾", "防拐勾", "七星", "防七星", "反弹", "飞刀", "防飞刀", "核弹"],
        "相应指令": signals,
        "技能花费": [cost for cost in costs.values()],
        "等级": [level for level in judgement_level.values()],
        "说明": ["为自己增加能量", "普通攻击(每隔一回合可使用)", "攻击技能(atk)", "防御技能(dfn)", "atk", "dfn", "atk", "atk", "dfn", "atk"]
    })
    head = list(actions)
    content = actions.values.tolist()
    act = [head]
    for i in content:
        act.append(i)
    act = AsciiTable(act)
    return act
##-------------------------------------------------------------

info = f"""欢迎游玩由"吖游工作室"开发制作的《悠悠》(Light版)
以下为版本信息：游戏版本：{VER};    游戏资源版本：{RES_VER};    作者：萧垣、煦
以下为当前版本介绍：在此版本中，玩家可通过输入指令的方式与电脑玩家进行对战（暂不支持游戏难度选择）；
若想再次看到此条信息请输入"info"；获取游戏规则请输入"rule",输入攻击指令可以继续游戏
可用的攻击指令有{signals}
"""
rule = ("-------------------游戏规则-------------------\n" + create_table().table +
        "\n附:1.攻击技能可被相应的防御技能或高等级的攻击技能抵挡\n2.空炮可被任何防御技能抵挡")

# 游戏主体
## 玩家类
class Player:
    def __init__(self, extra_hp=0):
        self.signal = None
        self.hp = 1 + extra_hp
        self.energy = 0
        self.atk_able = True

    def set_opl(self, opl):
        self.opl = opl

    def act(self,signal):
        self.signal = signal


    def change_state(self):
        if self.signal == "kp" or (not self.atk_able):
            self.atk_able = not self.atk_able
## 电脑类
class Computer(Player):
    def act(self, bout):
        if bout == 1:
            self.signal = random.choice(['kp', 'fgg'])
        elif self.energy != 7:
            motion = self.analyse()
            if self.atk_able:
                motion.append('kp')
            self.signal = random.choice(motion)
        elif self.energy == 7:
            self.signal = 'hd'

    def analyse(self):
        # 对方可进行的所有行动(不包括空炮、悠悠以及防御)
        act_able = [action for action in costs.keys() if (0 < costs[action] <= self.opl.energy)]
        # 己方可能需要采取的防御措施 + 可以进行的攻击
        motion = ['f'+ action for action in act_able] + [action for action in costs.keys() if (0 < costs[action] <= self.energy)]
        motion.append("yy")    # 加上悠悠
        if "fft" in motion:    # 有问题的行动
            motion.remove("fft")
        if "fgg" not in motion: # 至少得来个防
            motion.append("fgg")
        return motion
## 游戏类
class Game:
    def __init__(self, p1, p2):
        self.bout = 1
        self.p1 = p1
        self.p2 = p2

    def update(self,signal):
        self.p1.act(signal)
        self.p2.act(self.bout)
        p1_level = judgement_level[self.p1.signal]
        p2_level = judgement_level[self.p2.signal]
        self.p1.energy -= costs[self.p1.signal]
        self.p2.energy -= costs[self.p2.signal]

        if self.p1.energy < 0:
            result, tip = 1, "当前能量不足，游戏结束！"
        elif self.p2.energy < 0:
            result, tip = 1, "敌方玩家能量不足，游戏失败！"
        elif len(self.p1.signal) == 2 and len(self.p2.signal) == 2:    # 双方都是攻(或悠悠)
            if p1_level == 1 and not self.p1.atk_able:   # 是空炮，但不能空炮
                result, tip = 1, "当前状态下你无法使用空炮，游戏失败！"
            # 我悠他反弹或他反弹我悠
            elif ((not p1_level) and p2_level == 4) or (p1_level == 4 and(not p2_level)):
                result, tip = 0, "游戏继续~"
            elif p2_level == 1 and not self.p2.atk_able:
                result, tip = 1, "电脑玩家错误地使用了空炮，游戏成功！"
            elif p1_level > p2_level:
                result, tip = 1, "游戏成功!"
            elif p1_level == p2_level:
                result, tip = 0, "游戏继续~"
            else:
                result, tip = 1, "游戏失败！"
        elif len(self.p1.signal) == 2 and len(self.p2.signal) == 3:   # 我攻(或悠)他防
            if not p1_level or p1_level == 1 or p1_level == p2_level or p1_level == 4:   # 我悠或空炮或防住
                result, tip = 0, "游戏继续~"
            elif p2_level != p1_level:  # 它没防住
                result, tip = 1, "游戏成功!"
        elif len(self.p2.signal) == 2 and len(self.p1.signal) == 3:   # 他攻(或悠)我防
            if (not p2_level) or p2_level == 1 or p1_level == p2_level or p2_level == 4:
                result, tip = 0, "游戏继续~"
            elif p2_level != p1_level:  # 我没防住
                result, tip = -1, "游戏失败!"
        elif len(self.p1.signal) == 3 and len(self.p2.signal) == 3:
            result, tip = 0, "游戏继续~"
        
        self.p1.change_state()
        self.p2.change_state()
        self.bout += 1
        return result, tip
    
    def __repr__(self):
        print("---------------------------------------------------------")
        return (f"当前状态(第{self.bout}回合)：\
            \n\t电脑玩家：\tHp = {self.p2.hp}\
            \t能量 = {self.p2.energy}\
            \n\t人类玩家：\tHp = {self.p1.hp}\
            \t能量 = {self.p1.energy}")

def play_game():
    player = Player()
    computer = Computer()
    computer.set_opl(player)
    game = Game(player, computer)
    while True:
        print(game)
        result, tip = game.update()
        print(f"本回合你出了：{player.signal}, 电脑出了：{computer.signal}")
        print(tip)
        if result:
            return 0

# 主程序
if __name__ == "__main__":
    print(info)
    print(rule)
    while True:
        command = input("\n请输入你的指令：")
        if command == "rule":
            print(rule)
        elif command == "info":
            print(info)
        elif command == "start":
            play_game()
        elif command == "quit":
            print("正在退出游戏……")
            quit()
        else:
            print("输入不合法，请重新输入！")
