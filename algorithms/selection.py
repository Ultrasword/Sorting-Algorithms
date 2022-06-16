from ui import algo


NAME = "SelectionSort"

class SelectionSort(algo.Algo):
    def __init__(self):
        super().__init__()
        self._min_i = 0
        self._end = 0
    
    def setup(self):
        self.is_sorting = True
        self._min_i = 0
        self._end = len(self.dataset.values) -1
    
    def sort_step(self):
        if self._min_i >= self._end:
            self.is_sorting = False
            self.output_timer()
            return
        # find the lowest val at each iteration
        lowest_index = 0
        lowest_value = 1e9
        for i in range(self._min_i, self._end+1):
            if self.dataset.values[i] < lowest_value:
                lowest_index = i
                lowest_value = self.dataset.values[i]
        self.dataset.swap_values(lowest_index, self._min_i)
        
        # print("Sort Step", self._min_i, lowest_index, lowest_value)
        self._min_i += 1


def setup():
    return SelectionSort()

