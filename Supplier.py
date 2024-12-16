class Supplier:
    def __init__(self, supplier_id, first_name, last_name, address, phone):
        self.__supplier_id = supplier_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__phone = phone
    
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
    
    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone
        
    
   
