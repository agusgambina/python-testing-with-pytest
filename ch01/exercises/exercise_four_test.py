"""Exercise four."""

from collections import namedtuple

def test_one():
  """Passing test."""
  assert (1, 2, 3) == (1, 2, 3)

# def test_two():
#   """Failing test."""
#   assert (1, 2, 3) == (3, 2, 1)

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
  """Using no parameters should invoke defaults."""
  t1 = Task()
  t2 = Task(None, None, False, None)
  assert t1 == t2

def test_member_access():
  """Check .field functionality of namedtuple."""
  t = Task('buy milk', 'brian')
  assert t.summary == 'buy milk'
  assert t.owner == 'brian'
  assert (t.done, t.id) == (False, None)

def test_asdict():
  """asdict() should return a dictonary."""
  t_task = Task('do something', 'agus', False, 1)
  t_dict = t_task._asdict()
  t_expected = {
    'summary': 'do something',
    'owner': 'agus',
    'done': False,
    'id': 1
  }
  assert t_dict == t_expected

def test_replace():
  """replace should change passed in fields."""
  t_before = Task('do something', 'agus', False)
  t_after = t_before._replace(id = 10, done = True)
  t_expected = Task('do something', 'agus', True, 10)
  assert t_after == t_expected