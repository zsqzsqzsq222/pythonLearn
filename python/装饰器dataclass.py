from dataclasses import dataclass,field

@dataclass
class Person:
    name: str
    age: int = 30 # 1.默认值
    money: int = field(default=100, init=False)  # 2.不允许通过构造函数传入 age
    friends: list = field(default_factory=list) # 4.默认值为一个空列表

    # 3. 初始化后执行
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

p1 = Person("Alice", 30)
p2 = Person("Alice")
print(p1) # Person(name='Alice', age=30, money=100, friends=[])
print(p1 == p2) # True
p1.friends.append("Bob")
print(p1 == p2) # False



