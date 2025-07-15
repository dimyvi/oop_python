class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.total_mem_slots = 4

    def get_config(self):
        st = '; '.join([f"{mem.name} - {mem.volume}" for mem in self.mem_slots])
        return [f'Материнская плата: {self.name}',
               f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
               f'Слотов памяти: {self.total_mem_slots}',
               f'Память: {st}']


cpu = CPU("Intel Core i7", 3500)

mem1 = Memory("Kingston DDR4", 8192)
mem2 = Memory("Samsung DDR4", 16384)

mb = MotherBoard("ASUS ROG", cpu, mem1, mem2)
