from find_number import Solution


test_cases = [
        ([2, 687, 980, 1111], 1111, 3),
        ([0], 0, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4),
        ([1, 2, 3, 4, 5, 6], 10, -1)
    ]

def test_find_number_1():
    s = Solution()
    for nums, target, expected in test_cases:
        r = s.search(nums, target)
        assert r == expected, f"FAIL for {test}, expected {expected}, got {r}"



def test_find_number_2():
    s = Solution()
    for test in test_cases:
        r = s.search(test[0], test[1])
        expected = test[2]
        assert r == expected, f"FAIL for {test}, expected {expected}, got {r}"