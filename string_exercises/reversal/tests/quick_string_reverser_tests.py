from nose.tools import *
from reversal.string_reversers import *

class AbstractStringReverserTests(object):
    """
    An abstract class for running string reversal tests.
    Subclasses should instantiate a concrete reverser.
    """

    @abstractproperty
    def reverser(self):
        """A concrete instance of a StringReverser."""
        raise NotImplementedError("'AbstractStringReverserTests' subclasses should have a 'reverser' attribute")

    def test_reverses_empty_string(self):
        assert_equal(self.reverser.reverse(''), '')

    def test_reverses_single_character_string(self):
        assert_equal(self.reverser.reverse('A'), 'A')

    def test_reverses_complex_string(self):
        assert_equal(self.reverser.reverse('hello world'), 'dlrow olleh')

class TestsQuickStringReverser(AbstractStringReverserTests):
    """Concrete tests for QuickStringReverser."""

    reverser = QuickStringReverser()
