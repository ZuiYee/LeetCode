
'''
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        letter_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--."
                       "","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        eset = set()
        for word in words:
            eletter = ""
            for letter in word:
                eletter += letter_list[ord(letter)-97]
            eset.add(eletter)
        return len(eset)
'''

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)

if __name__ == '__main__':
    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(s.uniqueMorseRepresentations(words))