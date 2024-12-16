import re
import json

class Supplier:
    def __init__(self, supplier_id, first_name, last_name, address, phone):
        self.set_supplier_id(supplier_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_phone(phone)

    # Классовый метод для создания объекта из JSON
    @classmethod
    def from_json(cls, data_json):
        try:
            data = json.loads(data_json)
            return cls(
                supplier_id=data["supplier_id"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                address=data["address"],
                phone=data["phone"]
            )
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Ошибка при разборе JSON: {e}")

    # Getters
    def get_supplier_id(self):
        return self.__supplier_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    # Setters с валидацией
    def set_supplier_id(self, supplier_id):
        if not self.validate_id(supplier_id):
            raise ValueError("Supplier ID должен быть положительным целым числом.")
        self.__supplier_id = supplier_id

    def set_first_name(self, first_name):
        if not self.validate_name(first_name):
            raise ValueError("Имя должно быть непустой строкой.")
        self.__first_name = first_name

    def set_last_name(self, last_name):
        if not self.validate_name(last_name):
            raise ValueError("Фамилия должна быть непустой строкой.")
        self.__last_name = last_name

    def set_address(self, address):
        if not self.validate_address(address):
            raise ValueError("Адрес должен быть строкой длиной не менее 5 символов.")
        self.__address = address

    def set_phone(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Неверный формат телефона.")
        self.__phone = phone

    # Статические методы для валидации
    @staticmethod
    def validate_id(supplier_id):
        return isinstance(supplier_id, int) and supplier_id > 0

    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def validate_address(address):
        return isinstance(address, str) and len(address.strip()) >= 5

    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?\d{7,15}$'  # Номер телефона: от 7 до 15 цифр с возможным "+" в начале
        return isinstance(phone, str) and re.fullmatch(pattern, phone)

    # Полная версия объекта
    @property
    def full_version(self):
        return (f"Supplier(supplier_id={self.__supplier_id}, first_name={self.__first_name}, "
                f"last_name={self.__last_name}, address={self.__address}, phone={self.__phone})")

    # Краткая версия объекта
    @property
    def short_version(self):
        return f"Supplier({self.__first_name} {self.__last_name})"

    # Сравнение объектов на равенство
    def __eq__(self, other):
        if isinstance(other, Supplier):
            return (self.__supplier_id == other.__supplier_id and
                    self.__first_name == other.__first_name and
                    self.__last_name == other.__last_name and
                    self.__address == other.__address and
                    self.__phone == other.__phone)
        return False

    