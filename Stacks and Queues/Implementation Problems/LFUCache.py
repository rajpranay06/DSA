'''

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. 
When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. 
For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
The functions get and put must each run in O(1) average time complexity.


Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3

'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cnt = 1
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addFront(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    def removeNode(self, delnode):
        delprev = delnode.prev
        delnext = delnode.next
        delprev.next = delnext
        delnext.prev = delprev
        self.size -= 1

class LFUCache:

    def __init__(self, capacity):
        self.keyNode = {}
        self.freqListMap = {}
        self.maxSizeCache = capacity
        self.minFreq = 0
        self.curSize = 0

    def updateFreqListMap(self, node):
        # Delete the current node of the key
        del self.keyNode[node.key]
        self.freqListMap[node.cnt].removeNode(node)

        # If there are no keys in current minFreq increase minFreq
        if node.cnt == self.minFreq and self.freqListMap[node.cnt].size == 0:
            self.minFreq += 1

        # Get the list of the next frequent from the freq map
        nextHigherFreqList = List()
        if node.cnt + 1 in self.freqListMap:
            nextHigherFreqList = self.freqListMap[node.cnt + 1]

        node.cnt += 1
        nextHigherFreqList.addFront(node)
        self.freqListMap[node.cnt] = nextHigherFreqList
        self.keyNode[node.key] = node

    def get(self, key: int) -> int:
        # If key in keyNode map update the map
        if key in self.keyNode:
            node = self.keyNode[key]
            val = node.value
            self.updateFreqListMap(node)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.maxSizeCache == 0:
            return

        # If key in map, update the list
        if key in self.keyNode:
            node = self.keyNode[key]
            node.value = value
            self.updateFreqListMap(node)
        else:
            if self.curSize == self.maxSizeCache:
                # Get the least frequent key and delete it
                arr = self.freqListMap[self.minFreq]
                del self.keyNode[arr.tail.prev.key]
                arr.removeNode(arr.tail.prev)
                self.curSize -= 1

            self.curSize += 1
            self.minFreq = 1
            listFreq = List()
            # Add to the minFreq map if minFre exists
            if self.minFreq in self.freqListMap:
                listFreq = self.freqListMap[self.minFreq]

            # Add minFreq and list to the map
            node = Node(key, value)
            listFreq.addFront(node)
            self.keyNode[key] = node
            self.freqListMap[self.minFreq] = listFreq

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
