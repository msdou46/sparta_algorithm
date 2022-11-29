class Person:
    def __init__(self, param_name):
        print("i am created! ", self)
        self.name = param_name

    def talk (self):        # 괄호를 입력하려고 하면 자동으로 self 를 완성시켜줘. self 는 항상 존재해야 해.
        print(f"안녕하세요, 제 이름은 {self.name} 입니다.")


person1 = Person("김민수")  # i am created!  <__main__.Person object at 0x7fa84ac86760>
print(person1)      # <__main__.Person object at 0x7f9fe827e760>
print(person1.name)
person1.talk()
person2 = Person("가나다")  # i am created!  <__main__.Person object at 0x7fa84ae9f550>
print(person2)      # <__main__.Person object at 0x7f9fe82636d0>
print(person2.name)
person2.talk()
