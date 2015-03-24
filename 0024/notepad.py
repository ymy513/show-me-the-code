#! usr/bin/env python
# encoding=utf-8
import sqlite3
from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

app = Flask(__name__)


conn = sqlite3.connect('example.db',check_same_thread=False)
c = conn.cursor()
c.execute('create table tasks (task text, time text, finished bool)')

@app.route('/')
def show_notes(): 
    # cur = c.execute('select id, note, time from notes order by time desc')
    cur = c.execute('select * from tasks')
    notes = [dict(id=row[0], note=row[1], time=row[2]) for row in cur.fetchall()]
    return render_template('show_notes.html', notes=notes)

@app.route('/add',methods=['GET','POST'])
def add_note():
    
    c.execute("insert into notes (id,note,time) values (?,?,DATETIME('now'))",
                [request.form['id'],request.form['note']])
    conn.commit()
    flash('一条新记录')
    return redirect(url_for('show_notes'))


if __name__=='__main__':
    app.debug = True
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()