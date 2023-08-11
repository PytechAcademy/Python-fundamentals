def calculate_total_price(items):
    total = 0
    for item in items:
        total += item['price']
    return total

def test_calculate_total_price():
    items = [{'name': 'apple', 'price': 1}, {'name': 'banana', 'price': 2}]
    result = calculate_total_price(items)
    assert result == 3

if __name__ == '__main__':
    test_calculate_total_price()