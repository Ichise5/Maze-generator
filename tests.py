import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        x_size = 10
        y_size =10
        m1 = Maze(0, 0, num_rows, num_cols, x_size, y_size)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

        cell_end_end = m1._Maze__cells[num_cols-1][num_rows-1]

        self.assertEqual(
            cell_end_end._Cell__x1,
            x_size*(num_cols-1),
        )
        self.assertEqual(
            cell_end_end._Cell__y1,
            y_size*(num_rows-1),
        )

    def test_maze_create_cells_2(self):
        num_cols = 50
        num_rows = 150
        x_size = 30
        y_size = 10
        m1 = Maze(0, 0, num_rows, num_cols, x_size, y_size)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

        cell_end_end = m1._Maze__cells[num_cols-1][num_rows-1]

        self.assertEqual(
            cell_end_end._Cell__x1,
            x_size*(num_cols-1),
        )
        self.assertEqual(
            cell_end_end._Cell__y1,
            y_size*(num_rows-1),
        )

    def test_maze_create_cells_with_exit(self):
        num_cols = 12
        num_rows = 10
        x_size = 10
        y_size = 15
        m1 = Maze(0, 0, num_rows, num_cols, x_size, y_size)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

        cell_end_end = m1._Maze__cells[num_cols-1][num_rows-1]

        self.assertTrue(
            cell_end_end.has_top_wall,
        )
        self.assertFalse(
            cell_end_end.has_bottom_wall,
        )

    def test_maze_check_cells_visited(self):
        num_cols = 15
        num_rows = 10
        x_size = 10
        y_size = 15
        m1 = Maze(0, 0, num_rows, num_cols, x_size, y_size)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

        cell_end_end = m1._Maze__cells[num_cols-1][num_rows-1]

        self.assertTrue(
            cell_end_end.has_top_wall,
        )
        self.assertFalse(
            cell_end_end.has_bottom_wall,
        )

        m1._Maze__break_walls_r(0,0)

        cells_visited = []
        for row in m1._Maze__cells:
            for cell in row:
                cells_visited.append(cell.visited is True)

        self.assertTrue(
            all(cells_visited)
        )

        m1._Maze__reset_cells_visited()
        cells_reset = []
        for row in m1._Maze__cells:
            for cell in row:
                cells_reset.append(cell.visited is False)

        self.assertTrue(
            all(cells_reset)
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._Maze__cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
                
if __name__ == "__main__":
    unittest.main()
