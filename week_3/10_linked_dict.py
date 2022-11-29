
print('--------------------------- 3-7 해쉬-1 링크드 리스트의 형태로 값을 저장. ---------------------------')

class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            print('k, v : ', k, v)
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())        # [ [ (key, value), (key, value) ], [], [], [], [], [], [], [] ]

    def put(self, key, value):
        hash_idx = hash(key) % len(self.items)
        self.items[hash_idx].add(key, value)

    def get(self, key):
        hash_idx = hash(key) % len(self.items)
        return self.items[hash_idx].get(key)

linkedDict = LinkedDict()
linkedDict.put("test", 33)
linkedDict.put("test", 34)
linkedDict.put("test", 35)
print(linkedDict.get("test"))
print(linkedDict.items[7])