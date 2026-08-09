print("one-to-many relationship using composition")
class CPU:
    def __init__(self,cpu_type):
        self.cpu_type=cpu_type
    
class Computer:
    def __init__(self,cpu_type):
        self.CPU=CPU(cpu_type)

singe_core=Computer("single-core")
print(singe_core.CPU.cpu_type)
dual_core=Computer("dual-core")
quad_core=CPU("quad-core")
print(quad_core.cpu_type)