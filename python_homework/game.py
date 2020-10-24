
"""
回合制 游戏
"""



import random

# 定义一个fight函数
def fight(enemy_hp,enemy_power):
    # 定义敌人的初始血量
    #enemy_hp = 1000
    # 定义敌人的攻击力
    #enemy_power = 300

    # enemy_final_hp

    # 定义我的的初始血量
    my_hp = 1000
    # 定义我的攻击力
    my_power = 300

    # my_final_hp

    # 在没分出结果的时候一直打下去
    while True:
        # 我的最终血量等于我的初始血量减去敌人的攻击力
        my_final_hp = my_hp - enemy_power
        my_hp = my_final_hp
    # 判断是否我还活着，血量是不是等于小于零
        if  my_final_hp <= 0:
        # 因为我比较自负，一样的剩余血量以及少于敌人的剩余血量我都算我输
         print("我输了")
         break

    # 敌人的最终血量等于敌人的初始血量减去我的攻击力
        enemy_final_hp = enemy_hp - my_power
        enemy_hp = enemy_final_hp


    # 判断敌人是否还活着
        if enemy_final_hp <= 0:
            print("我赢了")
            break

##下面这个模块直接执行本文件时才执行被调用将不被执行
if __name__=="__main__":
    #利用推导式生成一定范围的血量
    hp=[x for x in range(900,1020)]
    #让敌人的血量从中随机选择一个值
    enemy_hp=random.choice(hp)

    #在用random方法给敌人的攻击力随机生成一些数
    enemy_power=random.randint(99,400)

    fight(enemy_hp,enemy_power)
