#!/usr/bin/env python
# encoding: utf-8
from __future__ import (unicode_literals, division,
                        print_function, absolute_import)
from collections import OrderedDict
from flask import request
from app import app

import json
import scraperwiki


@app.route('/')
def index():
    return app.send_static_file('index.html')


# TODO: Do we need to, and how do we make the database read-only?
@app.route('/select')
def sql_select():
    query = request.args.get('q')
    # TODO: Error handling?
    query_result = scraperwiki.sql.select(query)
    return json.dumps(query_result)


@app.route('/meta')
def meta():
    tables_data = scraperwiki.sql.select('name,type FROM sqlite_master '
                                         'WHERE type in ("table", "view")')
    meta_result = {'databaseType': 'sqlite3',
                   'table': {}, }

    for table_data in tables_data:
        table_name = table_data['name']
        # Do we need to clean names or not necessary as no user input?
        column_names = get_column_names(table_name)
        meta_result['table'][table_name] = {'columnNames': column_names,
                                            'type': table_data['type']}
    return json.dumps(meta_result)


def get_column_names(table_name):
    """ Take a table_name and return a list of column names. """
    # TODO: Issues with quotes in names? dumptruck quotes them.
    pragma = scraperwiki.sql.execute(
        ('PRAGMA table_info({0})'.format(table_name)))
    pragma_keys = pragma['keys']
    pragma_rows = pragma['data']
    pragma_data = [OrderedDict(zip(pragma_keys, pragma_row))
                   for pragma_row in pragma_rows]
    return [row['name'] for row in pragma_data]
