#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import sys
import os
from datetime import datetime
from pathlib import Path
from sphinx.roles import MenuSelection
from sphinxcontrib import spelling
import json
from sphinx_list_items import __version__
#__version__ = '1.0.0'

# -- Document Variables ---------------------------------------------------
docvars = {
    'name': os.getenv('DOCname', 'Sphinx List Items'),
    'subname': os.getenv('DOCsubname', 'User Manual'),
    'pdf': os.getenv('DOCpdf', 'sphinx-list-items_manual'),
    'version': os.getenv('DOCversion', __version__),
    'dir': os.getenv('DOCdir', 'sphinx-list-items'),
    'versions': os.getenv('DOCversions')
}


# -- General configuration ------------------------------------------------
if len(sys.argv) > 2:
    builder = sys.argv[2]
else:
    builder = 'html'

sys.path.insert(0, os.path.abspath('../../sphinx_list_items/'))

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinxcontrib.spelling',
    "sphinx_immaterial.theme_result",
    "sphinx_immaterial.kbd_keys",
    "sphinx_immaterial.apidoc.format_signatures",
    "sphinx_immaterial.apidoc.json.domain",
    "sphinx_immaterial.apidoc.python.apigen",
    "sphinx_immaterial.graphviz",
    'sphinx_list_items'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = f"{docvars['name']} {docvars['subname']}"
copyright = u'%s, JoKneeMo' % str(datetime.today().year)
author = 'JoKneeMo'
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'colorful'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

display_toc = True
numfig = True
autosectionlabel_prefix_document = True

MenuSelection.BULLET_CHARACTER = '\N{RIGHTWARDS ARROW}'


# Common html output setting shared across html and singlhtml(pdf)
html_scaled_image_link = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
htmlhelp_basename = 'docs'
html_static_path = ['_static']
html_title = f"{docvars['name']} v{docvars['version']} {docvars['subname']}"
html_short_title = f"{docvars['name']} v{docvars['version']}"


# -- Options for HTML output ----------------------------------------------
if builder == 'html':
    extensions.append("sphinx_immaterial")
    html_theme = 'sphinx_immaterial'
    html_theme_options = {
        'site_url': 'https://jokneemo.github.io/sphinx-list-items/',
        'repo_url': 'https://github.com/jokneemo/sphinx-list-items/',
        'repo_name': 'Sphinx List Items',
        'icon': {
            'repo': 'fontawesome/brands/github',
            'edit': 'material/file-edit-outline',
        },
        'edit_uri': 'blob/main/doc/content',
        'features': [
            'navigation.expand',
            'toc.integrate',
            'navigation.sections',
            'navigation.top',
            'search.highlight',
            'search.share',
            'toc.follow',
            'toc.sticky',
            'content.tabs.link',
            'announce.dismiss',
        ],
        'palette': [
            {
                'media': '(prefers-color-scheme: light)',
                'scheme': 'default',
                'primary': 'light-green',
                'accent': 'light-blue',
                'toggle': {
                    'icon': 'material/weather-night',
                    'name': 'Switch to dark mode',
                },
            },
            {
                'media': '(prefers-color-scheme: dark)',
                'scheme': 'slate',
                'primary': 'indigo',
                'accent': 'lime',
                'toggle': {
                    'icon': 'material/weather-sunny',
                    'name': 'Switch to light mode',
                },
            },
        ],
        'font': {
            'text': 'Roboto',
            'code': 'Roboto Mono'
        },
        'version_dropdown': False,
        'version_info': [
            {
                'version': 'https://jokneemo.github.io/sphinx-list-items',
                'title': 'HTML',
                'aliases': [],
            },
            {
                'version': f"/sphinx-list-items/_static/{docvars['pdf']}_v{docvars['version']}.pdf",
                'title': 'PDF',
                'aliases': [],
            },
        ],
        'toc_title_is_page_title': True
    }

    sphinx_immaterial_external_resource_cache_dir = '/tmp/html-cache'
    sphinx_immaterial_override_version_directives = False

    html_sidebars = {
        '**': ['globaltoc.html', 'localtoc.html', 'searchbox.html']
    }

    html_css_files = []


# -- Options for PDF output -----------------------------------------------
if builder == 'singlehtml':
    pdf_documents = [('index', u'rst2pdf', u'JoKneeMo', u'sphinx-list-items'), ]
    html_theme = 'business_theme'
    html_context = {
        'docs_scope': 'internal',
        'cover_logo_title': 'JoKneeMo',
        'cover_subtitle': f"{docvars['name']}\n{docvars['subname']}",
        'cover_meta_data': f"Version {docvars['version']}",
    }

    html_css_files = []

    html_sidebars = {
        '**': []
    }

    # Write docvars to file for weasyprint to set pdf file name
    with open('docvars.json', 'w') as f:
        json.dump(docvars, f, indent=4)

# -- Options for Texinfo output -------------------------------------------
texinfo_documents = [
    (master_doc, docvars['pdf'], 'JoKneeMo ' + docvars['name'],
        author, docvars['pdf'], 'Manual','Documentation'),
]
