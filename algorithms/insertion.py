from ui import algo

NAME = 'InsertionSort'

class InsertionSort(algo.Algo):
    def __init__(self):
        super().__init__()
        self._end = 0
        self.pointer1 = 0
        self.nextvalue = 1

    def setup(self):
        self.is_sorting = True
        self.pointer1 = 1
        self.nextvalue = 2
        self._end = len(self.dataset.values)
    
    def sort_step(self):
        if self.pointer1 >= self._end:
            self.is_sorting = False
            self.output_timer()
            return
        
        if self.pointer1 <= 0:
            self.pointer1 = 1
        if self.dataset.values[self.pointer1] < self.dataset.values[self.pointer1-1]:
            # swap
            self.nextvalue = max(self.nextvalue, self.pointer1 + 1)
            self.dataset.swap_values(self.pointer1, self.pointer1-1)
            self.pointer1 -= 1
        else:
            self.pointer1 = self.nextvalue
            self.nextvalue += 1
        print(self.pointer1, self.nextvalue)


def setup():
    return InsertionSort()