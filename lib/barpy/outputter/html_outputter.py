
from barpy.outputter.base import Outputter

class HtmlOutputter(Outputter):

    class_name = ""

    on_cell = '<td class="barby-cell on"></td>'
    off_cell = '<td class="barby-cell off"></td>'

    css = """
table.barby-barcode { border-spacing: 0; }
tr.barby-row {}
td.barby-cell { width: 3px; height: 3px; }
td.barby-cell.on { background: #000; }
    """

    def to_html(self, **opts):
        with self.options(**opts):
            return self.start + "".join(self.rows) + self.stop

    @property
    def start(self):
        return '<table class="barby-barcode'+(" " + self.class_name if self.class_name else "")+'"><tbody>'

    @property
    def stop(self):
        return '</tbody></table>'

    @property
    def rows(self):
        return self.rows_for(self.booleans() if self.barcode.is_two_dimensional else [self.booleans()])

    def rows_for(self, boolean_groups):
        return map(lambda g: self.row_for(self.cells_for(g)), boolean_groups)

    def row_for(self, cells):
        return "<tr class=\"barby-row\">%s</tr>" % cells

    def cells_for(self, booleans):
        return "".join(map(lambda b: self.on_cell if b else self.off_cell, booleans))

HtmlOutputter.register('to_html')

