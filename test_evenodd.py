from evenodd import even_or_odd

def test_even():
    assert even_or_odd(2) == "Even"

def test_odd():
    assert even_or_odd(3) == "Odd"
