'''

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

'''

'''

Approach 1: Using Node Class (Traditional Way)

'''

class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
    
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    
    def insert(self, ch, node):
        self.links[ord(ch) - ord('a')] = node 

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True
    
    def isEnd(self):
        return self.flag

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if not node.containsKey(i):
                node.insert(i, Node())
            
            node = node.get(i)

        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if not node.containsKey(i):
                return False

            node = node.get(i)
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if not node.containsKey(i):
                return False
            node = node.get(i)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''

Complexity Analysis

Time Complexity:

Insertion: O(N) where N is the length of the word being inserted. This is because we have to iterate over each letter of the word to find its corresponding node or create a node accordingly.
Search: O(N) where N is the length of the word being searched for. This is because in Trie search we traverse over each letter for the word from the root, 
checking if the current node contains a node at the index of the next letter. This process repeats until we reach the end of the word or encounter a node without the next letter.
Prefix Search: O(N) where N is the length of the prefix being searched for. Similar to searching for words, in prefix search we also iterate over each letter of the word to find its corresponding node.

Space Complexity: O(N) where N is the total number of characters across all unique words inserted into the Trie. 
For each character in a word, a new node may need to be created leading to space proportional to the number of characters.

'''

'''

Approach 2: Using dictonary in place of Node class

'''

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if node.get(i, 0) == 0:
                node[i] = {}
            
            node = node[i]

        node['.'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if node.get(i, 0) == 0:
                return False

            node = node[i]
        
        return node.get('.', False)

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if node.get(i, 0) == 0:
                return False

            node = node[i]
        return True

