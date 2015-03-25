#! usr/bin/env python
# encoding=utf-8
import sqlite3
from flask import Flask, request, g, redirect, session,url_for, \
     abort, render_template, flash
from contextlib import closing
from math import ceil

app = Flask(__name__)


conn = sqlite3.connect('example.db',check_same_thread=False)
c = conn.cursor()
c.execute('drop table tasks')
c.execute('create table tasks (id integer primary key autoincrement,task text, time text)')


PER_PAGE=5

@app.route('/',defaults={'page':1})
@app.route('/<int:page>')
def show_tasks(page):
    # cur = c.execute('select id, note, time from notes order by time desc')
    cur = c.execute('select * from tasks')
    # count = len(cur.fetchall())
    # # tasks = get_tasks_for_page(page,PER_PAGE,count)
    tasks = []
    # if page*PER_PAGE<count:
    #     for i in xrange(page):
    #         for j in xrange(PER_PAGE):
    #             cur.fetchone()
    #     for i in xrange(PER_PAGE):
    #         row = cur.fetchone()
    #         tasks.append([dict(id=row[0],task=row[1],time=row[2])])
    # print tasks
    # if not tasks and page!=1:
    #     abort(404)
    count = 0
    for row in cur.fetchall():
        count += 1 
        if count<(page-1)*PER_PAGE:
            continue
        else:
            tasks.append([dict(id=row[0],task=row[1],time=row[2])])
    print tasks
    #tasks = [dict(id=row[0],task=row[1], time=row[2])]
    #tasks = [dict(id=row[0],task=row[1], time=row[2]) for row in cur.fetchall()]
    return render_template('show_tasks.html',tasks=tasks)

@app.route('/add',methods=['GET','POST'])
def add_task():
    c.execute("insert into tasks (task,time) values (?,DATETIME('now'))",
                [request.form['task']])
    conn.commit()
    flash('一条新记录')
    return redirect(url_for('show_tasks'))


@app.route('/delete',methods=['GET','POST'])
def del_task():
    del_id = request.args.get('id', '')
    c.execute("delete from tasks where id = (?)",del_id)
    conn.commit()
    return redirect(url_for('show_tasks'))

@app.route('/search/',methods=['GET','POST'])
def search_task():
    search = request.args.get('search', '')
    c.execute("select * from tasks where task = (?)",[search])
    search_task = [dict(id=row[0],task=row[1], time=row[2]) for row in c.fetchall()]
    return render_template('search_tasks.jade',search_task = search_task)

if __name__=='__main__':
    app.debug = True
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
