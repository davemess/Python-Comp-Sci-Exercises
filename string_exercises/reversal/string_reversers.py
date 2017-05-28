from abc import ABCMeta, abstractmethod, abstractproperty

class StringReverser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def reverse(self, input):
        raise NotImplementedError

class QuickStringReverser(StringReverser):

    def reverse(self, input):
        result = ""
        characters = list(input)
        for c in reversed(characters):
            result += c
        return result
