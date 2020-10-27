# 创建一个虚竹类继承童姥类
from python_homework.tonglao import TongLao


class XuZhu(TongLao):
    # 定义虚竹的念经方法
    def read(self):
        print("罪过罪过")


# 创建一个虚竹对象
a = XuZhu(10, 10)
# 调用父类童姥的方法
a.fight_zms(10, 10)
# 调用自己的方法
a.read()
