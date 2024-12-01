import sys
import unittest
# 需要
# from vector.vector import Vector

# 这个一般是放在其他模块
class Vector:
    def __init__(self, x, y):
        if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            self.x = x
            self.y = y
        else:
            raise ValueError("not a number")

    def add(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def mul(self, factor):
        return Vector(self.x * factor,
                      self.y * factor)

    def dot(self, other):
        return self.x * other.x + \
               self.y * other.y

    def norm(self):
        return (self.x * self.x +
                self.y * self.y) ** 0.5

# 模块必须为test_开头
# 类一般为Test开头
class TestVector(unittest.TestCase):

    # # 运行每个测试方法之前执行
    # def setUp(self):
    #     print('start')
    #
    # # 运行每个测试方法之后执行
    # def tearDown(self):
    #     print('end')

    # # 运行每个测试类之前执行
    # @classmethod
    # def setUpClass(cls):
    #     print('start')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('end')

    # 满足条件的才执行
    @unittest.skipIf(sys.version_info < (3, 6), 'requires python3.6')

    # 测试方法必须以test_开头
    def test_init(self):
        v = Vector(1,2)
        self.assertEqual(v.x,1)
        self.assertEqual(v.y,2)

        # 有这个东西的话，就不出错
        with self.assertRaises(ValueError):
            v = Vector('a','b')

    def test_add(self):
        v1 = Vector(1,2)
        v2 = Vector(3,4)
        v3 = v1.add(v2)
        self.assertEqual(v3.x,4)
        self.assertEqual(v3.y,6)

