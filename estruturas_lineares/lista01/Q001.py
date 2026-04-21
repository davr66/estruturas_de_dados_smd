from enum import StrEnum, auto
import unittest


# implementação referente ao exercício 1 da lista de exercícios
class Status(StrEnum):
    TODO = auto()
    DOING = auto()
    DONE = auto()


class Task:

    def __init__(self, name, description=''):
        self.__name = name
        self.__status = Status.TODO
        self.__description = description

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: Status):
        self.__status = status

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    def __eq__(self, other):
        result = False
        if isinstance(other, Task) and other.name == self.__name:
            result = True
        return result


class TodoList:
    def __init__(self):
        self.__data = list()

    def add(self, task: Task):
        self.__data.append(task)

    def remove_by_name(self, task: Task):
        for t in self.__data:
            if t.name == task.name:
                self.__data.remove(t)
                return
        raise ValueError("Task not found in todo list")

    def list_undone(self):
        return [t for t in self.__data if t.status != Status.DONE]
        # a linha acima é equivalente ao trecho abaixo
        # result = list()
        # for t in self.__data:
        #     if t.status != Status.DONE:
        #         result.append(t)
        # return result

    def end_task(self, task: Task):
        if task in self.__data:
            task.status = Status.DONE
            self.remove_by_name(task)
        else:
            raise ValueError('Task does not exist')

