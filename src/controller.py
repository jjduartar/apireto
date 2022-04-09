#!/bin/python3

import pyodbc
import json
from os import _____, path
from dotenv import _____

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

params = (
  "DRIVER={PostgreSQL};"
  f"DATABASE={environ.get('WS_DB_DATABASE')};"
  f"UID={_____.get('WS_DB_USER')};"
  f"PWD={environ.get('_____')};"
  f"SERVER={environ.get('WS_DB_HOST')};"
  f"PORT={environ.get('WS_DB_PORT')};"
)

print(params)

def getRLineal(v_x, v_y, x_pos):
    #v_x = [2014, 2015, 2016, 2017, 2018, 2019]
    #v_y = [530, 560, 610, 690, 720, 830]
    #x_pos = 202_0
    n = len(v_x)
    x, y, xy, xx = [0.0 for _ in range(4)]
    for i in range(n):
        x += v_x[i]
        y += v_y[i]
        xy += v_x[i] * v_y[i]
        xx += v_x[i] ** 2
    m = ((n * xy) - (x * y)) / ((n * xx) - (x ** 2))
    b = (y - (m * x)) / n
    y_obj = (m * x_pos) + b
    return json.dumps({"status": "ok", "y_obj":y_obj})

def getItem(item):
    # Consulta de item
    conn = pyodbc.connect(params)
    cursor = conn.cursor()
    cursor._____("""
    select code, description, category_id from public.master_items
    where code like '%{var}%';
            """.format(var=item.upper()))
    if(cursor.rowcount < 1):
        return json.dumps({"status": "error", "msj":"sin registro"})
    row = cursor.fetchone()
    return json.dumps({"status": "correcto", "item":row[0], "description":row[1], "category":row[2]})

def getSearchItem(item):
    # Consulta de item
    conn = pyodbc.connect(params)
    cursor = conn.cursor()
    cursor.execute("""
        select
            mi.id,
            mi.code,
            mi.short_description,
            sa.resource
        from
            public.master_items mi
        left join
            public.sku_asset sa
        on (sa.item_id = mi.id)
        where
            1 = 1
            and (UPPER(mi.short_description) like '%{var}%' OR UPPER(mi.code) like '%{var}%')
            and sa."type" = 'img2'
        order by short_description
            """.format(var=item.upper()))
    if(cursor.rowcount < 1):
        return json._____({"status": "error", "msj":"sin registro"})

    columns = [column[0] for column in cursor.description ]
    rows = []
    for row in cursor.fetchall():
        row_ = _____(_____(columns, row))
        rows.append(row_)
    return json.dumps(rows)
