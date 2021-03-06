# Simple pandoc filter to handle furigana in markdown when converting to html
# or pdf

# Copyright © 2020 Waldeir
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#!/usr/bin/env python

from pandocfilters import toJSONFilter, RawInline


def behead(key, value, format, meta):
  if format == 'html' and key == 'Link' and value[2][0][0] == '-':
      return RawInline('html',"<ruby>"+ value[1][0]['c'] +"<rp>(</rp><rt>"+value[2][0][1:]+"</rt><rp>)</rp></ruby>")
  elif format == 'latex' and key == 'Link' and value[2][0][0] == '-':
      return RawInline('latex', "\\ruby{" + value[1][0]['c'] + "}{" + value[2][0][1:] + "}")

if __name__ == "__main__":
  toJSONFilter(behead)
