#!e:\virtualenvs\envs\env36_01\Scripts\python.exe
import sys, os
#sys.path.insert(1, r'e:\virtualenvs\envs\env36_01\Lib\site-packages')
from hypothesis import given, settings
import hypothesis.strategies as st
import hypothesis.provisional as provisional
import unittest
from method_dichotomy import dichotomy_find_idx, sequence_find_idx

curdir = os.path.abspath(os.path.dirname(__file__))
#os.chdir(curdir)
print(curdir)

class TestDichotomyFind(unittest.TestCase):

    @unittest.skip('test')
    #@settings(database=None)
    @given(st.lists(st.integers()), st.integers())
    def test_dichotomy_find_idx_int(self, arr, val):
        # Тест со значениями массива int, и поисковое значение тоже int
        arr = sorted(arr)
        res = dichotomy_find_idx(arr, val)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            self.assertIsInstance(res, int)
            if res > 0:
                self.assertLessEqual(arr[res-1], val)
            if res < len(arr)-1:
                self.assertGreaterEqual(arr[res+1], val)
            #self.assertGreaterEqual(arr[res], val)

    @unittest.skip('test')
    @given(st.lists(st.floats(allow_nan=False, allow_infinity=False)), st.floats(allow_nan=False, allow_infinity=False))
    def test_dichotomy_find_idx_float(self, arr, val):
        # Тест со значениями массива float, и поисковое значение тоже float
        arr = sorted(arr)
        res = dichotomy_find_idx(arr, val)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            if res > 0:
                self.assertLessEqual(arr[res-1], val)
            if res < len(arr)-1:
                self.assertGreaterEqual(arr[res+1], val)

    @unittest.skip('test')
    @given(st.lists(st.datetimes()), st.datetimes())
    def test_dichotomy_find_idx_datetime(self, arr, val):
        # Тест со значениями массива float, и поисковое значение тоже float
        arr = sorted(arr)
        res = dichotomy_find_idx(arr, val, sorting=True)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            if res > 0:
                self.assertLessEqual(arr[res-1], val)
            if res < len(arr)-1:
                self.assertGreaterEqual(arr[res+1], val)

    @unittest.skip('test')
    @given(val=st.datetimes())
    def test_dichotomy_find_idx_datetime(self, val):
        # Тест с подготовленным массивом
        from method_dichotomy_data import wheellog_data
        #arr = [-1, 2, 5, 10, 100, 1020]
        arr = wheellog_data
        res = dichotomy_find_idx(arr, val)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            if res > 0:
                self.assertLessEqual(arr[res-1], val)
            if res < len(arr)-1:
                self.assertGreaterEqual(arr[res+1], val)


class TestSequenceFind(unittest.TestCase):
    @unittest.skip('test')
    @given(st.lists(st.integers()), st.integers())
    def test_sequence_find_idx_integer(self, arr, val):
        arr = sorted(arr)
        res = sequence_find_idx(arr, val)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            if res > 0:
                self.assertLessEqual(arr[res-1], val)
            if res < len(arr)-1:
                self.assertGreaterEqual(arr[res+1], val)

    #@unittest.skip('test')
    @settings(max_examples=10)
    @given(st.lists(st.datetimes()), st.datetimes())
    def test_sequence_find_idx_datetime(self, arr, val):
        arr = sorted(arr)
        res = sequence_find_idx(arr, val)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            if res > 0:
                self.assertLessEqual(arr[res-1], val)
            if res < len(arr)-1:
                self.assertGreaterEqual(arr[res+1], val)

    @unittest.skip('test')
    @given(val=st.datetimes())
    def test_sequence_find_idx_datetime_wheellog(self, val):
        # Тест с подготовленным массивом
        from method_dichotomy_data import wheellog_data
        #arr = [-1, 2, 5, 10, 100, 1020]
        arr = wheellog_data
        res = sequence_find_idx(arr, val)
        if arr is None or arr == []:
            self.assertIsNone(res)
        else:
            self.assertGreaterEqual(res, 0)
            if res > 0:
                self.assertLessEqual(arr[res-1], val)
            if res < len(arr)-1:
                self.assertGreaterEqual(arr[res+1], val)


def my(val):
    print(val)
    
class TestMy(unittest.TestCase):
    import string
    @unittest.skip('test')
    #@given(st.from_regex('^myregexp \S{2,3}$'))
    @settings(max_examples=100)
    @given(st.text(min_size=3, max_size=100, alphabet=string.ascii_letters))
    def test_strings(self, val):
        res = my(val)

    @unittest.skip('test')
    #@given(provisional.domains())
    @given(provisional.urls())
    def test_urls(self, val):
        print(val)
        res = ''



if __name__ == '__main__':
    unittest.main()
    #input()
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