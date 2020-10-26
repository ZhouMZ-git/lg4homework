# 创建一个童姥类
class TongLao:

    def __init__(self, hp, power):
        # 定义童姥的血量属性
        self.hp = hp
        #  定义童姥的武力值
        self.power = power

    # 童姥的see_people方法
    def see_people(self, name):
        self.name = name
        if self.name == "WYZ":
            print("师弟！！！！ 我好爱你")
        elif self.name == "李秋水":
            print("师弟是我的，你这是找死 晓得不")
        elif self.name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("你得输入跟我有爱恨纠葛的人才行！")

        # 童姥的fight_zms方法

    def fight_zms(self, hp, power):
        # 敌人的血量
        enemy_hp = hp
        # 敌人的武力值
        enemy_power = power

        self.hp = self.hp * 0.5
        self.power = self.power

        # 童姥的最终血量等于童姥初始血量减去敌人的攻击力

        self.hp = self.hp - enemy_power
        # 敌人的最终血量等于敌人的初始血量减去童姥的攻击力
        enemy_hp = enemy_hp - self.power
        if enemy_hp < self.hp:
            print("童姥厉害！！！！")
        else:
            print("童姥 你到底还是老了")
