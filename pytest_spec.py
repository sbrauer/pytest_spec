import inspect
import re


TEST_PREFIX = 'test_'


# Abuse the decorator syntax to create a dynamically named test function.
def it(text):
    """ Example usage:
    @it('generates function name dynamically')
    def spec():
        assert True

    Note that you still have to define a function for the test, but the name
    doesn't really matter since the `it` decorator will create an alias to
    the function with a name based on the `it` string.
    However you should avoid naming the function "test" or "test_*" or "*_test"
    since those names will be collected by pytest.
    The name could be anything else.
    As a convention I suggest naming it "spec".
    In this example, the generated name will be:
    "test_it_generates_function_name_dynamically".
    Note that the `it` decorator can be used on both test function and methods
    of a test case class.
    """
    def wrap(func):
        namespace = inspect.currentframe().f_back.f_locals
        namespace[_generate_test_name(text)] = func
        return func
    return wrap


def _generate_test_name(text):
    texts = ContextManager.context_texts()
    texts.append(text)
    return TEST_PREFIX + '_'.join([_slugify(t) for t in texts])


def _slugify(text):
    return re.sub(r'\s+', '_', re.sub(r'[^\w\s]', '', text))


class ContextManager:

    _contexts = []

    def __init__(self, obj):
        self.obj = obj
        self.text = getattr(obj, '__name__', obj)

    def __enter__(self):
        ContextManager._contexts.append(self)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        ContextManager._contexts.pop()
        return False

    @classmethod
    def context_texts(cls):
        return [cm.text for cm in cls._contexts]


def describe(text_or_obj):
    """ Example usage:
    You can pass a string:
    with @describe('Some thing'):

    or pass an object, and optionally alias it via `as`:
    with @describe(SomeClass) as klass:
    with @describe(some_function) as func:
    """
    return ContextManager(text_or_obj)


def context(text):
    """ Example usage:
    with @context('valid email'):
    """
    return ContextManager(text)
