# implementação referente ao exercício 2 da lista de exercícios
class Contact:

    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Nome: {self.__name}, telefone: {self.__phone}'


class ContactList:

    def __init__(self):
        self.__contacts = list()

    def add(self, contact: Contact):
        for i, c in enumerate(self.__contacts):
            if contact.name.lower() < c.name.lower():
                self.__contacts.insert(i, contact)
                return
        self.__contacts.append(contact)

    def search_by_name(self, contact: Contact):
        return [c for c in self.__contacts if c.name == contact.name]
        """
        A linha acima é equivalente ao seguinte trecho
        for c in self.__contacts:
            if c.name == contact.name:
                return c
        return None        
        """

    def remove(self, contact: Contact):
        self.__contacts.remove(contact)

    def list_all(self):
        for c in self.__contacts:
            print(c)