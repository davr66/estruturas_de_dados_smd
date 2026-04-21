from collections import deque


class Customer:
    def __init__(self, name: str, pass_num: int):
        self.__name = name
        self.__pass_num = pass_num

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def pass_num(self):
        return self.__pass_num

    @pass_num.setter
    def pass_num(self,pass_num):
        self.__pass_num = pass_num

    def __str__(self):
        return f"Nome: {self.name} | Senha: {str(self.pass_num)}"

    def __repr__(self):
        return self.__str__()

class Queue:
    def __init__(self):
        self.__queue = deque()

    def waiting_number(self):
        return len(self.__queue)

    def add_customer(self, customer: Customer):
        customer.pass_num = len(self.__queue) + 1
        self.__queue.append(customer)

    def find_pos_by_name(self, name:str):
        for i, c in enumerate(self.__queue):
            if c.name == name:
                return i
        return -1

    def next_customer(self):
        return self.__queue.popleft()

    def queue_as_list(self):
        c_list = "------ Fila de Atendimento ------\n\n"
        for i, c in enumerate(self.__queue):
            c_list += f"[{i}] {c.name} - Senha {str(c.pass_num)}\n"
        c_list += "---------------------------------"
        return c_list


c1 = Customer("Alice", 1)
c2 = Customer("Bruno", 1)
c3 = Customer("Carla", 1)
c4 = Customer("Diego", 1)
c5 = Customer("Elena", 1)
c6 = Customer("Felipe", 1)
c7 = Customer("Gabi", 1)
c8 = Customer("Hugo", 1)

f1 = Queue()
for c in [c1, c2, c3, c4, c5, c6, c7, c8]:
    f1.add_customer(c)

print(f1.queue_as_list())
print(f1.next_customer())
print(f1.queue_as_list())
print(f1.find_pos_by_name('Hugo'))














