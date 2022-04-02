import markdown
string = """
```python hl_lines="1 3"
# This line is emphasized
# This line isn't
# This line is emphasized
print(3)
```
"""
html_txt = markdown.markdown(string, extensions=[
        'extra',
        'codehilite', 
        'nl2br',
        'tables',
        'admonition',
        'legacy_em',
        'smarty',
        'sane_lists',
])
print(html_txt)