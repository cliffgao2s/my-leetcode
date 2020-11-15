#https://leetcode-cn.com/contest/weekly-contest-215/problems/design-an-ordered-stream/
#注意边界值不越界即可 PRT长度不能超过数组长度

class OrderedStream(object):
    dict = {}
    lenDict = 0
    ptrDict = 0

    def __init__(self, n):
        """
        :type n: int
        """
        self.lenDict = n
        self.ptrDict = 0

        for index in range(n):
            self.dict[index] = ""

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        retList = []

        if len(value) != 5 or id > self.lenDict:
            return retList

        self.dict[id-1] = value

        if self.ptrDict < len(self.dict):
            for index in range(self.ptrDict, len(self.dict)):
                if self.dict[index] != "":
                    retList.append(self.dict[index])
                    self.ptrDict += 1
                else:
                    break

        return retList


#orderedStream = OrderedStream(5)

#print(orderedStream.insert(3, "ccccc"))
#print(orderedStream.insert(1, "aaaaa"))
#print(orderedStream.insert(2, "bbbbb"))
#print(orderedStream.insert(5, "eeeee"))
#print(orderedStream.insert(4, "ddddd"))


orderedStream = OrderedStream(6)
print(orderedStream.insert(3, "mtdul"))
print(orderedStream.insert(2, "ntpaz"))
print(orderedStream.insert(1, "hjawf"))
print(orderedStream.insert(6, "tlbxi"))
print(orderedStream.insert(5, "eeyfo"))
print(orderedStream.insert(4, "yuxep"))