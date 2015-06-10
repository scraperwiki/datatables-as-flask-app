#!/usr/bin/env python
# encoding: utf-8
from __future__ import (unicode_literals, division,
                        print_function, absolute_import)
from collections import OrderedDict
from flask import request, Blueprint

import json
import scraperwiki

datatables = Blueprint('datatables', __name__, static_folder='static',
                       static_url_path='/static/datatables')

@datatables.route('/')
def index():
    return datatables.send_static_file('datatables_tool_index.html')
