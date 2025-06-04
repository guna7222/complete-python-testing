# 18. Python program to interchange first and last elements in a list

class InterchangeListElements:

    def __init__(self, list_of_items):
        self.list_of_items = list_of_items

    def interchange_first_and_last_element(self):
        data = self.list_of_items
        first_item = data[0]
        last_item = data[-1]
        print(first_item, last_item)
        data[0] =  last_item
        data[-1] =  first_item
        return data

    def message(self):
        return_data = self.interchange_first_and_last_element()
        print(return_data)
        print(f"Interchanged values {return_data}")


# object creation
items = ["python", "go", "docker", "java"]
creation = InterchangeListElements(items)
creation.message()