'''@name: 128. Word Ladder II
'''


'''
@performance:
Runtime: 64 ms, faster than 23.98% of Python online submissions for Add Two Numbers.
Memory Usage: 11.9 MB, less than 25.73% of Python online submissions for Add Two Numbers.
'''


def wordLadder(beginWord, endWord, wordList):
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
            if checkConnections(wordList[i], wordListC[j]):
                adj[wordList[i]] += [wordListC[j]]

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
                return result
            else:
                queueLevel = len(queue)


def checkConnections(word0, word1):
    return True if sum([1 if i == j else 0 for i, j in zip(word0, word1)]) == len(word0) - 1 else False


if __name__ == "__main__":
    beginWord, endWord, wordList = ["hit", "cog",\
        ["hot", "dot", "dog", "lot", "log", "cog"]]
    print(wordLadder(beginWord, endWord, wordList))
