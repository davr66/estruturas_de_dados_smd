from collections import deque
from datetime import datetime
from time import sleep


class Document:
    def __init__(self,title:str, page_num:int, user_name:str):
        self.__title = title
        self.__page_num = page_num
        self.__user_name = user_name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.__title} | {str(self.__page_num)} página(s) | user: {self.__user_name}"

    @property
    def title(self):
        return self.__title
    @property
    def page_num(self):
        return self.__page_num
    @property
    def user_name(self):
        return self.__user_name

class Buffer:
    def __init__(self):
        self.__queue = deque()

    def is_empty(self):
        return not self.__queue

    def add(self,doc:Document):
        self.__queue.append(doc)

    def next(self):
        return self.__queue.popleft()


class Printer:
    def __init__(self,buffer:Buffer):
        self.__buffer = buffer
        self.__actions_log = list()

    def add_doc(self,doc:Document):
        self.__actions_log.append(f"Enviando documento {doc.title} - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
        self.__buffer.add(doc)
        self.__actions_log.append(f"{doc.title} enviado! - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")

    def show_log(self):
        return "\n".join(self.__actions_log)
        # log_str = ""
        # for i,log in enumerate(self.__actions_log):
        #     log_str += f"{log}\n"
        # return log_str

    def print(self):
        while not self.__buffer.is_empty():
            current_doc = self.__buffer.next()
            self.__actions_log.append(f"Imprimindo {current_doc.title} - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
            sleep(current_doc.page_num)
            self.__actions_log.append(f"Imprimiu {current_doc.title} - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")



d1 = Document("relatorio_anual.pdf", 5, "alice")
d2 = Document("contrato.docx", 2, "bruno")
d3 = Document("apresentacao.pptx", 8, "carla")
d4 = Document("manual_usuario.pdf", 12, "diego")
d5 = Document("planilha_gastos.xlsx", 1, "elena")

b = Buffer()

p = Printer(b)
for d in [d1,d2,d3,d4,d5]:
    p.add_doc(d)
p.print()
print(p.show_log())