#! usr/bin/env python
# encoding=utf-8
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

app = Flask(__name__)


conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('create table notes (id text, note text, time text)')

@app.route('/')
def show_notes(): 
    cur = c.execute('select id, note, time from notes order by time desc')
    notes = [dict(title=row[0], text=row[1], time=row[2]) for row in cur.fetchall()]
    return render_template('show_notes.html', notes=notes)

@app.route('/add',methods=['GET','POST'])
def add_note():
    c.execute("insert into notes (id,note,time) values (?,?,?)",
                [request.form['id'],request.form['note'],datetime()])
    c.commit()
    flash('一条新记录')
    return redirect(url_for('show_notes'))


if __name__=='__main__':
    app.run()