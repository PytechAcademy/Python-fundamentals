from calculator import add, product
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_product():
    assert product(5,6) == 30
    assert product(-3,5) == -15
    assert product(0, 5) == 0