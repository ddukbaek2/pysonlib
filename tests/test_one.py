#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
import unittest
import builtins
from pysonlib import PYSONObject


#------------------------------------------------------------------------
# 테스트 케이스.
#------------------------------------------------------------------------
class TestCase(unittest.TestCase):
    def test_Print(self):
        builtins.print("pysonlib-tests")
        pysonObject = PYSONObject()


#------------------------------------------------------------------------
# 파일 진입점.
#------------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()