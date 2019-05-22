CHAPTERS := $(shell perl listchapters.pl)

fullspec-a4.pdf: fullspec.md
	pandoc --pdf-engine=xelatex --template=template.tex -o fullspec-a4.pdf fullspec.md

server: $(CHAPTERS)
	jekyll serve

fullspec.md: $(CHAPTERS) opentype.yaml
	cat opentype.yaml $(CHAPTERS) > fullspec.md

$(CHAPTERS):
	python convert.py

clean:
	rm -f $(CHAPTERS)

%.pdf: %.md
	pandoc --pdf-engine=xelatex -o $@ $<