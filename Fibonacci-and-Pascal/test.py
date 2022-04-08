import unittest
import fibPascal as fp

class TestPrint(unittest.TestCase):

    def test_printNumbers(self):

        # write unittests for the tests below

        self.assertEqual(fp.printNumbers(8),       '1 4 3')
        self.assertEqual(fp.printNumbers(89),      '1 9 28 35 15 1')
        self.assertEqual(fp.printNumbers(610),     '1 13 66 165 210 126 28 1')
        self.assertEqual(fp.printNumbers(10_946),  '1 19 153 680 1820 3003 3003 1716 495 55 1')
        self.assertEqual(fp.printNumbers(317_811), '1 26 300 2024 8855 26334 54264 77520 75582 48620 19448 4368 455 14')

unittest.main()