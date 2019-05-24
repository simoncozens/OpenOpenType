CHAPTERS := $(shell perl listchapters.pl)

all: fullspec.pdf fullspec.epub

server: $(CHAPTERS) _data/navigation.yml
	bundle exec jekyll serve

fullspec.md: $(CHAPTERS) opentype.yaml
	cat opentype.yaml $(CHAPTERS) > fullspec.md

$(CHAPTERS):
	python convert.py

_data/navigation.yml: chapters.md
	perl create-sidebar.pl

clean:
	rm -f $(CHAPTERS)

%.pdf: %.md
	pandoc --template=template.tex --pdf-engine=xelatex -o $@ $<

%.epub: %.md
	pandoc -o $@ $<
