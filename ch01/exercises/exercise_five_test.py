def test_first_assertion():
  assert 1 not in [2, 3, 4]

def test_second_assertion():
  a = 1
  b = 2
  assert a < b

def test_third_assertion():
  assert 'fizz' in 'fizzbuzz'