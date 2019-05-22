# OpenOpenType: Tools for reformatting the OpenType spec

The OpenType font specification is extremely useful for font developers but is not necessarily produced in the most accessible or readable format.

This repository does not contain any of the copyrighted material of the specification itself but consists of scripts to help users view the spec in more convenient formats.

## Make targets

* `fullspec.md` converts the whole spec to Markdown.
* `fullspec.pdf` will produce the whole spec as a 1000+ page PDF file.
* `fullspec.epub` will produce the whole spec as an EPUB file.

You may also work on a file-per-chapter basis, by using `*chapter*.md`, `*chapter*.pdf` and `*chapter*.epub` targets respectively.