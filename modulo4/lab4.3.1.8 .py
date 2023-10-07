'''
nombre:Monserat Orduña Basaldua
Descripcion: Laboratorio 4.3.1.8
Fecha:06/10/2023
'''

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        return None

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    total_days = day
    for m in range(1, month):
        days_in_current_month = days_in_month(year, m)
        if days_in_current_month is None:
            return None
        total_days += days_in_current_month
    
    return total_days


print(day_of_year(2000, 12, 31))  
print(day_of_year(2023, 10, 6))   
print(day_of_year(2023, 2, 29))    
print(day_of_year(2023, 13, 1))    
print(day_of_year(2023, 7, 0))     




