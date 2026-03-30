import pytest
from math_own import Math

# Let's add some change 
class TestMath:
    @pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 200, 300)
    ])
    def test_add_2_nums(self,a, b, expected):
        name = Math(a, b)
        assert name.add_2_nums(a, b) == expected
        


'''
    @pytest.mark.parametrize("a, b", [
        ("1", 2),
        (None, 2),      
        ([1], 2),      
        (1, {"b": 2}),  
    ])
    def test_add_2_nums_invalid(self, a, b):
        obj = Math(a, b)
        with pytest.raises(TypeError):
            obj.add_2_nums(a, b)
'''