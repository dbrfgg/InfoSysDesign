import re

class BaseSupplier:
    def __init__(self, first_name, last_name, contact, supplier_id=None):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_contact(contact)
        self.set_supplier_id(supplier_id)

    # Геттеры
    def get_supplier_id(self):
        return self.__supplier_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_contact(self):
        return self.__contact

    # Сеттеры 
    def set_first_name(self, first_name):
        if not self.validate_name(first_name):
            raise ValueError("Имя должно быть непустой строкой.")
        self.__first_name = first_name.strip()

    def set_last_name(self, last_name):
        if not self.validate_name(last_name):
            raise ValueError("Фамилия должна быть непустой строкой.")
        self.__last_name = last_name.strip()

    def set_contact(self, contact):
        if not self.validate_contact(contact):
            raise ValueError("Неверный формат контактного телефона.")
        self.__contact = contact.strip()

    def set_supplier_id(self, supplier_id):
        if supplier_id is not None and not self.validate_id(supplier_id):
            raise ValueError("Supplier ID должен быть положительным числом.")
        self.__supplier_id = supplier_id if supplier_id else 0

    # Строковое представление объекта
    def __str__(self):
        initials = f"{self.__first_name[0].upper()}." if self.__first_name else ""
        return f"BaseSupplier: {self.__last_name} {initials} (Contact: {self.__contact})"

    def __repr__(self):
        return self.__str__()

    # Сравнение объектов на равенство
    def __eq__(self, other):
        if isinstance(other, BaseSupplier):
            return (self.__last_name == other.__last_name and
                    self.__first_name == other.__first_name and
                    self.__contact == other.__contact and
                    self.__supplier_id == other.__supplier_id)
        return False

    # Хеширование для использования в коллекциях
    def __hash__(self):
        return hash((self.__last_name, self.__first_name, self.__contact, self.__supplier_id))

    # Статические методы для валидации
    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def validate_contact(contact):
        pattern = r'^\+?\d{7,15}$'  # Номер телефона: от 7 до 15 цифр с возможным "+" в начале
        return isinstance(contact, str) and re.fullmatch(pattern, contact)

    @staticmethod
    def validate_id(supplier_id):
        return isinstance(supplier_id, int) and supplier_id > 0
