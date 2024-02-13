import os
from .test_results import test_case

class run_test():

    def __init__(self,kind: str):
        if kind == 'simple_run':
            self.num_cases = 2
        elif kind == 'complete_run':
            self.num_cases = 10

    def test(self,func):
        for test in range(self.num_cases):
            self.read_file(test+1)
            res = func(self.K, self.N, self.Arr)
            test_case.result(value=res,case=f'test_0{test+1}')

    def read_file(self,file:int):
        path = os.getcwd() + '\Case_Test'
        with open(f'{path}\\test_0{file}.txt','r') as f:
            lines = f.readlines()
        self.K = int(lines[0].replace('\n',''))
        self.N = int(lines[1].replace('\n',''))
        self.Arr = list(map(int,lines[2].split(' ')))
