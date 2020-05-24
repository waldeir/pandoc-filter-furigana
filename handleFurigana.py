#!/usr/bin/env python

from pandocfilters import toJSONFilter, RawInline

# simple pandoc filter to handle furigana in markdown to html conversion

def behead(key, value, format, meta):
  if format == 'html' and key == 'Link' and value[2][0][0] == '-':
    return RawInline('html',"<ruby>"+ value[1][0]['c'] +"<rp>(</rp><rt>"+value[2][0][1:]+"</rt><rp>)</rp></ruby>")

if __name__ == "__main__":
  toJSONFilter(behead)
