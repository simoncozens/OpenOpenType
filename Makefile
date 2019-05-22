CHAPTERS := $(shell perl listchapters.pl)

all: fullspec.pdf fullspec.epub

# server: $(CHAPTERS)
# 	jekyll serve

fullspec.md: $(CHAPTERS) opentype.yaml
	cat opentype.yaml $(CHAPTERS) > fullspec.md

$(CHAPTERS):
	python convert.py

clean:
	rm -f $(CHAPTERS)

%.pdf: %.md
	pandoc --template=template.tex --pdf-engine=xelatex -o $@ $<

%.epub: %.md
	pandoc -o $@ $<
