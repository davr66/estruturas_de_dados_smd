from abc import ABC, abstractmethod
import unittest


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere na posição <indice> o valor <elemento>.
        Como se trata de uma lista, deve ser garantido que
        se houver valor em <indice> que ele não seja apagado"""
        ...

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrência de <elemento>"""
        ...

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista"""
        ...

    @abstractmethod
    def clear(self):
        """Apaga a lista"""
        ...

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro índice de <elemento>"""
        ...

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        ...

    @abstractmethod
    def remove_all(self, item):
        """Remove todas as ocorrências de <item>"""
        ...

    @abstractmethod
    def remove_at(self, index):
        """Remove o elemento na posição <index>"""
        ...

    @abstractmethod
    def append(self, item):
        """Adiciona <item> ao final da lista - Concatenação"""
        ...

    @abstractmethod
    def replace(self, index, item):
        """Substitui o elemento na posição <index> por <item>"""
        ...


class Node:

    def __init__(self, element=None, next=None):
        self.__element = element
        self.__next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, element):
        self.__element = element

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '|' + self.__element.__str__() + '|'

    def __eq__(self, other):
        result = False
        if isinstance(other, Node) and other.element == self.element and other.next == self.next:
            result = True
        return result


class LinkedList(ListADT):

    def __init__(self, tamanho=0):
        if tamanho:
            self._head = Node()
            self._tail = self._head
            aux = self._head
            for i in range(1, tamanho):
                aux.next = Node()
                self._tail = aux.next
                aux = aux.next
            self._length = tamanho
        else:
            self._head = None
            self._tail = None
            self._length = 0

    def insert(self, index, elem):
        # a inserção pode acontecer em três locais: início, meio e fim da lista
        # separei em métodos diferentes (privados) para facilitar o entendimento
        if index == 0:  # primeiro local de inserção é no começo da lista
            self.__insert_at_beginning(elem)
        elif index > self._length:  # segundo local de inserção é no fim da lista
            self.__insert_at_end(elem)  # se o índice passado foi maior que o tamanho da lista, insero no fim
        else:  # por fim, a inserção no meio da lista
            self.__insert_in_between(index, elem)

        self._length += 1  # após inserido, o tamanho da lista é modificado

    def __insert_at_beginning(self, elem):
        n = Node(elem)  # primeiro criamos o nó com o elemento a ser inserido
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:  # se houver elemento na lista
            n.next = self._head  # o head atual passa a ser o segundo elemento
            self._head = n  # e o novo nó criado passa a ser o novo head

    def __insert_at_end(self, elem):
        n = Node(elem)  # primeiro criamos o nó com o elemento a ser inserido
        if self.empty():  # caso particular da lista vazia
            self.__empty_list_insertion(n)
        else:
            self._tail.next = n  # o último elemento da lista aponta para o nó criado
            self._tail = n  # o nó criado passa a ser o último elemento

    def __empty_list_insertion(self, node):
        # na inserção na lista vazia, head e tail apontam para o nó
        self._head = node
        self._tail = node

    def __insert_in_between(self, index, elem):
        n = Node(elem)  # primeiro criamos o nó com o elemento a ser inserido
        pos = 0  # a partir daqui vamos localizar a posição de inserção
        aux = self._head  # variável auxiliar para nos ajudar na configuração da posição do novo nó
        while pos < index - 1:  # percorre a lista até a posição imediatamente anterior
            aux = aux.next  # à posição onde o elemento será inserido
            pos += 1
        n.next = aux.next  # quando a posição correta tiver sido alcançada, insere o nó
        aux.next = n

    # TODO ajustar tail quando o último elemento foi removido
    def remove(self, elem):
        removed = False  # Flag que marca quando a remoção foi feita
        if not self.empty():  # Só pode remover se a lista não estiver vazia, não é?!
            aux: Node = self._head
            if aux.element == elem:  # Caso especial: elemento a ser removido está no head
                self._head = aux.next  # head passa a ser o segundo elemento da lista
                removed = True
            else:
                while aux.next and not removed:  # verifico se estamos no fim da lista e não foi removido elemento
                    prev = aux
                    aux = aux.next  # passo para o próximo elemento
                    if aux.element == elem:  # se for o elemento desejado, removo da lista
                        prev.next = aux.next
                        removed = True  # marco que foi removido
            if removed:
                self._length -= 1

    def count(self, elem):
        counter = 0
        if not self.empty():  # Verifica se a lista não está vazia (só faz sentido contar em listas não vazias!)
            aux = self._head  # Se a lista não estiver vazia, percorre a lista contando as ocorrências
            if aux.element is elem:
                counter += 1
            while aux.next:  # percorrendo a lista....
                aux = aux.next
                if aux.element is elem:
                    counter += 1
        return counter

    def clear(self):
        self._head = None  # todos os nós que compunham a lista serão removidos da memória pelo coletor de lixo
        self._tail = None
        self._length = 0

    def index(self, elem):
        result = None
        pos = 0
        aux = self._head
        # Vamos percorrer a lista em busca de elem
        while not result and pos < self._length:  # lembrando que not None é o mesmo que True
            if aux.element is elem:
                result = pos
            aux = aux.next
            pos += 1
        return result  # se o elemento não estiver na lista, retorna None

    def length(self):
        return self._length

    def empty(self):
        result = False
        if not self._head:
            result = True
        return result

    def remove_all(self, item):
        while self.index(item) is not None:
            self.remove(item)

    # TODO ajustar tail quando o último elemento foi removido
    def remove_at(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        if index == 0:
            self._head = self._head.next
        else:
            aux = self._head
            for _ in range(index - 1):
                aux = aux.next
            aux.next = aux.next.next
        self._length -= 1

    def append(self, item):
        self.insert(self._length, item)

    def replace(self, index, item):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._head
        for _ in range(index):
            aux = aux.next
        aux.element = item

    def __str__(self):
        if not self.empty():
            result = ''
            aux: Node = self._head
            result += aux.__str__()
            while aux.next:
                aux = aux.next
                result += aux.__str__()
            return result
        else:
            return '||'

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        node = self.__get_node_at(index)
        result = None
        if node:
            result = node.element
        return result

    def __get_node_at(self, index):
        result = None
        if not self.empty():
            result = self._head
            while index > 0:
                result = result.next
                index -= 1
        return result

    def __setitem__(self, key, value):
        node = self.__get_node_at(key)
        if node:
            node.element = value


class DoublyLinkedList(ListADT):
    class _DoublyNode:
        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

        def __str__(self):
            if self._elem is not None:
                return str(self._elem) + ' '
            else:
                return '|'

        @property
        def element(self):
            return self._elem

        @element.setter
        def element(self, elem):
            self._elem = elem

        @property
        def previous(self):
            return self._prev

        @previous.setter
        def previous(self, node):
            self._prev = node

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, node):
            self._next = node

    def __init__(self, size=0):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._length = 0

    def __len__(self):
        return self._length

    def insert(self, index, elem):
        if index >= self._length:
            index = self._length
        if self.empty():
            new_node = self._DoublyNode(elem, self._header, self._trailer)
            self._header.next = new_node
            self._trailer.previous = new_node
        elif index == 0:
            new_node = self._DoublyNode(elem, self._header, self._header.next)
            self._header.next.previous = new_node
            self._header.next = new_node
        else:
            this = self._header.next
            successor = this.next
            pos = 0
            while pos < index - 1:
                this = successor
                successor = this.next
                pos += 1
            new_node = self._DoublyNode(elem, this, successor)
            this.next = new_node
            successor.previous = new_node

        self._length += 1

    def remove(self, elemento):
        if not self.empty():
            node = self._header.next
            pos = 0
            found = False
            while not found and pos < self._length:
                if node.element == elemento:
                    found = True
                else:
                    node = node.next
                    pos += 1
            if found:
                node.previous.next = node.next
                node.next.previous = node.previous
                self._length -= 1

    def count(self, elem):
        result = 0
        this = self._header.next
        if self._length > 0:
            while this.next is not None:
                if this.element == elem:
                    result += 1
                this = this.next
        return result

    def clear(self):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._length = 0

    def index(self, elem):
        result = None
        pos = 0
        this = self._header.next
        while not result and pos < self._length:
            if this.element is elem:
                result = pos
                break
            this = this.next
            pos += 1
        return result

    def length(self):
        return self._length

    def empty(self):
        return self._length == 0

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._header
            result += aux.__str__()
            while aux.next:
                aux = aux.next
                result += aux.__str__()
            return result
        else:
            return '||'

    def remove_all(self, item):
        while self.index(item) is not None:
            self.remove(item)

    def remove_at(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        if index == 0:
            self._header.next = self._header.next.next
            self._header.next.previous = self._header
        elif index == self._length - 1:
            self._trailer.previous = self._trailer.previous.previous
            self._trailer.previous.next = self._trailer
        else:
            aux = self._header.next
            for _ in range(index):
                aux = aux._next
            aux.previous.next = aux.next
            aux.next.previous = aux.previous
        self._length -= 1

    def append(self, item):
        self.insert(self._length, item)

    def replace(self, index, item):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._header.next
        for _ in range(index):
            aux = aux.next
        aux.element = item


class TestLinkedList(unittest.TestCase):

    def test_inserting_element_at_specific_index(self):
        lista = LinkedList()
        lista.insert(0, "a")
        lista.insert(1, "b")
        lista.insert(1, "c")
        self.assertEqual(lista.length(), 3)
        self.assertEqual(lista.index("c"), 1)
        self.assertEqual(lista.index("a"), 0)
        self.assertEqual(lista.index("b"), 2)

    def test_removing_first_occurrence_of_element(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        lista.remove("a")
        self.assertEqual(lista.count("a"), 1)

    def test_counting_occurrences_of_element(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        self.assertEqual(lista.count("a"), 2)
        self.assertEqual(lista.count("b"), 1)

    def test_clearing_all_elements(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        lista.clear()
        self.assertEqual(lista.length(), 0)

    def test_retrieving_index_of_element(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        self.assertEqual(lista.index("b"), 1)

    def test_removing_all_occurrences_of_element(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        lista.remove_all("a")
        self.assertEqual(lista.count("a"), 0)

    def test_removing_element_at_specific_index(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("c")
        lista.remove_at(1)
        self.assertEqual(lista.index("c"), 1)
        self.assertEqual(lista.index("a"), 0)
        self.assertIsNone(lista.index('b'))

    def test_appending_element_to_end(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        self.assertEqual(lista.index("b"), 1)

    def test_replacing_element_at_specific_index(self):
        lista = LinkedList()
        lista.append("a")
        lista.append("b")
        lista.replace(1, "c")
        self.assertEqual(lista.index("c"), 1)


class TestDoublyLinkedList(unittest.TestCase):

    def test_inserting_element_at_specific_index(self):
        lista = DoublyLinkedList()
        lista.insert(0, "a")
        lista.insert(1, "b")
        lista.insert(1, "c")
        self.assertEqual(lista.length(), 3)
        self.assertEqual(lista.index("c"), 1)
        self.assertEqual(lista.index("a"), 0)
        self.assertEqual(lista.index("b"), 2)

    def test_removing_first_occurrence_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        lista.remove("a")
        self.assertEqual(lista.count("a"), 1)

    def test_counting_occurrences_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        self.assertEqual(lista.count("a"), 2)
        self.assertEqual(lista.count("b"), 1)

    def test_clearing_all_elements(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.clear()
        self.assertEqual(lista.length(), 0)

    def test_retrieving_index_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        self.assertEqual(lista.index("b"), 1)

    def test_removing_all_occurrences_of_element(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("a")
        lista.remove_all("a")
        self.assertEqual(lista.count("a"), 0)

    def test_removing_element_at_specific_index(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.append("c")
        lista.remove_at(1)
        self.assertEqual(lista.index("c"), 1)
        self.assertEqual(lista.index("a"), 0)
        self.assertIsNone(lista.index('b'))

    def test_appending_element_to_end(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        self.assertEqual(lista.index("b"), 1)

    def test_replacing_element_at_specific_index(self):
        lista = DoublyLinkedList()
        lista.append("a")
        lista.append("b")
        lista.replace(1, "c")
        self.assertEqual(lista.index("c"), 1)