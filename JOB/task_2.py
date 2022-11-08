class DescriptWoreker:

    def __set_name__(self, owner_class, num):
        self._num = num
    def __get__(self, instance, owner_class):
        return instance.__dict__[self._num]        
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отритцательного значения!!!")
        instance.__dict__[self._num] = value

class Worker:

    wage = DescriptWoreker()
    bonus = DescriptWoreker()
    
    def __init__(self, name, surname, position, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self.name = name
        self.surname = surname
        self.position = f"Должность: {position}"

class Position(Worker):
    def get_full_name(self):
        return print (f"Полное имя: {self.name} {self.surname}")
    def get_total_income(self):
        return print (f"Доход с учетом премии: {self.wage + self.bonus}")

obj = Position('Erling', 'Holland', 'footballer', 45000, 3000)
obj.get_full_name()
obj.get_total_income()

obj = Position('Костик', 'Тучкин', 'Дворник', -33000,-2000)
obj.get_full_name()
obj.get_total_income()