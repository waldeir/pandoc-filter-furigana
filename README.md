# A pandoc filter to handle furigana in markdown

This pandoc filter written in python will enable pandoc to recognize and format
furigana correctly when converting a markdown text to html.

You must have *pandocfilters* installed for python. 

```bash
pip install pandocfilters
```


# Usage

Write the kanji inside a link structure with its reading aid after a dash
```markdown
[日本語](-にほんご)
```
save the file and run:
```bash
pandoc -F handleFurigana.py myfile.md -o myfile.html
```

The result will be:

![](nihongo.png)

