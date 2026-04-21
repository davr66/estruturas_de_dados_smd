from queue import PriorityQueue

class Patient:
    def __init__(self,name:str,age:int,urgency:int):
        self.__name = name
        self.__age = age
        self.__urgency = urgency

    @property
    def urgency(self):
        return self.__urgency

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.__name} | {self.__age} | Nível de urgência: {self.__urgency}"

class Triage:
    def __init__(self):
        self.__queue = PriorityQueue()

    def add_patient(self,patient:Patient):
        self.__queue.put((patient.urgency, self.__queue.qsize()+1, patient))

    def next_patient(self):
        return self.__queue.get()[2]


p1 = Patient("Alice", 34, 2)
p2 = Patient("Bruno", 68, 1)
p3 = Patient("Carla", 22, 3)
p4 = Patient("Diego", 45, 1)
p5 = Patient("Elena", 55, 4)
p6 = Patient("Felipe", 29, 2)
p7 = Patient("Gabi", 78, 1)
p8 = Patient("Hugo", 41, 3)
p9 = Patient("Íris", 19, 4)
p10 = Patient("João", 60, 2)

t = Triage()
for p in [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]:
    t.add_patient(p)

for _ in range(10):
    print(t.next_patient())
