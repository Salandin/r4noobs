# Windmill Dark theme

## About

Windmill Dark theme focuses on clean usable navigation for large documentation
projects. It retains the state of the menu of pages and folders across page
transitions, by keeping navigation to an iframe.

It also implements a versatile search, featuring term highlighting, and both a
quick dropdown and a full-page option that allows the user to come back to
search results.

Within pages, it uses the default mkdocs theme, including syntax highlighting.

## Installation

Install the Windmill Dark theme using `pip`:

``` sh
pip install mkdocs-windmill-dark
```

To install and get started with `mkdocs`, follow [MkDocs documentation](http://www.mkdocs.org/#installation).

## Usage

To use the Windmill Dark theme installed via `pip`, add this to your `mkdocs.yml`:

``` yaml
theme: 'windmill-dark'
```

If you cloned Windmill Dark from GitHub:

``` yaml
theme_dir: 'mkdocs-windmill-dark/mkdocs_windmill_dark'
```

See [Customization](customization.md) for a few extra configuration options
supported by the Windmill Dark theme.
