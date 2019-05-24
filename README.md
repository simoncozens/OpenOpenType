# OpenOpenType: Tools for reformatting the OpenType spec

The OpenType font specification is extremely useful for font developers but is not necessarily produced in the most accessible or readable format.

This repository does not contain any of the copyrighted material of the specification itself but consists of scripts to help users view the spec in more convenient formats.

## Installation

To install the required Python packages:

```
> pip install -r requirements.txt
```

You will also need a copy of [pandoc](https://pandoc.org) installed to convert between document formats; this can normally be installed with your distribution's package manager: `apt-get install pandoc`, `brew install pandoc`, or local equivalent.

## Make targets

After installing the requirement, you can now use `make` to perform the reformatting:

* `fullspec.md` converts the whole spec to Markdown.
* `fullspec.pdf` will produce the whole spec as a 1000+ page PDF file.
* `fullspec.epub` will produce the whole spec as an EPUB file.

You may also work on a file-per-chapter basis, by using `*chapter*.md`, `*chapter*.pdf` and `*chapter*.epub` targets respectively.