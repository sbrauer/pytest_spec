# pytest_spec
Rspec-like organization for PyTest.

Provides an `it` decorator for generating meaningful names for test functions and methods.

Also provides `describe` and `context` context managers for grouping tests.

See [`test_demo.py`](test_demo.py) for example usage patterns.

Sample run:
```
$ py.test -vv test_demo.py
========================================= test session starts =========================================
platform darwin -- Python 3.4.3 -- py-1.4.30 -- pytest-2.7.2 -- /Users/sbrauer/projects/pytest_spec_env/bin/python3.4
rootdir: /Users/sbrauer/projects/pytest_spec_env/pytest_spec, inifile:
collected 8 items

test_demo.py::test_generates_test_name_dynamically PASSED
test_demo.py::test_Foo_bar_does_this PASSED
test_demo.py::test_Foo_bar_does_that PASSED
test_demo.py::test_Foo_bar_when_such_and_so_blah_blah PASSED
test_demo.py::TestClass::test_does_something_I_wouldnt_do PASSED
test_demo.py::TestClass::test_does_something_else PASSED
test_demo.py::test_even_or_odd_even_input_returns_even PASSED
test_demo.py::test_even_or_odd_odd_input_returns_odd PASSED

====================================== 8 passed in 0.01 seconds =======================================
```
