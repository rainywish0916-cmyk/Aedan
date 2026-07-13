AUTHOR: 'Aedan Hatchell'
SITENAME = 'AEDAN'
SITEURL = 'https://github.io'
RELATIVE_URLS = False

PATH = "content"
TIMEZONE = 'EST'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ('Home', '/'),
    ('Resume', '/resume.html'),
    ('Developer Journal', '/journal-entry-hello.html'),
    ('Portfolio', '/portfolio-tracker.html'),
)

SOCIAL = (
    ('GitHub Profile', 'https://github.com'),
)

DEFAULT_PAGINATION = 10

THEME = 'simple'

EXTRA_TEMPLATES_HTML = """
<style>
    /* Cozy Cottagecore Style Guide */
    html, body {
        background-color: #fbf9f4 !important; /* Soft warm cream background */
        color: #1c1a17 !important;            /* High-contrast deep earth text */
        font-family: 'Georgia', Cambria, serif !important;
        line-height: 1.8 !important;
        max-width: 750px !important;
        margin: 40px auto !important;
        padding: 0 24px !important;
    }
    
    /* Page brand manu links matching titles */
    h1 a, h2 a, h3 a {
        color: #3a503e !important;
        text-decoration: none !important;
    }
    /* Terracotta Core Hyperlinks */
    a, a:visited {
        color: #ad6d4a !important;
        text-decoration: none !important;
        font-weight: bold !important;
    }
    a:hover {
        color: #8f5333 !important;
    }
    
    ul, ol, li {
        color: #55658 !important;  /* Soft, faded muted green font */
    }
    
    li strong {
        color: #1c1a17 !important;
    }
    
    /* Clean listing indents */
    ul { padding-left: 20px !important; }
    li { margin-bottom: 8px !important; }
</style>
"""