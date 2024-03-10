class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        current = self.root
        print(current.children)
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]
        current.is_end_of_word = True


    def search(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                print("Not in ")
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

t = Trie()
t.insert("bat")
# t.insert("apple")
# t.insert("orange")
# t.insert("pineapple")
# print(t.search("apple"))
# print(t.starts_with("or"))
