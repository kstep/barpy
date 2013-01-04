
from barpy.outputter.base import Outputter

class AsciiOutputter(Outputter):

    def to_ascii(self, **opts):
        default_opts = dict(
                height = 10,
                xdim   = 1,
                bar    = "#",
                space  = " ")

        if self.barcode.is_two_dimensional:
            default_opts.update(
                    height = 1,
                    bar    = ' X ',
                    space  = '   ')

        for k, v in default_opts.iteritems():
            if k not in opts:
                opts[k] = v

        def line_to_ascii(booleans):
            return "\n".join(["".join(map(lambda b: opts['bar'] if b else opts['space'], booleans))] * opts['height'])

        if self.barcode.is_two_dimensional:
            return "\n".join(map(line_to_ascii, self.booleans()))

        else:
            return line_to_ascii(self.booleans())

AsciiOutputter.register('to_ascii')

