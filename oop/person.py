print("Hello world")
APPROVED_JOBS = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
class Person:
    def __init__(self,name="John",job="Admin"):
        self.name=name
        self.job=job 
        # print(f"{name}")
        # print(f"{job}")
    def get_name(self):
        return self._name 
    def set_name(self,name):
        if isinstance(name,str) and 1 <= len(name) <=25:
            self._name=name.title()
        else:
            print(f"{name} <== must be a string between 1 and 25 characters")
    name=property(get_name,set_name)
    def get_job(self):
        print("Retrieving the job title")
        return self._job 
    def set_job(self,job):
        if job in APPROVED_JOBS:
            print(f"Setting job to: {job}")
            self._job=job 
        else:
            print(f"{job} <== must be in list of approved jobs")
    job=property(get_job,set_job)
ian=Person("ian")
#print(ian.name)
print(ian.get_name())
kinuthia=Person("Kinuthia","Mechanic")
test=Person(10)
