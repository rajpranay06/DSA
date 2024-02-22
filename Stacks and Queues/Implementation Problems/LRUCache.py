'''

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Intuition:

While inserting the {key,val} pair into the DDL make sure that we are inserting it from the back tail to head.
The cache will tell us when the {key, value} pair is used/inserted.

Time Complexity:O(N)
Space Complexity:O(1)

'''

class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
    
    # Adding node after head
    def addNode(self, node):
        temp = self.head.next
        node.next = temp
        self.head.next = node 
        node.prev = self.head
        temp.prev = node
    
    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def __init__(self, capacity: int):
        self.map = {}
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        # Get the node from map, and update th map and DLL
        curr = self.map[key]
        val = curr.val
        del self.map[key]
        self.deleteNode(curr)
        self.addNode(curr)
        self.map[key] = self.head.next
        return val

    def put(self, key: int, value: int) -> None:

        # If key is already present delete the key node and update it with new value
        if key in self.map:
            self.deleteNode(self.map[key])
            del self.map[key]
        
        # If the size is full, delete the prev node of tail 
        if len(self.map) == self.size:
            delNode = self.tail.prev
            del self.map[delNode.key]
            self.deleteNode(delNode)

        self.addNode(self.Node(key, value))
        self.map[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''

Using in-built function:
-> We can use OrderDict(), where we can set the LRU key to end using dict.move_to_end(key)

'''

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache.keys()) > self.size:
            self.cache.popitem(0)
        
