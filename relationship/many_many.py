print("Many-to-many relationship")

#many-to-many relationship without an intermediary class
class Parent:
    all=[]
    def __init__(self,name,children=None):
        self.name=name
        self._children=[]
        if children:
            for child in children:
                self.add_child(child)
        Parent.all.append(self)
    def children(self):
        return self._children
    def add_child(self,child):
        if isinstance(child,Child):
            self._children.append(child)
        else:
            raise ValueError("child must be an instance of the Child class")

class Child:
    def __init__(self,name):
        self.name=name
    def parents(self):
        return [parent for parent in Parent.all if self in parent.children()]
    def add_parent(self,parent):
        if isinstance(parent,Parent):
            parent.add_child(self)
        else:
            raise ValueError("parent must be an instance of the Parent class")

parent1=Parent('Nick')
parent2=Parent("Megan")
child1=Child('Steve')
child2=Child("Liz")

parent1.add_child(child1)
parent2.add_child(child2)

child2.add_parent(parent1)
child2.add_parent(parent2)
for child in parent1.children():
    print(f"child name: {child.name}")

child3=Child("Guido")
child4=Child("Rossum")
parent3=Parent("John",[child3,child4])

for child in parent3.children():
    print(f"Child name is: {child.name}")

child3.add_parent(parent1)
child3.add_parent(parent2)
for parent in child3.parents():
    print(f"For child {child3.name} the parent is: {parent.name}")
