#!/usr/bin/env python

from barpy import GS1128, Code128, Code128A, EAN13, QrCode, HtmlOutputter

code = QrCode("123456789012")

#code = GS1128("01950123456789033103000123", "A", "")
outputter = code.outputter_for("to_png")
#print outputter.booleans()
#print code.is_two_dimensional
#print outputter.to_png(margin=5, height=200, width=200, xdim=2, ydim=2)
print "<html><style>" + HtmlOutputter.css + "</style><body>"
print code.to_html()
print "</body></html>"

