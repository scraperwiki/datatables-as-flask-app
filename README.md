# Table view tool in Flask

## What is it?

View SQLite databases in your browser using `datatables`.

Using [`datatables-view-tool`](https://github.com/scraperwiki/datatables-view-tool)
whose licence is in `app/static`.

## How to use?

Either:

* Install the requirements and run using `local_run.py`. By default, you
  can connect via http://127.0.0.1:5000.

or:

* Run in a `docker` container via the Makefile `make run`. By default,
  you can connect via http://0.0.0.0:8000.

Add your own SQLite database named `scraperwiki.sqlite` to the top level of
this repository.
