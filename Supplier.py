import re
import json
from BaseSupplier import BaseSupplier

class Supplier(BaseSupplier):
    def __init__(self, first_name, last_name, address, phone, supplier_id=None):
        # Вызов родительского конструктора
        super(Supplier, self).__init__(first_name=first_name, last_name=last_name, supplier_id=supplier_id)
        self.set_address(address)
        self.set_phone(phone)

    # Классовый метод для создания объекта из JSON
    @classmethod
    def from_json(cls, data_json):
        try:
            data = json.loads(data_json)
            return cls(
                supplier_id=data.get("supplier_id"),  # Безопаснее использовать get() для предотвращения KeyError
                first_name=data["first_name"],
                last_name=data["last_name"],
                address=data["address"],
                phone=data["phone"]
            )
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Ошибка при разборе JSON: {e}")

    # Геттеры
    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    # Сеттеры с валидацией
    def set_address(self, address):
        if not self.validate_address(address):
            raise ValueError("Адрес должен быть строкой длиной не менее 5 символов.")
        self.__address = address.strip()

    def set_phone(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Неверный формат телефона.")
        self.__phone = phone.strip()

    # Статические методы для валидации
    @staticmethod
    def validate_address(address):
        return isinstance(address, str) and len(address.strip()) >= 5

    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?\d{7,15}$'  # Номер телефона: от 7 до 15 цифр с возможным "+" в начале
        return isinstance(phone, str) and re.fullmatch(pattern, phone)

    # Строковое представление для краткой версии объекта
    @property
    def short_version(self):
        return f"Supplier({self.get_first_name()} {self.get_last_name()})"

    # Полная версия объекта
    @property
    def full_version(self):
        return (f"Supplier(supplier_id={self.get_supplier_id()}, first_name={self.get_first_name()}, "
                f"last_name={self.get_last_name()}, address={self.get_address()}, phone={self.get_phone()})")
