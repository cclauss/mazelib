
import unittest
from mazelib.generate.Prims import Prims
from mazelib.solve.WallFollower import WallFollower
from mazelib.mazelib import Maze


class MazeTest(unittest.TestCase):
    
    def _on_edge(self, grid, cell):
        """test helper method to determine if a point
        is on the edge of a maze"""
        r,c = cell
        
        if r == 0 or r == (grid.height - 1):
            return True
        elif c == 0 or c == (grid.width - 1):
            return True
        
        return False

    def testGridSize(self):
        h = 4
        w = 5
        H = 2 * h + 1
        W = 2 * w + 1

        m = Maze()
        m.generator = Prims(h, w)
        m.generate()

        self.assertEqual(m.grid.height, H)
        self.assertEqual(m.grid.width, W)

    def testInnerEntrances(self):
        h = 4
        w = 5

        m = Maze()
        m.generator = Prims(h, w)
        m.generate()
        m.generate_entrances(False, False)

        self.assertFalse(self._on_edge(m.grid, m.start))
        self.assertFalse(self._on_edge(m.grid, m.end))

    def testOuterEntrances(self):
        h = 4
        w = 5

        m = Maze()
        m.generator = Prims(h, w)
        m.generate()
        m.generate_entrances()

        self.assertTrue(self._on_edge(m.grid, m.start))
        self.assertTrue(self._on_edge(m.grid, m.end))

    def testGeneratorWipe(self):
        h = 4
        w = 5

        m = Maze()
        m.generator = Prims(h, w)
        m.generate()
        m.generate_entrances()
        m.generate()

        self.assertTrue(m.start == None)
        self.assertTrue(m.end == None)
        self.assertTrue(m.solutions == None)

    def testMonteCarlo(self):
        h = 4
        w = 5
        H = 2 * h + 1
        W = 2 * w + 1

        m = Maze()
        m.generator = Prims(h, w)
        m.solver = WallFollower()
        m.generate_monte_carlo(3)

        # grid size
        self.assertEqual(m.grid.height, H)
        self.assertEqual(m.grid.width, W)

        # test entrances are outer
        self.assertTrue(self._on_edge(m.grid, m.start))
        self.assertTrue(self._on_edge(m.grid, m.end))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
