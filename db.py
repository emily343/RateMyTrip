import click
import os
import sqlite3
from flask import current_app, g

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

def close_db_con(e=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        db_con.close()

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

def insert_sample():
    db_con = get_db_con()
    with open(os.path.join(current_app.root_path, 'sql', 'insert_sample.sql'), "r") as f:
         db_con.executescript(f.read())
  

def insert_image_paths():
    db_con = get_db_con()
    updates = [
        ('Copenhagen', 'copenhagen.webp')
    ]
    for name, image in updates:
        db_con.execute("UPDATE city SET image_path = ? WHERE name = ?", (image, name))
    db_con.commit()

def add_image_column():
    db_con = get_db_con()
    try:
        db_con.execute("ALTER TABLE city ADD COLUMN image_path TEXT")
        db_con.commit()
    except sqlite3.OperationalError:
        print("Spalte 'image_path' existiert bereits.")
