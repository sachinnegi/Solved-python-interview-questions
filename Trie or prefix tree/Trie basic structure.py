class Trie:

    def __init__(self):
        self.trie = {}   # using dictionary of dictionary for trie
        

    def insert(self, word: str) -> None:
        t = self.trie       
        for char in word:
            if char not in t:
                t[char] = {}    # initialising new char as key with empty dictionary value
            t = t[char]         # move inside the char value (sub dictionaries)
        t['#'] = '#'            # ending word with # as key and value
        
    def search(self, word: str) -> bool:
        t = self.trie
        for char in word:
            if char not in t:   # curr character is not present
                return False
            t = t[char]         # narrow down to sub dcitionary
        if '#' in t:            # reached to the end of a word
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for char in prefix:
            if char not in t:   # curr character is not present
                return False
            t = t[char]    
        return True             # prefix present
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
