import os
import sys

# Inject the parent directory into Python's active system path-matrix:
# with '..' telling Python to step up into the repository root:
sys.path.insert(0, os.path.abspath('..'))

# --- Standard Sphinx configurations continue below ---
project = 'Sphinx Sandbox: Code and Docs'
copyright = '2026, Elliria'
author = 'Elliria'

# Provide the location for the theme assets in the resources sub-directory:
templates_path = ['resources/templates']
html_static_path = ['resources/static']
extensions = [
    'sphinx.ext.autodoc',  # The engine that executes the code to grab docstrings
    'sphinx.ext.viewcode', # Adds handy "[source]" links to your compiled site
    'sphinx.ext.githubpages',  # Bypass Jekyll blocking bugs to enable GitHub Pages
]

# Provide the location for the master document:
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
