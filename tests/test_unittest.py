import unittest
from main import create_folder
from parameterized import parameterized

class TestFunctions(unittest.TestCase):
#тест функции
    @parameterized.expand(
        [('test_api_2',201),
         ('test_api_3',201)]
    )
    def test_create_folder(self,path,result):
        testresult = create_folder(path)
        self.assertEqual(testresult,result)

#если папка на диске уже есть, то тест успешен, т.к. он упадет
#в данном случае ожидается ошибка, т.к. ответ будет 409
    @unittest.expectedFailure
    def test_create_folder(self):
        testresult = create_folder('test_api')
        self.assertEqual(testresult,201)

if __name__=='__main__':
    unittest.main