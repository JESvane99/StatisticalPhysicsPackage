# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import pathlib


sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# sys.path.insert(0,pathlib.Path(__file__).parents[1].resolve().as_posix())


project = "Handbook and guide: Statistical and Solid State Physics"
copyright = "2024, Jonas E. Svane"
author = "Jonas E. Svane"
release = "0.1"

# root_doc = "index"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "autodoc2",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_subfigure",
]

templates_path = ["_templates"]
exclude_patterns = ["../env"]

# include_patterns = ['../md']

# autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

# -- Configuring MyST-parser -------------------------------------------------

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 5

# -- Configuring autodoc2 -----------------------------------------------------

autodoc2_packages = [
    "../SttPhscsPckg",
]

autodoc2_render_plugin = "myst"
