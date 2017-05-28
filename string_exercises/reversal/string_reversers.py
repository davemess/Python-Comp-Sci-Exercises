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

class ManualStringReverser(StringReverser):

    def reverse(self, input):
        length = len(input)
        if length <= 1:
            return input
        else:
            characters = list(input)

            for i in range(length/2):
                swapIndex = (length - 1) - i
                swap = characters[swapIndex]
                characters[swapIndex] = characters[i]
                characters[i] = swap

            return "".join(characters)


class RecursiveStringReverser(StringReverser):

    def reverse(self, input):
        if len(input) <= 1:
            return input
        else:
            first = input[0]
            remainder = input[1:]
            return self.reverse(remainder) + first
