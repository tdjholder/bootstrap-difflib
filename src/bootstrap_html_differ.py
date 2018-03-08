

import difflib


_file_template = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>

<head>
    <meta http-equiv="Content-Type"Bo
          content="text/html; charset=%(charset)s" />
    <title></title>
    <style type="text/css">%(styles)s
    </style>
</head>

<body>
    %(table)s%(legend)s
</body>

</html>"""

_styles = """
        table.diff {font-family:Courier; border:medium;}
        .diff_header {background-color:#e0e0e0}
        td.diff_header {text-align:right}
        .diff_next {background-color:#c0c0c0}
        .diff_add {background-color:#aaffaa}
        .diff_chg {background-color:#ffff77}
        .diff_sub {background-color:#ffaaaa}"""

_table_template = """
    <table class="table" id="difflib_chg_%(prefix)s_top"
           cellspacing="0" cellpadding="0" rules="groups" >
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        %(header_row)s
        <tbody>
%(data_rows)s        </tbody>
    </table>"""



class BootstrapHtmlDiff(difflib.HtmlDiff):
    _file_template = _file_template
    _styles = _styles
    _table_template = _table_template
    _default_prefix = 0

    def make_file(self, *args, **kwargs):
        return super(BootstrapHtmlDiff, self).make_file(*args, **kwargs)

    def make_table(self, *args, **kwargs):
        kwargs.setdefault('context', True)
        kwargs.setdefault('numlines', 1)
        return super(BootstrapHtmlDiff, self).make_table(*args, **kwargs)


d = BootstrapHtmlDiff()


