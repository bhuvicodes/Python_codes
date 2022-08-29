class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_yourself(self):
        return f"My name is {self.name}"

r1= Robot("Tom", "Blue", 50)
r2 = Robot("Jerry", "Green", 100)


class Person():
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False
    
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r2
p2.robot_owned = r1

print(p1.robot_owned.introduce_yourself())
print(p2.robot_owned.introduce_yourself())