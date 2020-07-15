import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]: 
    """Purpose: Given a non-empty list of words, return the k most frequent elements.
    The answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
    """
        words.sort() # sort words into alphabetical order
        mydict = {}
        for word in words:
            if word in mydict.keys():
                mydict[word] += 1
            else:
                mydict[word] = 1
        
        # turn dict into a heap, with values of dict as priorities.
        res = []
        myheap = [(-value, key) for key,value in mydict.items()]
        heapq.heapify(myheap)
        for i in range(k):
            res.append(heapq.heappop(myheap)[1])
        return res
