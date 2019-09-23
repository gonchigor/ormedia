'''
Есть класс Person, конструктор которого принимает три параметра
(не учитывая self) – имя, фамилию и квалификацию специалиста.
Квалификация имеет значение заданное по умолчанию, равное единице.
У класса Person есть метод, который возвращает строку,
включающую в себя всю информацию о сотруднике.
'''


class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def info(self):
        return ' '.join((self.name, self.surname, 'квалификация:',
                        str(self.qualification)))


def main():
    person = Person('Bill', 'Gates')
    print(person.name)
    print(person.surname)
    print(person.qualification)
    print(person.info())


if __name__ == '__main__':
    main()
