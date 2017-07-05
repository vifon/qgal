all:
	find static/ -name '*.scss' | while read REPLY; do echo "$${REPLY%%.scss}.css"; done | xargs make

clean:
	find static/ -name '*.css' -exec $(RM) {} +

.SUFFIXES: .css .scss
%.css: %.scss
	scss "$<" > "$@"
