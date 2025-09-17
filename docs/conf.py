from datetime import datetime

# Get current year for copyright
current_year = datetime.now().year

# project information
project = "xarray-dataclass"
author = "Wouter-Michiel Vierdag"
copyright = f"{current_year} Wouter-Michiel Vierdag"


# general configuration
add_module_names = False
autodoc_typehints = "both"
autodoc_typehints_format = "short"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
myst_heading_anchors = 3
templates_path = ["_templates"]


# options for HTML output
html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "logo": {
        "image_light": "logo-light.svg",
        "image_dark": "logo-dark.svg",
    },
    "github_url": "https://github.com/xarray-contrib/xarray-dataclass/",
    "twitter_url": "https://x.com/xarray_dev/",
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/xarray-dataclass/",
            "icon": "fa-solid fa-box",
        },
    ],
    "external_links": [
        {"name": "xarray", "url": "https://xarray.pydata.org/"},
    ],
}
