from collections import OrderedDict
class LRUCache:
    dic = OrderedDict()
    capacity = -1

    def __init__(self, capacity: int):
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key, last=True)
            return self.dic[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key, last=True)
            self.dic[key] = value
        elif len(self.dic) < self.capacity:
            self.dic[key] = value
        else:
            self.dic.popitem(last=False)
            self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)