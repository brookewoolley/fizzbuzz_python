import fizzbuzz

def test_div_by_3():
    assert fizzbuzz.DivisibleBy3(3) == True

def test_div_by_5():
    assert fizzbuzz.DivisibleBy5(5) == True

if __name__ == '__main__':
    unittest.main()
