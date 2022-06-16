import time


class Algo:
    def __init__(self):
        self.dataset = None
        self.is_sorting = False
        
        self.starting_time = 0

    def set_dataset(self, data):
        self.dataset = data

    def sort_step(self):
        print("Sort")
    
    def setup(self):
        pass

    def init_timer(self):
        self.starting_time = time.time()
    
    def output_timer(self):
        print(f"Time Taken: {time.time()-self.starting_time:.2f}")