#!e:\virtualenvs\envs\env36_01\Scripts\python.exe
import sys
#sys.path.insert(1, r'e:\virtualenvs\envs\env36_01\Lib\site-packages')
from hypothesis import given
import hypothesis.strategies as st
import unittest
from method_dichotomy import dichotomy_find_idx, sequence_find_idx


class TestDichotomyFind(unittest.TestCase):

    #@unittest.skip('test')
    @given(st.lists(st.integers()), st.integers())
    def test_dichotomy_find_idx_int(self, arr, val):
        # Тест со значениями массива int, и поисковое значение тоже int
        res = dichotomy_find_idx(arr, val, sorting=True)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            #self.assertGreaterEqual(arr[res], val)
            self.assertIsInstance(res, int)
            
    #@unittest.skip('test')
    @given(st.lists(st.floats()), st.floats())
    def test_dichotomy_find_idx_float(self, arr, val):
        # Тест со значениями массива float, и поисковое значение тоже float
        res = dichotomy_find_idx(arr, val, sorting=True)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            self.assertIsInstance(res, int)
            
    #@unittest.skip('test')
    @given(st.lists(st.datetimes()), st.datetimes())
    def test_dichotomy_find_idx_datetime(self, arr, val):
        # Тест со значениями массива float, и поисковое значение тоже float
        res = dichotomy_find_idx(arr, val, sorting=True)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            
    #@unittest.skip('test')
    @given(val=st.datetimes())
    def test_dichotomy_find_idx_datetime(self, val):
        # Тест с подготовленным массивом
        from method_dichotomy_data import wheellog_data
        #arr = [-1, 2, 5, 10, 100, 1020]
        arr = wheellog_data
        res = dichotomy_find_idx(arr, val, sorting=True)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)


class TestSequenceFind(unittest.TestCase):
    #@unittest.skip('test')        
    @given(st.lists(st.integers()), st.integers())
    def test_sequence_find_idx_datetime(self, arr, val):
        res = sequence_find_idx(arr, val, sorting=True)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)



def my(val):
    print(val)
    
class TestMy(unittest.TestCase):
    #@unittest.skip('test')        
    #@given(st.text())
    #def test_my(self, val):
    #    res = my(val)

    @given(st.from_regex('^myregexp \d{2,3}$'))
    def test_my(self, val):
        res = my(val)


    

if __name__ == '__main__':
    unittest.main()

# Запуск из командной строки: python -m unittest method_dichotomy_test.py

"""
def incremental_find_idx(arr, val):
    if len(arr) == 0:
        return None
    step = 0
    for idx, v in enumerate(arr):
        step += 1
        if v >= val:
            print(step)
            return idx
    return 0


def dichotomy_find_idx(arr, val):
    if len(arr) == 0:
        return None
    idx_min = 0
    idx_max = len(arr) - 1
    step = 0
    while True:
        if idx_max == idx_min:
            print(step)
            return idx_max
        else:
            idx = (idx_max - idx_min) // 2 + idx_min
            if arr[idx] == val:
                print(step)
                return idx
            elif arr[idx] > val:
                idx_max = idx
            else:
                idx_min = idx + 1
        step += 1

def incremental_find_idx_test():
    from datetime import datetime
    assert incremental_find_idx([], 0) is None
    assert incremental_find_idx([5.3], 3) == 0
    assert incremental_find_idx([5.3], 10) == 0
    assert incremental_find_idx([5.3], 5.3) == 0
    assert incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 4.2) == 3
    assert incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 11) == 5
    assert incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 8.3) == 5
    assert incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 0) == 0
    assert incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 20) == 9
    assert incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18], 17.9) == 8
    assert incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18], -10) == 0
    assert incremental_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 5, 25)) == 0
    assert incremental_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 6, 25)) == 2
    assert incremental_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 7, 28)) == 2
    assert incremental_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 1, 1)) == 0
    assert incremental_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23, 10, 45), datetime(2020, 6, 26)], datetime(2020, 6, 23)) == 1


def dichotomy_find_idx_test():
    from datetime import datetime
    assert dichotomy_find_idx([], 0) is None
    assert dichotomy_find_idx([5.3], 3) == 0
    assert dichotomy_find_idx([5.3], 10) == 0
    assert dichotomy_find_idx([5.3], 5.3) == 0
    assert dichotomy_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 4.2) == 3
    assert dichotomy_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 11) == 5
    assert dichotomy_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 8.3) == 5
    assert dichotomy_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 0) == 0
    assert dichotomy_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 20) == 9
    assert dichotomy_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18], 17.9) == 8
    assert dichotomy_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18], -10) == 0
    assert dichotomy_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 5, 25)) == 0
    assert dichotomy_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 6, 25)) == 2
    assert dichotomy_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 7, 28)) == 2
    assert dichotomy_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 1, 1)) == 0
    assert dichotomy_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23, 10, 45), datetime(2020, 6, 26)], datetime(2020, 6, 23)) == 1



def main():
    from datetime import datetime
    # print(incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 11.2))
    # print(incremental_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 6))
    #a = dichotomy_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 5, 26)], datetime(2020, 5, 25))
    #dichotomy_find_idx_test()
    #incremental_find_idx_test()
    print('ok')


if __name__ == '__main__':
    main()
"""