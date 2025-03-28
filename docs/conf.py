# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'openMINDS'
copyright = '2023, open Metadata Initiative'
author = 'Zehl'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_code_tabs',
    'sphinx_togglebutton'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

html_logo = "_static/openMINDS-logos/openMINDS_logo_dark.png"

html_show_sphinx = False

html_theme_options = {
  'display_version': False,
  'logo_only': True,
  'includehidden': True,
  'titles_only': True
}

togglebutton_hint = "show more"
togglebutton_hint_hide = "show less"

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'custom.css',
]

html_js_files = [
    'custom.js'
]

