
print('--------------------------- 3-7 해쉬-1 딕셔너리 구현해보기 ---------------------------')

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        idx_key = hash(key) % len(self.items)   # 나머지를 이용하는 거잖아. 따라서 무조건 배열의 길이 미만으로 값이 나오지. 그걸 인덱스로 이용.
        self.items[idx_key] = value
        return

    def get(self, key):
        idx = hash(key) % len(self.items)
        return self.items[idx]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!