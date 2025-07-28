class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


lead = TeamLead("Іван", 5000, "R&D", "Python", 5)

print(hasattr(lead, "name"))                   
print(hasattr(lead, "salary"))
print(hasattr(lead, "department"))
print(hasattr(lead, "programming_language"))
print(hasattr(lead, "team_size"))
