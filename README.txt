# barpy #

This is Python a port of [barby][] library written in Ruby. I couldn't find
lightweight Python barcode generation library of the same caliber as **barby**
([elaphe][] is broken and others don't support GS1-128 *and* QRCode at the same
time, so I ported **barby**.

[barby]: http://toreto.re/barby/
[elaphe]: http://code.google.com/p/elaphe/

API is basicly the same as of **barby**, but in Python style.

The port is very quick and not complete at the moment (I ported only parts
I really need for my project), I will port the rest eventually.

Also the port is quite direct, in a sense there are a lot of places in Python
code which have more Rubyish flavour instead of Pythonian (e.g. a lot of
`@property` decorators to call methods without parenthesis). I did it to avoid
logic errors during porting process, I will make code more Pythonian in the
future.
