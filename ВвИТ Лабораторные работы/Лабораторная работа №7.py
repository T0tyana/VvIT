class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        return f'Имя сотрудника: {self.name}\nID сотрудника: {self.employee_id}'

class Manager(Employee):
    def __init__(self,name, employee_id, department):
        Employee.__init__(self, name, employee_id)
        self.department = department

    def manage_project(self):
        return f'{self.name} руководит проектом в отделе {self.department}'

    #def get_info(self):
        #return f'{super().get_info()}'

class Technician(Employee):
    def __init__(self, name, employee_id, specialization):
        Employee.__init__(self, name, employee_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.name} выполняет техническое обслуживаение в области {self.specialization}'

    #def get_info(self):
        #return f'{super().get_info()}'

class TechManager(Manager, Technician):
    def __init__(self, name, employee_id, department, specialization):
        Manager.__init__(self, name, employee_id, department)
        Technician.__init__(self, name, employee_id, specialization)
        self.team = []

    def project(self):
        return f'{Manager.manage_project(self)}'

    def maintenance(self):
        return f'{Technician.perform_maintenance(self)}'

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        info = 'Информация о команде:\n______________________\n'
        for employee in self.team:
            info += employee.get_info()+'\n'+'______________________'+'\n'
        return info

    def get_info(self):
        return f'Имя сотрудника: {self.name}\nID сотрудника: {self.employee_id}'

Miky = Employee('Miky', 213031)
print(Miky.get_info())
print()

Chloe = Manager('Chloe', 102310, 'Business')
print(Chloe.manage_project())
print(Chloe.get_info())
print()

Kriss = Technician('Kriss', 102311, 'Networking')
print(Kriss.perform_maintenance())
print(Kriss.get_info())
print()

Alec = TechManager('Alec', 101002, 'IT', 'System Administration')
print(Alec.manage_project())
print(Alec.perform_maintenance())
print(Alec.get_info())
print()

Alec.add_employee(Miky)
Alec.add_employee(Chloe)
Alec.add_employee(Kriss)

print(Alec.get_team_info())