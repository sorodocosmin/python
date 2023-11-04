import unittest
from matrix import Matrix


class MyTestCase(unittest.TestCase):
    def test_ctor_invalid_rows_cols(self):
        # whenever the rows or cols are invalid,
        # the matrix will be created with 1 row and 1 col
        m1 = Matrix(3, 0)
        self.assertEqual(1, m1.get_nr_rows())
        self.assertEqual(1, m1.get_nr_cols())

        m1 = Matrix(-1, -4)
        self.assertEqual(1, m1.get_nr_rows())
        self.assertEqual(1, m1.get_nr_cols())

        m2 = Matrix(2.23, 9)
        self.assertEqual(1, m2.get_nr_rows())
        self.assertEqual(1, m2.get_nr_cols())

        m2 = Matrix("2", 10)
        self.assertEqual(1, m2.get_nr_rows())
        self.assertEqual(1, m2.get_nr_cols())

    def test_ctor_valid_rows_cols(self):
        m1 = Matrix(2, 3)
        self.assertEqual(2, m1.get_nr_rows())
        self.assertEqual(3, m1.get_nr_cols())

        m2 = Matrix(1, 12)
        self.assertEqual(1, m2.get_nr_rows())
        self.assertEqual(12, m2.get_nr_cols())

    def test_set_cell_invalid(self):
        m1 = Matrix(2, 2)
        self.assertIsNone(m1.set_cell(-1, 0, "1"))
        self.assertIsNone(m1.set_cell("0", 1, "1"))

        self.assertTrue(m1.set_cell(0, 0, "1"))

        # try to set a cell with a different type than the other cells
        self.assertFalse(m1.set_cell(0, 1, 2))

    def test_set_get(self):
        m1 = Matrix(2, 2)
        self.assertTrue(m1.set_cell(0, 0, 1))
        self.assertTrue(m1.set_cell(0, 1, 2))
        self.assertTrue(m1.set_cell(1, 0, 3))
        self.assertTrue(m1.set_cell(1, 1, 4))

        self.assertEqual(1, m1.get_cell(0, 0))
        self.assertEqual(2, m1.get_cell(0, 1))
        self.assertEqual(3, m1.get_cell(1, 0))
        self.assertEqual(4, m1.get_cell(1, 1))

        # try to get a cell with invalid row/col
        self.assertEqual(m1.get_cell(0,0), m1.get_cell(23, -3))
        self.assertEqual(m1.get_cell(0,0), m1.get_cell("1", 3.34))

    def test_transpose(self):
        m1 = Matrix(2, 3)
        m1.set_cell(0, 0, 1)
        m1.set_cell(0, 1, 0)
        m1.set_cell(0, 2, 1)
        m1.set_cell(1, 0, 0)
        m1.set_cell(1, 1, 1)
        m1.set_cell(1, 2, 2)

        m1_transpose = m1.transpose()
        self.assertEqual(3, m1_transpose.get_nr_rows())
        self.assertEqual(2, m1_transpose.get_nr_cols())

        expected_res = Matrix(3, 2)
        expected_res.set_cell(0, 0, 1)
        expected_res.set_cell(0, 1, 0)
        expected_res.set_cell(1, 0, 0)
        expected_res.set_cell(1, 1, 1)
        expected_res.set_cell(2, 0, 1)
        expected_res.set_cell(2, 1, 2)

        self.assertEqual(expected_res, m1_transpose)

    def test_multiply(self):
        m1 = Matrix(2, 3)
        m1.set_cell(0, 0, 1)
        m1.set_cell(0, 1, 0)
        m1.set_cell(0, 2, 1)
        m1.set_cell(1, 0, 0)
        m1.set_cell(1, 1, 1)
        m1.set_cell(1, 2, 2)

        m2 = Matrix(3, 2)
        m2.set_cell(0, 0, 3)
        m2.set_cell(0, 1, 5)
        m2.set_cell(1, 0, -1)
        m2.set_cell(1, 1, 0)
        m2.set_cell(2, 0, 2)
        m2.set_cell(2, 1, -1)

        expected_res = Matrix(2, 2)
        expected_res.set_cell(0, 0, 5)
        expected_res.set_cell(0, 1, 4)
        expected_res.set_cell(1, 0, 3)
        expected_res.set_cell(1, 1, -2)

        self.assertEqual(expected_res, m1*m2)

    def test_apply_function(self):
        m1 = Matrix(1, 2)
        m1.set_cell(0, 0, 1)
        m1.set_cell(0, 1, 2)

        m1.apply_function(lambda x: x+1)
        self.assertEqual(2, m1.get_cell(0, 0))
        self.assertEqual(3, m1.get_cell(0, 1))

        # the matrix remains the same bcs the function doesn't return
        # the same type for all the cells
        m1.apply_function(lambda x: "2" if x == 2 else x)
        self.assertEqual(2, m1.get_cell(0, 0))
        self.assertEqual(3, m1.get_cell(0, 1))


if __name__ == '__main__':
    unittest.main()
