import click
import os
import sqlite3
from flask import current_app, g


#Stellt Verbindung zur Datenbank her
def get_db_con(pragma_foreign_keys = True):
    if 'db_con' not in g:
        g.db_con = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db_con.row_factory = sqlite3.Row
        if pragma_foreign_keys:
            g.db_con.execute('PRAGMA foreign_keys = ON;')
    return g.db_con

#Schließt die DB-Verbindung
def close_db_con(e=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        db_con.close()

#Initialisiert die Datenbank
@click.command('init-db')
def init_db():
    try:
        os.makedirs(current_app.instance_path)
    except OSError:
        pass
    db_con = get_db_con()
    with open(os.path.join(current_app.root_path, 'sql', 'drop_tables.sql'), "r") as f:
        db_con.executescript(f.read())
    with open(os.path.join(current_app.root_path, 'sql', 'create_tables.sql'), "r") as f:
        db_con.executescript(f.read())
    click.echo('Database has been initialized.')

#Daten einfügen
def insert_sample():
    db_con = get_db_con()
    with open(os.path.join(current_app.root_path, 'sql', 'insert_sample.sql'), "r") as f:
         db_con.executescript(f.read())
  

