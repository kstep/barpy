
class Barcode(object):
    outputters = {}

    @classmethod
    def register_outputter(cls, name, klass, method_name):
        cls.outputters[name] = (klass, method_name)

    def encoding(self):
        raise NotImplementedError("Every barcode should implement this method")

    @property
    def is_valid(self):
        return False

    @property
    def is_two_dimensional(self):
        return False

    def outputter_for(self, name, *args):
        return self.outputter_class_for(name)(self, *args)

    def outputter_class_for(self, name):
        return self.outputters[name][0]

    def __getattr__(self, name):
        klass, method_name = self.__class__.outputters[name]
        return getattr(klass(self), method_name)

class Barcode1D(Barcode):
    pass

class Barcode2D(Barcode):
    @property
    def is_two_dimensional(self):
        return True

