import os

version = os.environ.get("DOCS_VERSION", "unknown")
release = version

# project information
author = "Wouter-Michiel Vierdag"
copyright = "2025 Wouter-Michiel Vierdag"


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
    "switcher": {
        "json_url": "https://xarray-contrib.github.io/xarray-dataclass/versions.json",
        "version_match": version,
    },
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "github_url": "https://github.com/xarray-contrib/xarray-dataclass/",
    "twitter_url": "https://x.com/xarray_dev/",
}
