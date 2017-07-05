SCSS=scss --sourcemap=none

all:
	$(SCSS) --update static:static

watch:
	$(SCSS) --watch static:static

clean:
	find static/ -name '*.css' -exec $(RM) {} +
	$(RM) -r ./static/.sass-cache
	$(RM) -r ./.sass-cache

.PHONY: all watch clean
