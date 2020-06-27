def sequence_find_idx(arr, val, sorting=False):
    if len(arr) == 0:
        return None
    if sorting:
        arr = sorted(arr)
    step = 0
    for idx, v in enumerate(arr):
        step += 1
        if v >= val:
            print('({}...{}, {}) return:{} val:{} step:{} [max=min]'.format(arr[:5], arr[-1], val, idx, arr[idx], step)) 
            #print(step)
            return idx
    return 0


def dichotomy_find_idx(arr, val, sorting=False):
    if len(arr) == 0:
        return None
    if sorting:
        arr = sorted(arr)
    idx_min = 0
    idx_max = len(arr) - 1
    step = 1
    while True:
        if idx_max == idx_min:
            print('({}...{}, {}) return:{} val:{} step:{} [max=min]'.format(arr[:5], arr[-1], val, idx_max, arr[idx_max], step)) 
            return idx_max
        else:
            idx = (idx_max - idx_min) // 2 + idx_min
            if arr[idx] == val:
                print('({}...{}, {}) return:{} val:{} step:{}'.format(arr[:5], arr[-1], val, idx, arr[idx], step))
                return idx
            elif arr[idx] > val:
                idx_max = idx
            else:
                idx_min = idx + 1
        step += 1

def sequence_find_idx_test():
    from datetime import datetime
    assert sequence_find_idx([], 0) is None
    assert sequence_find_idx([5.3], 3) == 0
    assert sequence_find_idx([5.3], 10) == 0
    assert sequence_find_idx([5.3], 5.3) == 0
    assert sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 4.2) == 3
    assert sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 11) == 5
    assert sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 8.3) == 5
    assert sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 0) == 0
    assert sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 20) == 9
    assert sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18], 17.9) == 8
    assert sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18], -10) == 0
    assert sequence_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 5, 25)) == 0
    assert sequence_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 6, 25)) == 2
    assert sequence_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 7, 28)) == 2
    assert sequence_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 6, 26)], datetime(2020, 1, 1)) == 0
    assert sequence_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23, 10, 45), datetime(2020, 6, 26)], datetime(2020, 6, 23)) == 1


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
    # print(sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 11.2))
    # print(sequence_find_idx([1, 1.1, 2.5, 6, 8.2, 11, 12.3, 16.8, 18, 20], 6))
    a = dichotomy_find_idx([datetime(2020, 5, 25), datetime(2020, 6, 23), datetime(2020, 5, 26)], datetime(2020, 5, 25))
    dichotomy_find_idx_test()
    #sequence_find_idx_test()
    print('ok')


if __name__ == '__main__':
    main()
