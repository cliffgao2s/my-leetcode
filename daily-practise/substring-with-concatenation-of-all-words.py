#https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/

#方法1  求出words的全排序，然后直接拿全排序去比对，但复杂度随着WORDS增大，指数级增大

#方法2  该题有个特性，WORDS子元素长度相同，方便比较;直接 不停找和WORDS长度相同的子串，然后均匀切割子串，去比较每一个WORDS是否在内

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        lenElements = len(words[0])
        totalLen = lenElements * len(words)

        result = []
        
        for index in range(len(s) - totalLen + 1):
            splitList = []

            for index1 in range(len(words)):
                splitList.append(s[index + index1*lenElements : index + index1*lenElements + lenElements])
            
            for item in words:
                if item in splitList:
                    splitList.remove(item)
                else:
                    break
            
            if len(splitList) <= 0:
                result.append(index)


        return result
    


solution = Solution()

#[0,9]
#s = "barfoothefoobarman"
#words = ["foo","bar"]

#[8]
#s = "wordgoodgoodgoodbestword"
#words = ["word","good","best","good"]

#[0,1]
#s = "aaa"
#words = ["a", "a"]

#[935]
s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]

print(solution.findSubstring(s, words))






'''
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []   

        #将WORDS所有排列都组合起来
        wordList = []

        totalLen = 0
        for item in words:
            totalLen += len(item)

        wordList = self.fullStack(words)

        print(wordList)


        for item in wordList:

            for index in range(len(s)):
                if s.find(item, index) >= 0:
                    result.append(s.find(item, index))

        #防止那种对称字符，对结果查重
        finalResult = []

        for item in result:
            if item not in finalResult:
                finalResult.append(item)

        return finalResult

    def fullStack(self, listA):
        if len(listA) == 1:
            return [listA[0]]

        resultList = []

        for index in range(len(listA)):
            subList = listA[:index] + listA[index+1:]
            subResult = self.fullStack(subList)

            for index1 in range(len(subResult)):
                resultList.append(listA[index] + subResult[index1])


        return resultList
        '''