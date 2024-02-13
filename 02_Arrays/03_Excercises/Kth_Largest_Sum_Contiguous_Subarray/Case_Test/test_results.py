from unittest import TestCase

class test_case(TestCase):

    test = {
        "test_01": 5,
        "test_02": 11,
    }
    
    @classmethod
    def result(self,value: int,case: str):
        a = self().assertEqual(first=value, second=self.test[case])
    
        