class Person:
    pass

class Worker(Person):
    pass

class Studenet(Person):
    pass

class Teacher(Person):
    pass

class Factory:
    def get_person(self,p_type:str) -> Person:
        if p_type == 'w':
            return Worker()
        if p_type =='s':
            return Studenet()
        if p_type =="t":
            return Teacher()