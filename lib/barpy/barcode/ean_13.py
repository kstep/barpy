
from barpy.barcode.base import Barcode1D
import re

class EAN13(Barcode1D):
    LEFT_ENCODINGS_ODD = [
            '0001101', '0011001', '0010011',
            '0111101', '0100011', '0110001',
            '0101111', '0111011', '0110111',
            '0001011'
            ]

    LEFT_ENCODINGS_EVEN = [
            '0100111', '0110011', '0011011',
            '0100001', '0011101', '0111001',
            '0000101', '0010001', '0001001',
            '0010111'
            ]

    RIGHT_ENCODINGS = [
            '1110010', '1100110', '1101100',
            '1000010', '1011100', '1001110',
            '1010000', '1000100', '1001000',
            '1110100'
            ]

    #Describes whether the left-hand encoding should use
    #LEFT_ENCODINGS_ODD or LEFT_ENCODINGS_EVEN, based on the
    #first digit in the number system  (and the barcode as a whole)
    LEFT_PARITY_MAPS = [
            ['odd', 'odd', 'odd', 'odd', 'odd', 'odd'],   #UPC-A
            ['odd', 'odd', 'even', 'odd', 'even', 'even'],
            ['odd', 'odd', 'even', 'even', 'odd', 'even'],
            ['odd', 'odd', 'even', 'even', 'even', 'odd'],
            ['odd', 'even', 'odd', 'odd', 'even', 'even'],
            ['odd', 'even', 'even', 'odd', 'odd', 'even'],
            ['odd', 'even', 'even', 'even', 'odd', 'odd'],
            ['odd', 'even', 'odd', 'even', 'odd', 'even'],
            ['odd', 'even', 'odd', 'even', 'even', 'odd'],
            ['odd', 'even', 'even', 'odd', 'even', 'odd']
            ]

    #These are the lines that "stick down" in the graphical representation
    START = '101'
    CENTER = '01010'
    STOP = '101'

    #EAN-13 barcodes have 12 digits + check digit
    FORMAT = re.compile(r'^\d{12}$')

    data = None

    def __init__(self, data):
        self.data = data
        if not self.is_valid:
            raise ValueError("data not valid")

    @property
    def characters(self):
        return self.data

    @property
    def numbers(self):
        return map(int, self.data)

    @property
    def odd_and_even_numbers(self):
        odds = []
        evens = []
        is_odd = True

        for n in self.numbers:
            if is_odd:
                odds.append(n)
            else:
                evens.append(n)
            is_odd = not is_odd

        return odds, evens

    @property
    def left_numbers(self):
        return self.numbers[1:7]

    @property
    def right_numbers(self):
        return self.numbers_with_checksum[7:13]

    @property
    def numbers_with_checksum(self):
        return self.numbers + [self.checksum]

    @property
    def data_with_checksum(self):
        return self.data + str(self.checksum)

    @property
    def left_encodings(self):
        from itertools import starmap
        return list(
            starmap(lambda parity, number: self.LEFT_ENCODINGS_ODD[number] if parity == 'odd' else
                self.LEFT_ENCODINGS_EVEN[number],
                zip(self.left_parity_map, self.left_numbers)))

    @property
    def right_encodings(self):
        return map(lambda n: self.RIGHT_ENCODINGS[n], self.right_numbers)

    @property
    def left_encoding(self):
        return "".join(self.left_encodings)

    @property
    def right_encoding(self):
        return "".join(self.right_encodings)

    def encoding(self):
        return (self.start_encoding + self.left_encoding + self.center_encoding +
                self.right_encoding + self.stop_encoding)

    @property
    def left_parity_map(self):
        return self.LEFT_PARITY_MAPS[self.numbers[0]]

    @property
    def weighted_sum(self):
        odds, evens = self.odd_and_even_numbers
        odds = map(lambda n: n * 3, odds)
        return sum(odds + evens)

    @property
    def checksum(self):
        mod = self.weighted_sum % 10
        return 0 if mod == 0 else 10 - mod

    @property
    def checksum_encoding(self):
        return self.RIGHT_ENCODINGS[self.checksum]

    @property
    def is_valid(self):
        return bool(self.FORMAT.match(self.data))

    def __str__(self):
        return self.data_with_checksum

    @property
    def is_upc(self):
        return self.numbers[0] == 0

    @property
    def start_encoding(self):
        return self.START

    @property
    def center_encoding(self):
        return self.CENTER

    @property
    def stop_encoding(self):
        return self.STOP


class UPCA(EAN13):
    pass

    #def data
      #'0' + super
    #end
