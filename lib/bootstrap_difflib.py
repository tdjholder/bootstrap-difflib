import difflib
from utils import FormatDict


_file_template = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
          "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>

<head>
    <meta http-equiv="Content-Type"
          content="text/html; charset=%(charset)s" />
    <title></title>
    <link rel="stylesheet" type="text/css" href="%(bootstrap_source)s">
    <style type="text/css">%(styles)s
    </style>
</head>

<body>
    %(table)s%(legend)s
</body>

</html>"""

_styles = """
        .table td {padding: 0;}
        .table th {padding: 0;} 
        table.diff {font-family:Courier; border:medium;}
        .diff_header {background-color:#e0e0e0}
        td.diff_header {text-align:right}
        .diff_next {background-color:#c0c0c0}
        .diff_add {background-color:#aaffaa}
        .diff_chg {background-color:#ffff77}
        .diff_sub {background-color:#ffaaaa}"""

_table_template = """
    <table class="diff %(bootstrap_table_class)s" id="difflib_chg_%(prefix)s_top"
           cellspacing="0" cellpadding="0" rules="groups" >
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        %(header_row)s
        <tbody>
%(data_rows)s        </tbody>
    </table>"""


class BootstrapHtmlDiff(difflib.HtmlDiff):
    """A simple wrapper for the DiffLib that makes it useful with Bootstrap."""
    _styles = _styles

    def __init__(self, bootstrap_source, bootstrap_table_class="table", *args, **kwargs):
        """
        Behaves exactly as the HtmlDiff class, but requires a Bootstrap source.

        :param bootstrap_source: URL to your bootstrap source.
        :param bootstrap_table_class: Name of the bootstrap class to use, defaults to table.
        :param args: See superclass
        :param kwargs: See superclass
        """
        self._file_template = _file_template % FormatDict(bootstrap_source=bootstrap_source)
        self._table_template = _table_template % FormatDict(bootstrap_table_class=bootstrap_table_class)
        super(BootstrapHtmlDiff, self).__init__(*args, **kwargs)
