
from barpy.barcode.base import Barcode1D

def invert(d):
    return dict(map(lambda p: (p[1], p[0]), d.iteritems()))

class Code128(Barcode1D):

    ENCODINGS = {
      0: "11011001100", 1: "11001101100", 2: "11001100110",
      3: "10010011000", 4: "10010001100", 5: "10001001100",
      6: "10011001000", 7: "10011000100", 8: "10001100100",
      9: "11001001000", 10: "11001000100", 11: "11000100100",
      12: "10110011100", 13: "10011011100", 14: "10011001110",
      15: "10111001100", 16: "10011101100", 17: "10011100110",
      18: "11001110010", 19: "11001011100", 20: "11001001110",
      21: "11011100100", 22: "11001110100", 23: "11101101110",
      24: "11101001100", 25: "11100101100", 26: "11100100110",
      27: "11101100100", 28: "11100110100", 29: "11100110010",
      30: "11011011000", 31: "11011000110", 32: "11000110110",
      33: "10100011000", 34: "10001011000", 35: "10001000110",
      36: "10110001000", 37: "10001101000", 38: "10001100010",
      39: "11010001000", 40: "11000101000", 41: "11000100010",
      42: "10110111000", 43: "10110001110", 44: "10001101110",
      45: "10111011000", 46: "10111000110", 47: "10001110110",
      48: "11101110110", 49: "11010001110", 50: "11000101110",
      51: "11011101000", 52: "11011100010", 53: "11011101110",
      54: "11101011000", 55: "11101000110", 56: "11100010110",
      57: "11101101000", 58: "11101100010", 59: "11100011010",
      60: "11101111010", 61: "11001000010", 62: "11110001010",
      63: "10100110000", 64: "10100001100", 65: "10010110000",
      66: "10010000110", 67: "10000101100", 68: "10000100110",
      69: "10110010000", 70: "10110000100", 71: "10011010000",
      72: "10011000010", 73: "10000110100", 74: "10000110010",
      75: "11000010010", 76: "11001010000", 77: "11110111010",
      78: "11000010100", 79: "10001111010", 80: "10100111100",
      81: "10010111100", 82: "10010011110", 83: "10111100100",
      84: "10011110100", 85: "10011110010", 86: "11110100100",
      87: "11110010100", 88: "11110010010", 89: "11011011110",
      90: "11011110110", 91: "11110110110", 92: "10101111000",
      93: "10100011110", 94: "10001011110", 95: "10111101000",
      96: "10111100010", 97: "11110101000", 98: "11110100010",
      99: "10111011110", 100: "10111101110", 101: "11101011110",
      102: "11110101110", 103: "11010000100", 104: "11010010000",
      105: "11010011100"
    }

    VALUES = {
      'A': invert({
        0: " ",      1: "!",        2: "\"",
        3: "#",       4: "$",        5: "%",
        6: "&",       7: "'",        8: "(",
        9: ")",       10: "*",       11: "+",
        12: ",",      13: "-",       14: ".",
        15: "/",      16: "0",       17: "1",
        18: "2",      19: "3",       20: "4",
        21: "5",      22: "6",       23: "7",
        24: "8",      25: "9",       26: ":",
        27: ";",      28: "<",       29: "=",
        30: ">",      31: "?",       32: "@",
        33: "A",      34: "B",       35: "C",
        36: "D",      37: "E",       38: "F",
        39: "G",      40: "H",       41: "I",
        42: "J",      43: "K",       44: "L",
        45: "M",      46: "N",       47: "O",
        48: "P",      49: "Q",       50: "R",
        51: "S",      52: "T",       53: "U",
        54: "V",      55: "W",       56: "X",
        57: "Y",      58: "Z",       59: "[",
        60: "\\",     61: "]",       62: "^",
        63: "_",      64: "\000",    65: "\001",
        66: "\002",   67: "\003",    68: "\004",
        69: "\005",   70: "\006",    71: "\a",
        72: "\b",     73: "\t",      74: "\n",
        75: "\v",     76: "\f",      77: "\r",
        78: "\016",   79: "\017",    80: "\020",
        81: "\021",   82: "\022",    83: "\023",
        84: "\024",   85: "\025",    86: "\026",
        87: "\027",   88: "\030",    89: "\031",
        90: "\032",   91: "\e",      92: "\034",
        93: "\035",   94: "\036",    95: "\037",
        96: "\303",   97: "\302",    98: "SHIFT",
        99: "\307",   100: "\306",   101: "\304",
        102: "\301",  103: "STARTA", 104: "STARTB",
        105: "STARTC"
      }),

      'B': invert({
        0: " ", 1: "!", 2: "\"", 3: "#", 4: "$", 5: "%",
        6: "&", 7: "'", 8: "(", 9: ")", 10: "*", 11: "+",
        12: ",", 13: "-", 14: ".", 15: "/", 16: "0", 17: "1",
        18: "2", 19: "3", 20: "4", 21: "5", 22: "6", 23: "7",
        24: "8", 25: "9", 26: ":", 27: ";", 28: "<", 29: "=",
        30: ">", 31: "?", 32: "@", 33: "A", 34: "B", 35: "C",
        36: "D", 37: "E", 38: "F", 39: "G", 40: "H", 41: "I",
        42: "J", 43: "K", 44: "L", 45: "M", 46: "N", 47: "O",
        48: "P", 49: "Q", 50: "R", 51: "S", 52: "T", 53: "U",
        54: "V", 55: "W", 56: "X", 57: "Y", 58: "Z", 59: "[",
        60: "\\", 61: "]", 62: "^", 63: "_", 64: "`", 65: "a",
        66: "b", 67: "c", 68: "d", 69: "e", 70: "f", 71: "g",
        72: "h", 73: "i", 74: "j", 75: "k", 76: "l", 77: "m",
        78: "n", 79: "o", 80: "p", 81: "q", 82: "r", 83: "s",
        84: "t", 85: "u", 86: "v", 87: "w", 88: "x", 89: "y",
        90: "z", 91: "{", 92: "|", 93: "}", 94: "~", 95: "\177",
        96: "\303", 97: "\302", 98: "SHIFT", 99: "\307", 100: "\304",
        101: "\305", 102: "\301", 103: "STARTA", 104: "STARTB",
        105: "STARTC",
      }),

      'C': invert({
        0: "00", 1: "01", 2: "02", 3: "03", 4: "04", 5: "05",
        6: "06", 7: "07", 8: "08", 9: "09", 10: "10", 11: "11",
        12: "12", 13: "13", 14: "14", 15: "15", 16: "16", 17: "17",
        18: "18", 19: "19", 20: "20", 21: "21", 22: "22", 23: "23",
        24: "24", 25: "25", 26: "26", 27: "27", 28: "28", 29: "29",
        30: "30", 31: "31", 32: "32", 33: "33", 34: "34", 35: "35",
        36: "36", 37: "37", 38: "38", 39: "39", 40: "40", 41: "41",
        42: "42", 43: "43", 44: "44", 45: "45", 46: "46", 47: "47",
        48: "48", 49: "49", 50: "50", 51: "51", 52: "52", 53: "53",
        54: "54", 55: "55", 56: "56", 57: "57", 58: "58", 59: "59",
        60: "60", 61: "61", 62: "62", 63: "63", 64: "64", 65: "65",
        66: "66", 67: "67", 68: "68", 69: "69", 70: "70", 71: "71",
        72: "72", 73: "73", 74: "74", 75: "75", 76: "76", 77: "77",
        78: "78", 79: "79", 80: "80", 81: "81", 82: "82", 83: "83",
        84: "84", 85: "85", 86: "86", 87: "87", 88: "88", 89: "89",
        90: "90", 91: "91", 92: "92", 93: "93", 94: "94", 95: "95",
        96: "96", 97: "97", 98: "98", 99: "99", 100: "\306", 101: "\305",
        102: "\301", 103: "STARTA", 104: "STARTB", 105: "STARTC"
      })
    }

    FNC1 = "\xC1"
    FNC2 = "\xC2"
    FNC3 = "\xC3"
    FNC4 = "\xC4"
    CODEA = "\xC5"
    CODEB = "\xC6"
    CODEC = "\xC7"

    STOP = "11000111010"
    TERMINATE = "11"

    def __init__(self, data, type):
        self.type = type
        self.data = str(data)
        if not self.is_valid:
            raise ValueError("Data not valid")

    __type = None
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        value = value.upper()
        if len(value) != 1 or value not in "ABC":
            raise ValueError("type must be A, B or C")

        self.__type = value

    def __str__(self):
        return self.full_data

    @property
    def full_data(self):
        return self.data + self.full_extra_data

    @property
    def full_data_with_change_codes(self):
        return self.data + self.full_extra_data_with_change_codes

    @property
    def full_extra_data(self):
        if not self.extra:
            return ''
        return self.extra.full_data

    @property
    def full_extra_data_with_change_code(self):
        if not self.extra:
            return ''
        return self.change_code_for(self.extra) + self.extra.full_data_with_change_codes

    __data = None
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        from re import split

        extra = None
        try:
            (value, div, extra) = split("(["+self.CODEA+self.CODEB+self.CODEC+"])", value, 1)
        except ValueError:
            pass
        
        self.__data = value or ""
        if extra:
            self.extra = div + extra

    __extra = None
    @property
    def extra(self):
        return self.__extra

    @extra.setter
    def extra(self, value):
        if not value.startswith((self.CODEA, self.CODEB, self.CODEC)):
            raise ValueError("Extra must begin with \\305, \\306 or \\307")
        (type, data) = (extra[0], extra[1:])
        self.__extra = self.class_for(type)(data)

    @property
    def characters(self):
        chars = self.data

        if self.type == "C":
            result = []
            count = 0
            while count < len(chars):
                if chars[count] in "0123456789":
                    result.append(chars[count] + chars[count+1])
                    count += 2
                else:
                    result.append(chars[count])
                    count += 1

            return result

        else:
            return chars

    def encoding(self):
        return (self.start_encoding + self.data_encoding + self.extra_encoding
                + self.checksum_encoding + self.stop_encoding)

    @property
    def checksum_encoding(self):
        return self.encodings[self.checksum]

    @property
    def data_encoding(self):
        return "".join(map(self.encoding_for, self.characters))

    @property
    def data_encoding_with_extra_encoding(self):
        return self.data_encoding + self.extra_encoding

    @property
    def extra_encoding(self):
        if not self.extra:
            return ""
        return self.change_code_encoding_for(self.extra) + extra.data_encoding + extra.extra_encoding

    @property
    def checksum(self):
        return (self.start_num + sum(
                map(lambda pair: pair[1] * (pair[0] + 1),
                    enumerate(self.numbers + self.extra_numbers)))) % 103

    @property
    def numbers(self):
        return map(lambda char: self.values[char], self.characters)

    @property
    def extra_numbers(self):
        if not self.extra:
            return []
        [self.change_code_number_for(self.extra)] + self.extra.numbers + self.extra.extra_numbers

    @property
    def encodings(self):
        return self.ENCODINGS

    @property
    def stop_encoding(self):
        return self.STOP + self.TERMINATE

    def encoding_for(self, char):
        return self.encodings[self.values[char]]

    def change_code_for_class(self, klass):
        return {Code128A: self.CODEA, Code128B: self.CODEB, Code128C: self.CODEC}[klass]

    def change_code_for(self, barcode):
        return self.change_code_for_class(barcode.__class__)

    def change_code_number_for(self, barcode):
        return self.values[self.change_code_for(barcode)]

    def change_code_encoding_for(self, barcode):
        return self.encodings[self.change_code_number_for(barcode)]

    def class_for(character):
        if character in ('A', self.CODEA):
            return Code128A
        elif character in ('B', self.CODEB):
            return Code128B
        elif character in ('C', self.CODEC):
            return Code128C

    @property
    def is_valid(self):
        return any(self.characters) and all(map(lambda c: c in self.values, self.characters))

    @property
    def values(self):
        return self.VALUES[self.type]

    @property
    def start_num(self):
        return self.values["START%s" % self.type]

    @property
    def start_encoding(self):
        return self.encodings[self.start_num]

class Code128A(Code128):
    def __init__(self, data):
        Code128.__init__(self, data, "A")

class Code128B(Code128):
    def __init__(self, data):
        Code128.__init__(self, data, "B")

class Code128C(Code128):
    def __init__(self, data):
        Code128.__init__(self, data, "C")

