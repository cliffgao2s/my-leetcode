#coding:utf-8
#https://leetcode-cn.com/problems/building-h2o/
#本题使用的网友答案
class H2O:
    def __init__(self):
        self.h, self.o = [], []

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.append(releaseHydrogen)
        self.res()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.append(releaseOxygen)
        self.res()

    def res(self):
        if len(self.h) > 1 and len(self.o) > 0:
            self.h.pop(0)()
            self.h.pop(0)()
            self.o.pop(0)()


