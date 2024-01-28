"""Test the module my_library.

my_library.count_has_2 should accept a list of integers and return the number
of them that contain the digit "2".

To run these tests, ensure that both test_python_activity_1.py and your
my_library.py are on your Python path, and run:
```
python test_python_activity_1.py
```
The simplest way to achieve this to execute this command from the directory
containing both files.
"""
import my_library

assert my_library.count_has_2([2, 3, 4]) == 1
assert my_library.count_has_2([22, 32, 42]) == 3
assert my_library.count_has_2([34, 56, 78]) == 0

print("Tests pass!")
