# class Employee:
#     def __init__(self):
#         self.name="Mouni"
#         self.age=22
#         self.position="CEO"
#     def display_employee_info(self):
#         print("Employee information:")
#         print("-------------------")  
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"position:{self.position}")

# employee1=Employee()
# employee1.display_employee_info()          



# class Employee:
#     employee_count=0
#     def __init__(self,name,age,position):
#         self.name=name
#         self.age=age
#         self.position=position
#         Employee.employee_count+=1
#     def display_employee_info(self):
#         print("Employee information:")
#         print("-------------------")  
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"position:{self.position}")
#     @classmethod    
#     def get_total_count(cls):
#         return cls.employee_count    

# employee1=Employee("mouni",22,"software")
# employee1.display_employee_info()  
# employee1.get_total_count()
# employee2=Employee("roshini",20,"analyst") 
# employee2.display_employee_info() 

# print(f"total employee:{Employee.get_total_count()}")


"""    Home work   :1)create a class with department
departed,department name,location
through the consructoreinitiaizthe dep attribues ,create  methd to diplay the dept information and then display total departments in your organaization

2)everything with hardcoded with objects

i-> take users input
ii-> take no of users
iii ->create a list or dictionary to store different department ,use for loop t displa the dictonary values
iV->search department name using department Id
v-> add  afunction to search dept by name




and also codeshare.io/bvritpython4
codeshare.io/bvritpython5    problems



"""

# class Department:
#     count_of_dept=0
#     def __init__(self,dept_Id,dept_name,location):
#         self.dept_Id=dept_Id
#         self.dept_name=dept_name
#         self.location=location
#         Department.count_of_dept+=1
#     def department_info(self):
#         print("Department details")
#         print("----------------")
#         print(f"Department id:{self.dept_Id}")
#         print(f"Department name:{self.dept_name}")
#         print(f"location :{self.location}")
#     @classmethod
#     def total_department(cls):
#         return cls.count_of_dept
    
# dept1=Department(1,"Mouni","Hyderabad")
# dept1.department_info()
# dept2=Department(2,"Chinni","chennai")
# dept2.department_info()
# print(f"Total department={Department.total_department()}")



class Department:
    count_of_dept=0
    def __init__(self,dept_Id,dept_name,location):
        self.dept_Id=dept_Id
        self.dept_name=dept_name
        self.location=location
        Department.count_of_dept+=1
    def department_info(self):
        print("Department details")
        print("----------------")
        print(f"Department id:{self.dept_Id}")
        print(f"Department name:{self.dept_name}")
        print(f"location :{self.location}")
    @classmethod
    def total_department(cls):
        return cls.count_of_dept
    
    @staticmethod
    def search_by_id(departments,search_id):
        for dept in departments:
            if dept.dept_Id==search_id:
                print("department found by id")
                dept.department_info()
                return
        print("department id not found")    

    @staticmethod
    def search_by_name(departments,search_name):
        for dept in departments:
            if dept.dept_name==search_name:
                print("department found by name")
                dept.department_info()
                return
        print("Invalid department name")    
    


num=int(input("enter no of departments"))
departments=[]
for i in range(num):
    print(f"\nEnter the details of department {i+1}")
    dept_id=int(input("Enter the department id"))
    dept_name=input("Enter Department name")
    location=input("Enter the location")

    dept=Department(dept_id,dept_name,location)
    departments.append(dept)

    for depts in departments:
        print(depts.department_info())

print(f"Total departments ={Department.count_of_dept}") 


while True:
    print("Search options:")
    print("1.search by department Id")
    print("2.Searc by department")
    choice =int(input("enter the choice") )
    if choice ==1:
        search_id=int(input("Enter the department id"))
        Department.search_by_id(departments,search_id)
        break
    elif(choice==2):
        search_name=input("Enter the department name")
        Department.search_by_name(departments,search_name)
        break
    else:
        print("Invalid choice")

    

    