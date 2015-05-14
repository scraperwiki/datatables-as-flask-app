# Table view tool in Flask

## What is it?

View SQLite databases in your browser using `datatables`.

Using [`datatables-view-tool`](https://github.com/scraperwiki/datatables-view-tool)
whose licence is the same as the extra code here (see LICENCE).

## How to use?

1. Add your own SQLite database named `scraperwiki.sqlite` to the top level of
   this repository.

2. To view your database in a browser:

   * Install the requirements and run using `local_run.py`. By default, you
     can connect via http://127.0.0.1:5000.

   or:

   * Run in a `docker` container via the Makefile: `make run`. By default,
     you can connect via http://0.0.0.0:8000.
