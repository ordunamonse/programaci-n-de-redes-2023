'''
nombre:Monserat Orduña Basaldua
descripcion:lab 3.4.1.13
Fecha:06/11/2023
'''
class WeekDayError(Exception):
    pass

class Weeker:
    DAYS = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

    def __init__(self, day):
        if day not in self.DAYS:
            raise WeekDayError("Lo siento, no puedo atender tu solicitud.")
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        current_index = self.DAYS.index(self.__day)
        new_index = (current_index + n) % 7
        self.__day = self.DAYS[new_index]

    def subtract_days(self, n):
        current_index = self.DAYS.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = self.DAYS[new_index]

try:
    day1 = Weeker("Lun")
    print(day1)  

    day1.add_days(1)
    print(day1)  

    day1.subtract_days(2)
    print(day1)  

    day2 = Weeker("Viernes")  
except WeekDayError as e:
    print(e)  
