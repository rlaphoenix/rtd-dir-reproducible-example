# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'rtd-dir-reproducible-example'
copyright = '2022, rlaphoenix'
author = 'rlaphoenix'

version = "1.0.0"
release = "1.0.0"

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib.images',
]

master_doc = 'index'

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

templates_path = ['_templates']

# -- Options for internationalization ----------------------------------------

language = 'en'

# -- Options for HTML output -------------------------------------------------

html_static_path = ['_static']
