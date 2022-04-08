import datetime


class House:
    houses_list = []

    # статические поля
    id = 0
    street = 'Nezavisimosti'

    # конструктор / динамические поля / магический метод
    def __init__(self, square, floor, qty_rooms, building_type, service_time):
        self.square = square
        self.floor = floor
        self.qty_rooms = qty_rooms
        self.building_type = building_type
        self.service_time = service_time
        House.id += 1

    # метод класса
    @classmethod
    def set_house_id(cls):
        return cls.id

    def get_apartment_number(self):
        return self.__apartment_number

    # функции-члены реализуют запись и считывание полей (проверка корректности)
    # инкапсулированное поле
    def set_apartment_number(self, apartment_number):
        if apartment_number > 0:
            self.__apartment_number = apartment_number
        else:
            print("Номер квартиры должен быть больше 0!")

    # открытое поле
    def set_square(self, square):
        if square > 0:
            self.square = square
        else:
            print("Площадь должна быть больше 0!")

        # статический метод

    @staticmethod
    def service_time_calc(service_time):
        return datetime.datetime.now().year - service_time

    # метод для расчета необходимости в кап. ремонте (кап.ремонт необходим после 50 лет эксплуатации)

    def renovation_need(self):
        inuse_time = datetime.datetime.now().year - self.service_time
        print('Дом эксплуатируется', inuse_time, 'лет')
        if inuse_time > 50:
            print('Дом нуждается в капитальном ремонте')
        else:
            print('Дом в капитальном ремонте на данный момент не нуждается')

    # метод для вывода списка квартир, имеющих заданное число комнат + магический метод

    def get_room_list(self, rooms_number_sorted):
        new_house_list = []
        i = 0
        while i < len(self.houses_list):
            if self.houses_list.__getitem__(i).qty_rooms == rooms_number_sorted:
                new_house_list.append(self.houses_list.__getitem__(i))
            i += 1
        return new_house_list

    # метод для изменения представления экземпляра класса / магический метод

    def __str__(self):
        return f'rooms quantity = {self.qty_rooms}, floor = {self.floor}, square = {self.square}, ' \
               f'type of the building = {self.building_type}, was built in {self.service_time}'

    # метод для вывода списка квартир, имеющих заданное число комнат и расположенных на этаже,
    # который находится в заданном промежутке + магический метод

    def get_room_and_floor(self, rooms_number_sorted, floor_min, floor_max):
        new_house_list = []
        i = 0
        while i < len(self.houses_list):
            if (self.houses_list.__getitem__(i).qty_rooms == rooms_number_sorted) and (
                    floor_min < self.houses_list.__getitem__(i).floor < floor_max):
                new_house_list.append(self.houses_list.__getitem__(i))
            i += 1
        return new_house_list


# создание 2 объектов класса
first_house = House(45.2, 2, 2, 'block of flats', 1963)
second_house = House(61.5, 4, 1, 'town house', 2012)

first_house.set_apartment_number(5)
House.set_apartment_number(second_house, 11)

# создание 10 объектов класса
House.houses_list = [House(45.2, 2, 2, 'block of flats', 1963), House(61.5, 4, 2, 'town house', 2012),
                     House(81.5, 3, 3, 'town house', 2012), House(39.8, 8, 1, 'block of flats', 1961),
                     House(95.2, 4, 4, 'block of flats', 2010), House(67.8, 5, 2, 'block of flats', 1961),
                     House(100.4, 2, 3, 'town house', 2015), House(84.7, 1, 3, 'town house', 2017),
                     House(69.1, 2, 2, 'town house', 2010), House(48.3, 4, 2, 'block of flats', 1963)]


# вспомогательные методы/для наведения красоты при выводе информации + магический метод
def print_list_defined_rooms(class_name, param_sorted):
    i = 0
    list_required = House.get_room_list(class_name, param_sorted)
    while i < len(list_required):
        print(i+1, ') ', list_required.__getitem__(i))
        i += 1


def print_list_defined_rooms_and_floor(class_name, param_sorted, param_min, param_max):
    i = 0
    list_required = House.get_room_and_floor(class_name, param_sorted, param_min, param_max)
    while i < len(list_required):
        print(i+1, ') ', list_required.__getitem__(i))
        i += 1


# реализация методов
print('Анализ потребности в кап.ремонте')
first_house.renovation_need()
second_house.renovation_need()
print('************************************************')

print('Cписок квартир, имеющих заданное число комнат:\n')
print_list_defined_rooms(House, 2)
print('************************************************')

print('Cписок квартир с заданным числом комнат и расположенных на этаже в заданном промежутке\n')
print_list_defined_rooms_and_floor(House, 3, 2, 5)
print('************************************************')