from LeetCode.lemonade_change import Solution

bills_dict = {
    True: [5, 5, 5, 10, 20],
    False: [5, 5, 10, 10, 20],
    True: [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5],
    True: [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20],
}


def test_lemonade_change_brute_force():
    for key, value in bills_dict.items():
        brute_force = Solution().lemonadeChange(value)
        assert brute_force == key


def test_lemonade_change_optimal():
    for key, value in bills_dict.items():
        optimal = Solution().lemonade_change(value)
        assert optimal == key


def test_lemonade_change_compare_both():
    for _, value in bills_dict.items():
        optimal = Solution().lemonade_change(value)
        brute_force = Solution().lemonadeChange(value)
        assert optimal == brute_force
