'''
nombre:Monserat Orduña Basaldua
descripcion:lab 4.6.1.13
Fecha:08/11/2023
'''
from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            month_calendar = self.monthdays2calendar(year, month)
            for week in month_calendar:
                for day, day_of_week in week:
                    if day != 0 and day_of_week == weekday:
                        count += 1
        return count


cal = MyCalendar()

print(cal.count_weekday_in_year(2019, 0)) 


print(cal.count_weekday_in_year(2000, 6))  
