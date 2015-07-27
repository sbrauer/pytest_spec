from pytest_spec import it, describe, context

@it('generates test name dynamically')
def spec():
    assert True

with describe('Foo bar'):
    @it('does this')
    def spec():
        assert True

    with context('barney'):
        @it('blah blah')
        def spec():
            assert True

    @it('does that')
    def spec():
        assert True


@it('does something else')
def spec():
    assert True

class TestClass:
    def setup(self):
        self.foo = 'Hello'

    @it("does something I wouldn't do!")
    def spec(self):
        assert self.foo == 'Hello'

    @it("does something else")
    def spec(self):
        assert type(self.foo) is str

class TestAnotherClass:
    def setup(self):
        self.foo = 'Hello'

    with describe('Apples'):
        @it("seems alright, don't ya think?")
        def spec(self):
            assert self.foo == 'Hello'

    with describe('Bananas'):
        @it("seems alright, don't ya think?")
        def spec(self):
            assert self.foo == 'Hello'
