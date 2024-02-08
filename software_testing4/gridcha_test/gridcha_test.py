from software_testing4.grid_cha.grid_cha import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_grid1(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        result = gridChallenge(grid)
        self.assertEqual(result,'YES')