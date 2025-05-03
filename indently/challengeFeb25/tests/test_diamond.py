# test diamond.py

import unittest
from challengeFeb25.diamond import create_diamond
from io import StringIO
import sys

#  create_diamond(width): Prints a diamond shape using star characters based on the given width.


class TestCreateDiamond(unittest.TestCase):

    def test_diamond_width_3(self):
        expected_output = " * \n***\n * \n"
        captured_output = StringIO()
        sys.stdout = captured_output
        create_diamond(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_diamond_width_5(self):
        expected_output = "  *  \n *** \n*****\n *** \n  *  \n"
        captured_output = StringIO()
        sys.stdout = captured_output
        create_diamond(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_diamond_width_6(self):
        expected_output = "  **  \n **** \n******\n **** \n  **  \n"
        captured_output = StringIO()
        sys.stdout = captured_output
        create_diamond(6)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_diamond_width_7(self):
        expected_output = (
            "   *   \n  ***  \n ***** \n*******\n ***** \n  ***  \n   *   \n"
        )
        captured_output = StringIO()
        sys.stdout = captured_output
        create_diamond(7)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_invalid_width(self):
        with self.assertRaises(ValueError) as context:
            create_diamond(2)
        self.assertEqual(str(context.exception), "width must be greater than 2")

    def test_invalid_negative_width(self):
        with self.assertRaises(ValueError) as context:
            create_diamond(-1)
        self.assertEqual(str(context.exception), "width must be greater than 2")


if __name__ == "__main__":
    unittest.main()
