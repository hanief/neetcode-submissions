class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)

        for wordIndex in range(n):
            rowWord = words[wordIndex]
            
            columnWord = ""
            
            for i in range(len(rowWord)):
                if len(words) <= i:
                    return False
                    
                word = words[i]

                if len(word) <= wordIndex:
                    return False

                char = word[wordIndex]
                columnWord += char

            if rowWord != columnWord:
                return False
        
        return True
            