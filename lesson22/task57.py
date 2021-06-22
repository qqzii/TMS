import unittest


def fn1(ls1, ls2):
    ls = []
    for i in ls1:
        if i in ls2:
            ls.append(i)
    return ls

def fn2(ls1, ls2):
    ls = []
    for i in ls1:
        if i in ls2:
            if i in ls:
                continue
            else:
                ls.append(i)
    return ls

class Tests(unittest.TestCase):
    def test_one(self):
        test1 = fn1([1, 2, 3, 4], [3, 4, 5, 6])
        self.assertTrue(test1 == [3, 4])

    def test_two(self):
        test2 = fn2([1, 2, 3, 4, 4, 5], [3, 4, 5, 5, 5, 6])
        self.assertTrue(test2 == [3, 4, 5])

if __name__ == '__main__':
    unittest.main()