from bootstrap_difflib.bootstrap_difflib import BootstrapHtmlDiff

print(__name__)
if __name__ == "__main__":
    toLines = ['This project was born out of the idea', 'Of wanting a slightly better', 'Looking Diff Table']
    fromLines = ['This project has been born out of the idea', 'Of wanting a slightly better', 'GUI']

    import os
    import webbrowser

    t = BootstrapHtmlDiff("https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css")
    path = os.path.abspath('temp.html')
    url = 'file://' + path
    html = t.make_file(toLines, fromLines)
    print(html)
    with open(path, 'w') as f:
        f.write(html)
    webbrowser.open(url)

    f.close()