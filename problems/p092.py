import unittest
import utils


# O(nm) time. O(m) space. Space-optimized DP.
class Solution(object):
    def backPack(self, m, a):
        """
        @param m: An integer m denotes the size of a backpack
        @param a: Given n items with size a[i]
        @return: The maximum size
        """
        # dp[j]: max size for a[0:i+1] items and backpack size j
        dp = [0] * (m + 1)
        size_sum = sum(a)

        for i in xrange(len(a)):
            item_size = a[i]
            bound = max(item_size, m - size_sum)

            for pack_size in xrange(m, bound - 1, -1):
                dp[pack_size] = max(dp[pack_size], dp[pack_size - item_size] + item_size)

            size_sum - item_size

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../lintcode_test_cases/p092.json').test_cases

        for case in cases:
            actual = Solution().backPack(case.m, case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
