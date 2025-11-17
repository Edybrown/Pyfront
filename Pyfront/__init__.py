# pyfront/__init__.py

# ----------------------------------------------------------------------
# Package Configuration
# ----------------------------------------------------------------------
__version__ = "0.1.0"
__author__ = "Eduardo Antonio Ferrera Rodriguez" 
__license__ = "GPLv3"

# ----------------------------------------------------------------------
# Export main classes and functions
# ----------------------------------------------------------------------

# Import utility classes
from .html_doc import HtmlDoc
from .css import CSSRegistry
from .block import Block

from .tags import (
    Div, Section, Article, Header, Footer, Nav, Main, Aside, Button, Form, Ul, Li,
    div, section, article, header, footer, nav, main, aside, button, form, ul, li
)
