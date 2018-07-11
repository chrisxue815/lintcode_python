import unittest
import utils


# O(nm) time. O(nm) space. DP.
class Solution(object):
    def backPack(self, m, a):
        """
        @param m: An integer m denotes the size of a backpack
        @param a: Given n items with size a[i]
        @return: The maximum size
        """
        # dp[i][j]: max size for a[0:i] items and backpack size j
        dp = [[0] * (m + 1) for _ in xrange(len(a) + 1)]

        for i in xrange(1, len(a) + 1):
            item_size = a[i - 1]
            for pack_size in xrange(m + 1):
                if pack_size < item_size:
                    dp[i][pack_size] = dp[i - 1][pack_size]
                else:
                    dp[i][pack_size] = max(dp[i - 1][pack_size], dp[i - 1][pack_size - item_size] + item_size)

        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../lintcode_test_cases/p092.json').test_cases

        for case in cases:
            actual = Solution().backPack(case.m, case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
