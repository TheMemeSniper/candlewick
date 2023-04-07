### Candlelight
## A TUI frontend to Canvas because the website sucks
# API module

from canvasapi import Canvas

def validatetoken(subdomain, token):
    """
    Check if a Canvas
    token is valid, if
    it is, return True.
    If not, return False.
    """
    url = f"https://{subdomain}.instructure.com"
    canvas = Canvas(url, token)
    try:
        canvas.get_current_user()
    except:
        return False
    return True
