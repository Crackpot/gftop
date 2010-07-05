#coding=utf8
from pygments import formatters, styles 
mystyles = styles.get_all_styles()

for mystyle in mystyles:
    formatter = formatters.html.HtmlFormatter(style = mystyle)
    outfile = open('pygments_%s.css' % mystyle, 'w')
    outfile.write(formatter.get_style_defs())
    outfile.close()
    print mystyle
