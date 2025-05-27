# Determine the type of object in Python

class DetermineTypeOfAnObject:

    def __init__(self, obj):
        self.obj = obj

    def check_object_type(self):
        print(type(self.obj))



type_obj = DetermineTypeOfAnObject(5)
type_obj.check_object_type()

type_obj1 = DetermineTypeOfAnObject("Python3")
type_obj1.check_object_type()