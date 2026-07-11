AUTHOR = 'Aedan Hatchell'
SITENAME = 'Aedan'
SITEURL = ""

PATH = "content"

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    (('HOME', '/Aedan/index/html'),
     ('PROJECTS', '/Aedan/category/projects.html'),)
]

# Social widget
SOCIAL = [
    (('GitHub Profile', 'https://github.com'),)
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'simple'

EXTERNAL_CSS = [
    'https://unpkg.com'
]

EXTRA_TEMPLATES_HTML = """
<style>
    html, body {
    background-color: #fbf9f4 !important; /* Soft warm cream linen */
    color: #3c3836 !important;            /* Gentle dark charcoal text */
    font-family: 'Georgia', serif !important;
    }
    h1, h2, h3 {
        color: #3a503e !important;        /* Deep cottage forest green */
        }
        a {
            color: #ad6d4a !important;    /* Warm terracotta mud links */
            text-decoration: underline !important;
        }
        a:hover {
            color: #8f5333 !important;
        }
<style>
"""
