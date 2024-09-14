# Задание 1
# Для закрепления принципов ООП давайте потренируемся создавать
# программы, которые пока что не имеют практической применимости,
# но зато с ними легче и веселее работать.
# Задача:
# - создать класс “Car” (Машина).
# - Свойства, которые должны задаваться при создании экземпляра
# класса:
# - Цвет
# - Количество топлива
# - Расход топлива на 100 км
# - Пробег - по умолчанию 0
# - Методы, которые должны быть у машины:
# - drive
# - Принимает в себя аргумент - количество км, которые
# надо проехать. Если топлива хватает - уменьшаем
# количество топлива, пишем “Мы проехали … км”. Если
# не хватает - пишем “Не хватает топлива”
# - get_mileage
# - Возвращает пробег
class Car:
    def __init__(self, color, fuel, consumption, mileage=0, ):
        self.color = color
        self.fuel = fuel
        self.consumption = consumption
        self.mileage = mileage
        print(f'создали машину {self.color, self.fuel}')


    def drive(self, km):
        need_fuel = (km * self.consumption)/100
        if need_fuel <= self.fuel:
            print(f'мы проехали {km} км')
            self.fuel -= need_fuel
            self.mileage += km
        else:
            print('не доедем :)')

    def get_mileage(self):
        return self.mileage




car = Car(color='yellow', fuel=20, consumption=5)


for i in range(6):
    car.drive(100)
print(car.get_mileage())























