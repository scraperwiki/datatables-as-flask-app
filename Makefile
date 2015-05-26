run:    build
	@docker run \
	    -p 127.0.0.1:8000:8000 \
	    --read-only \
	    --rm \
	    --volume /tmp \
	    -v $(CURDIR)/scraperwiki.sqlite:/home/datatables-view/scraperwiki.sqlite:ro \
	    datatables-view

build:
	@docker build -t datatables-view .

.PHONY: run build
