from pytest_spec import it, describe, context

# Basic usage: a top-level test function.
@it('generates test name dynamically')
def spec():
    assert True

# You can use `describe` to organize related tests.
with describe('Foo bar'):
    @it('does this')
    def spec():
        assert True

    @it('does that')
    def spec():
        assert True

    # `context` is similar to `describe`
    # Note that both can be nested.
    with context('when such and so'):
        @it('blah blah')
        def spec():
            assert True


class TestClass:
    def setup(self):
        self.foo = 'Hello'

    # `it` also works with test methods.
    @it("does something I wouldn't do!")
    def spec(self):
        assert self.foo == 'Hello'

    @it("does something else")
    def spec(self):
        assert type(self.foo) is str

# A slightly more fleshed out example...

# A function to be tested:
def even_or_odd(num):
    if num % 2:
        return 'odd'
    else:
        return 'even'

# Using `as` with `describe` to alias the unit under test.
with describe(even_or_odd) as func:

    with context('even input'):
        @it('returns "even"')
        def spec():
            assert func(4) == 'even'

    with context('odd input'):
        @it('returns "odd"')
        def spec():
            assert func(5) == 'odd'
