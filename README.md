[![test workflow](https://github.com/capjamesg/siml/actions/workflows/tests.yml/badge.svg)](https://github.com/capjamesg/siml/actions/workflows/tests.yml)

# Structured Index Markup Language (SIML)

Structured Index Markup Language (SIML) describes a markup language for indices.

SIML is human readable and machine parsable, implementing a syntax based on real-world book indices.

I made this to learn more about parsing with the [Lark](https://github.com/lark-parser/lark) parser.

The utility of this project may be limited, but it was a fun project to work on!

## Installation

```bash
pip install git+https://github.com/capjamesg/siml
```

## Syntax

The following syntaxes are available:

```
# a term with a page number range and sub terms
term, page-page
    subterm, page
    subterm, page

# a term with a single page number
term, page

# a term with a page range
term, page-page

# a term with a see also reference
term, page. See also: term
```

## License

This project is licensed under an [MIT license](LICENSE).