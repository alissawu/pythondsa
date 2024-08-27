#Construct a class hierarchy for people on a college campus. 
# Include faculty, staff, and students. 
# What do they have in common? What distinguishes them from one another?
class People:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    #self.name not name bc self.name is of the object
    def show(self):
        print(f"Name: {self.name}, Role: {self.role}, ID: {self.ID}")
    def __str__(self):
        print(f"Name: {self.name}, Role: {self.role}, ID: {self.ID}")

class Faculty(People):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.role = "Faculty"
        self.department = department
    def show(self):
        print(f"Name: {self.name}, Role: {self.role}, ID: {self.ID}, Department: {self.department}")
    def __str__(self):
        print(f"Name: {self.name}, Role: {self.role}, ID: {self.ID}, Department: {self.department}")
    


#etc..
