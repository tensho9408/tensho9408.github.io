# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MyLearning'
copyright = '2025, tensho'
author = 'tensho'
release = 'y'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# ソースファイルのエンコーディング
source_encoding = "utf-8"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"


html_static_path = ['_static']
# サイドバーに表示するロゴ画像を指定（ファイル名を適切に変更してください）
html_logo = '_static/logo.png'
# ブラウザのタブアイコンにする場合
html_favicon = '_static/favicon.ico'  # favicon.ico を用意する場合
html_css_files = ['css/style.css']