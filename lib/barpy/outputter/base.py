from barpy.barcode.base import Barcode

from contextlib import contextmanager

class Outputter(object):

    def __init__(self, barcode):
        self.barcode = barcode

    @classmethod
    def register(cls, *method_names, **methods):
        for name, method_name in methods.iteritems():
            Barcode.register_outputter(name, cls, method_name)

        for name in method_names:
            Barcode.register_outputter(name, cls, name)

    @property
    def is_two_dimensional(self):
        return self.barcode.is_two_dimensional

    def booleans(self, reload=False):
        if self.is_two_dimensional:
            return map(lambda l: map(lambda c: c == "1", l), self.encoding(reload))

        else:
            return map(lambda c: c == "1", self.encoding(reload))

    __encoding = None
    def encoding(self, reload=False):
        if reload or not self.__encoding:
            self.__encoding = self.barcode.encoding()
        return self.__encoding

    def boolean_groups(self, reload=False):
        from itertools import groupby

        if self.is_two_dimensional:
            return map(
                lambda line: map(
                    lambda group: (group[0], len(list(group[1]))),
                    groupby(line, lambda c: c == "1")),
                self.encoding(reload))
        else:
            return map(lambda group: (group[0], len(list(group[1]))),
                    groupby(self.encoding(reload), lambda c: c == "1"))

    @contextmanager
    def options(self, **options):
        original_options = {}

        for k, v in options.iteritems():
            original_options[k] = getattr(self, k)
            setattr(self, k, v)

        try:
            yield

        finally:
            for k, v in original_options.iteritems():
                setattr(self, k, v)

