from barpy.barcode.base import Barcode2D
from qrcode import QRCode

class QrCode(Barcode2D):
    SIZES = [
      [0, 0, 0, 0],

            #L   M   Q   H
      [17, 14, 11, 7],          [32, 26, 20, 14],
      [53, 42, 32, 24],         [78, 62, 46, 34],
      [106, 84, 60, 44],        [134, 106, 74, 58],
      [154, 122, 86, 64],       [192, 152, 108, 84],
      [230, 180, 130, 98],      [271, 213, 151, 119],
      [321, 251, 177, 137],     [367, 287, 203, 155],
      [425, 331, 241, 177],     [458, 362, 258, 194],
      [520, 412, 292, 220],     [586, 450, 322, 250],
      [644, 504, 364, 280],     [718, 560, 394, 310],
      [792, 624, 442, 338],     [858, 666, 482, 382],
      [929, 711, 509, 403],     [1003, 779, 565, 439],
      [1091, 857, 611, 461],    [1171, 911, 661, 511],
      [1273, 997, 715, 535],    [1367, 1059, 751, 593],
      [1465, 1125, 805, 625],   [1528, 1190, 868, 658],
      [1628, 1264, 908, 698],   [1732, 1370, 982, 742],
      [1840, 1452, 1030, 790],  [1952, 1538, 1112, 842],
      [2068, 1628, 1168, 898],  [2188, 1722, 1228, 958],
      [2303, 1809, 1283, 983],  [2431, 1911, 1351, 1051],
      [2563, 1989, 1423, 1093], [2699, 2099, 1499, 1139],
      [2809, 2213, 1579, 1219], [2953, 2331, 1663, 1273]
    ]

    LEVELS = {'l': 0, 'm': 1, 'q': 2, 'h': 3}

    data = None

    def __init__(self, data, **options):
        self.data = data
        for k, v in options.iteritems():
            setattr(self, k, v)
        if not self.size:
            raise ValueError("data too large")

    def encoding(self):
        return map(lambda r: reduce(lambda s, m: s + ("1" if m else "0"), r, ""), self.qrcode.modules)

    __level = None
    @property
    def level(self):
        return self.__level or 'l'

    @level.setter
    def level(self, value):
        self.__level = value

    __size = 0
    @property
    def size(self):
        if self.__size:
            return self.__size

        level_index = self.LEVELS[self.level]
        length = len(self.data)
        found_size = None

        for size, max_values in enumerate(self.SIZES):
            if max_values[level_index] >= length:
                found_size = size
                break

        return found_size

    @size.setter
    def size(self, value):
        self.__size = int(value)

    def __str__(self):
        return self.data[0:20]

    @property
    def qrcode(self):
        qrcode = QRCode(error_correction=self.LEVELS[self.level], version=self.size)
        qrcode.add_data(self.data)
        qrcode.make()
        return qrcode

