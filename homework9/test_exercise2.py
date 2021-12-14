#!/usr/bin/python3

import exercise2 as ex


class TestEquation:
    def test_incorrectValuse(self):
        assert ex.equation(1, 'hello', 5) is None
    def test_a0(self):
        assert ex.equation(0, 1, -9) == {'x1': 9.0}
    def test_a0_b0(self):
        assert ex.equation(0, 0, 5) is None
    def test_D_above_0(self):
        assert ex.equation(1, 4, 3) == {'x1': -1.0, 'x2': -3.0}
    def test_D_equal_0(self):
        assert ex.equation(1, 2, 1) == {'x1': -1.0}
    def test_D_less_0(self):
        assert ex.equation(1, 3, 2.5) == {'x1': complex(-1.5, 0.5), 'x2': complex(-1.5, -0.5)}