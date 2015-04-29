run:    build
	@docker run \
	    -p 127.0.0.1:8000:8000 \
	    --read-only \
	    --rm \
	    --volume /tmp \
	    datatables-view

build:
	@docker build -t datatables-view .

.PHONY: run build
