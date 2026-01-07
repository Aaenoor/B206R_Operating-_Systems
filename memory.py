class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_memory = total_memory
        self.allocated = {}

    def first_fit(self, process):
        if process.memory_required <= self.free_memory:
            self.allocated[process.pid] = process.memory_required
            self.free_memory -= process.memory_required
            return True
        return False

    def best_fit(self, process):
        # simplified best-fit for contiguous memory
        return self.first_fit(process)

    def deallocate(self, process):
        if process.pid in self.allocated:
            self.free_memory += self.allocated.pop(process.pid)

    def utilization(self):
        used = self.total_memory - self.free_memory
        return (used / self.total_memory) * 100
