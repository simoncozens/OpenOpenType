CHAPTERS := $(shell perl listchapters.pl)

fullspec-a4.pdf: $(CHAPTERS)
	pandoc --pdf-engine=xelatex -V title:"The OpenType Standard" -V documentclass:book -o fullspec-a4.pdf fullspec.md

server: $(CHAPTERS)
	jekyll serve

fullspec.md: $(CHAPTERS)
	cat $(CHAPTERS) > fullspec.md

$(CHAPTERS):
	python convert.py

clean:
	rm -f $(CHAPTERS)

%.pdf: %.md
	pandoc --pdf-engine=xelatex -o $@ $<