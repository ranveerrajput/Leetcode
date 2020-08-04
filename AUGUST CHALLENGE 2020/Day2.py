class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word==word.upper()):
            return(1)
        elif(word==word.lower()):
            return(1)
        elif(word[0]==word[0].upper()  and word[1:]==word[1:].lower()):
            return(1)
        else:
            return(0)
            
        
