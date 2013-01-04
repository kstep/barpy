
from barpy.barcode.code_128 import Code128

class GS1128(Code128):

    application_identifier = None

    def __init__(self, data, type, ai):
        self.application_identifier = ai
        super(GS1128, self).__init__(data, type)

    @property
    def data(self):
        return self.FNC1 + self.application_identifier + super(GS1128, self).data

    @data.setter
    def data(self, value):
        super(GS1128, self).__setattr__('data', value)

    @property
    def partial_data(self):
        return self.data

    @property
    def application_identifier_number(self):
        return self.values[self.application_identifier]

    @property
    def application_identifier_encoding(self):
        return self.encodings[self.application_identifier_number()]

    def __str__(self):
        return "({application_identifier}) {partial_data}".format(
                application_identifier=self.application_identifier,
                partial_data=self.partial_data)

