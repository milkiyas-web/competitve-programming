# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution(object):
    def equalFrequency(self, word):
        counter = Counter(word)
        for w in word:
            counter[w] -= 1
            
            if counter[w] == 0:
                counter.pop(w)

            if len(set(counter.values())) == 1:
                return True
            counter[w] += 1
        return False