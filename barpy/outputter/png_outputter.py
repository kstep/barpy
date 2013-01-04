from barpy.outputter.base import Outputter
from PIL import Image

class PngOutputter(Outputter):

    def to_image(self, **opts):
        canvas = None

        with self.options(**opts):
            canvas = Image.new("RGB", (self.full_width, self.full_height), 0xFFFFFF)

            if self.barcode.is_two_dimensional:
                (x, y) = (self.margin, self.margin)
                for line in self.booleans():
                    for bar in line:
                        if bar:
                            canvas.paste(0x000000, (x, y, x + self.xdim, y + self.ydim))
                        x += self.xdim
                    y += self.ydim
                    x = self.margin

            else:
                (x, y) = (self.margin, self.margin)
                for bar in self.booleans():
                    if bar:
                        canvas.paste(0x000000, (x, y, x + self.xdim, y + self.height))
                    x += self.xdim

        return canvas

    def to_datastream(self, constraints=None, **kw):
        constraints = [constraints] if constraints else []
        return self.to_image(**kw).tostring(*constraints)

    def to_png(self, constraints=None, **kw):
        constraints = [constraints] if constraints else []

        from StringIO import StringIO
        strio = StringIO()

        self.to_image(**kw).save(strio, format="png", **kw)
        strio.seek(0)
        return strio.read()

    @property
    def width(self):
        return self.length * self.xdim

    @width.setter
    def width(self, value):
        self.xdim = int(value) / self.length

    __height = 0
    @property
    def height(self):
        return self.ydim * len(self.encoding()) if self.barcode.is_two_dimensional else self.__height or 100

    @height.setter
    def height(self, value):
        self.__height = int(value)

    @property
    def full_width(self):
        return self.width + self.margin * 2

    @property
    def full_height(self):
        return self.height + self.margin * 2

    __xdim = None
    __ydim = None
    __margin = None

    @property
    def xdim(self):
        return self.__xdim or 1

    @property
    def ydim(self):
        return self.__ydim or self.xdim

    @property
    def margin(self):
        return 10 if self.__margin is None else self.__margin

    @xdim.setter
    def xdim(self, value):
        self.__xdim = int(value)

    @ydim.setter
    def ydim(self, value):
        self.__ydim = int(value)

    @margin.setter
    def margin(self, value):
        self.__margin = int(value)

    @property
    def length(self):
        return len(self.encoding()[0]) if self.barcode.is_two_dimensional else len(self.encoding())

    def __len__(self):
        return self.length

PngOutputter.register('to_png', 'to_image', 'to_datastream')


