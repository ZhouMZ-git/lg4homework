


# 创建一个虚竹类继承童姥类
from python_homework.tonglao import TongLao


class XuZhu(TongLao):
    # 定义虚竹的念经方法
    def read(self):
        print("罪过罪过")


a = XuZhu(10, 10)
a.fight_zms(10, 10)
a.read()
