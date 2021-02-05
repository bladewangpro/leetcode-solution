'''@name: 128. Word Ladder II
'''


'''
@performance:
Runtime: 64 ms, faster than 23.98% of Python online submissions for Add Two Numbers.
Memory Usage: 11.9 MB, less than 25.73% of Python online submissions for Add Two Numbers.
'''


#def wordLadder(beginWord, endWord, wordList):
#    """create wordLadder
#    1. create adjacent joint list
#    IMPORTANT: ONE STEP == ONE LEVEL in queueLevel
#    """
#    if endWord not in wordList:
#        return []
#
#    # endWord in wordList
#    adj = dict()
#    wordList.insert(0, beginWord)
#    for i in wordList:
#        adj[i] = []
#
#    for i in range(len(wordList)):
#        wordListC = wordList.copy()
#        wordListC.pop(i)
#        if i != 0:
#            wordListC.pop(0)
#        for j in range(len(wordListC)):
#            if checkConnections(wordList[i], wordListC[j]):
#                adj[wordList[i]] += [wordListC[j]]
#
#    #now BFS
#    queue, queueLevel, result = [[[beginWord]], 1, []]
#
#    while len(queue) != 0:
#        path = queue.pop(0)
#        for i in adj[path[-1]]:
#            path.append(i)
#            if i == endWord:
#                result.append(path.copy())
#            queue.append(path.copy())
#            path.pop(-1)
#        queueLevel -= 1
#        if queueLevel == 0:
#            if len(result) != 0:
#                return result
#            else:
#                queueLevel = len(queue)
#
#
#def checkConnections(word0, word1):
#    return True if sum([1 if i == j else 0 for i, j in zip(word0, word1)]) == len(word0) - 1 else False
#
#
#if __name__ == "__main__":
#    beginWord, endWord, wordList = ["hit", "cog",\
#        ["hot", "dot", "dog", "lot", "log", "cog"]]
#    print(wordLadder(beginWord, endWord, wordList))

"""Word Ladder II
---------------------------------------------
涉及到的知识点：
    1. Breadth-first search
    2. Depth-first search
    3. Dijkstra Algorithm
    4. 双端BFS优化
问题：
    1. What is BFS, bidirectional BFS? and What's the difference between those two method?
    2. What is DFS? Does bidirectional DFS exist? and if it exists, What's the difference between them?
    3. What is Dijkstra Algorithm? What's the advantage of it, especially compared with BFS and DFS?
    4. What kind of situation do BFS, DFS and Dijkstra Algorithm fit?
    5. What kind of improvement can we do on bidirectional BFS and bidirectional DFS?
    6. Which algorithm is better in this topic, BFS, DFS or Dijkstra? and Why?
"""


def findLadders(beginWord, endWord, wordList):

    """create wordLadder
    1. create adjacent joint list
    IMPORTANT: ONE STEP == ONE LEVEL in queueLevel
    """
    if endWord not in wordList:
        return []
    # endWord in wordList
    adj = dict()
    wordList.insert(0, beginWord)
    for i in wordList:
        adj[i] = []

    for i in range(len(wordList)):
        wordListC = wordList.copy()
        wordListC.pop(i)
        if i != 0:
            wordListC.pop(0)
        for j in range(len(wordListC)):
            if wordListC[j] not in adj[wordList[i]]:
                if checkConnections(wordList[i], wordListC[j]):
                    adj[wordList[i]] += [wordListC[j]]
                    adj[wordListC[j]] += [wordList[i]]

    #now BFS
    queue, queueLevel, result = [[[beginWord]], 1, []]

    while len(queue) != 0:
        path = queue.pop(0)
        for i in adj[path[-1]]:
            path.append(i)
            if i == endWord:
                result.append(path.copy())
            queue.append(path.copy())
            path.pop(-1)
        queueLevel -= 1
        if queueLevel == 0:
            if len(result) != 0:
                resultC = []
                for i in range(len(result)):
                    if result[i] not in resultC:
                        resultC.append(result[i])
                return resultC
            else:
                queueLevel = len(queue)


def checkConnections(word0, word1):
    return True if sum([1 if i == j else 0 for i, j in zip(word0, word1)]) == len(word0) - 1 else False



if __name__ == "__main__":
    '''BFS or Dijkstra
    works on finding shortest path
    directed and undirected unweighted graph;
    directed weighted graph
    '''
    beginWord, endWord = ("cet", "ism")
    wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    result = findLadders(beginWord, endWord, wordList)
    print(result)
