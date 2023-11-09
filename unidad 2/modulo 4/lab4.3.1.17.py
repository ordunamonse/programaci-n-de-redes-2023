'''
nombre:Monserat Orduña Basaldua
descripcion:lab 4.3.1.17
Fecha:08/11/2023
'''
class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, line):
        self.line = line
        super().__init__("Línea incorrecta: " + line)

class FileEmpty(StudentsDataException):
    def __init__(self, filename):
        self.filename = filename
        super().__init__("El archivo {} está vacío.".format(filename))

def process_student_data(filename):
    students_data = {}

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise FileEmpty(filename)

            for line in lines:
                try:
                    name, surname, points = line.strip().split()
                    points = float(points)
                    students_data[name + ' ' + surname] = students_data.get(name + ' ' + surname, 0) + points
                except ValueError:
                    raise WrongLine(line)

    
        for student, total_points in sorted(students_data.items()):
            print(f"{student} \t {total_points}")

    except FileNotFoundError:
        print("El archivo {} no se encuentra.".format(filename))
    except FileEmpty as e:
        print(e)
    except WrongLine as e:
        print(e)


nombre_archivo = input("Introduce el nombre del archivo del profesor Jekyll: ")

process_student_data(nombre_archivo)
