'''
nombre:Monserat Orduña Basaldua
descripcion:lab 3.2.1.16
Fecha:06/11/2023
'''
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.insert(0, item)  

    def get(self):
        if not self.items:
            raise QueueError("Cola vacia")  
        return self.items.pop()  
    def is_empty(self):
        return not bool(self.items)  


q = Queue()
q.put(1)
q.put("perro")
q.put(False)

try:
    print(q.get())  
    print(q.get())  
    print(q.get())  
    print(q.get())  
except QueueError as e:
    print(e)  

print(q.is_empty())  