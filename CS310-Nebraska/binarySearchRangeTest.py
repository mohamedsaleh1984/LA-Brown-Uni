import unittest

from binarySearchRange import binarySearchRange

class BinSearchRangeUnitTest(unittest.TestCase):
    testList = [1,1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,9,9,9]

    # unit test methods must start with "test"
    def test_001(self):
        expected = (0,0)
        actual = binarySearchRange(self.testList,-10,-5)
        self.assertEqual(expected,actual)

    def test_002(self):
        expected = (8,14)
        actual = binarySearchRange(self.testList,2,7)
        self.assertEqual(expected,actual)

    def test_batchTest(self):
        inputs = [(0,7),(9,20),(10,20),(20,30)]
        expected = [(0,14),(15,19),(19,19),(19,19)]
        for i in range(len(inputs)):
            actual = binarySearchRange(self.testList, *inputs[i])
            self.assertEqual(expected[i],actual)

    def test_batchTestDict(self):
        inputToExpected = {
            (-10,-5):(0,0),
            (1,1):(0,8),
            (1,2):(0,9),
        }
        for inputs,expected in inputToExpected.items():
            actual = binarySearchRange(self.testList, *inputs)
            self.assertEqual(expected,actual)

if __name__ == '__main__':
    unittest.main()