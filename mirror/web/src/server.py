from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from datetime import datetime
import mysql.connector as mysql
import bjoern
import os

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def add_todolist(req):
  info = req.json_body
  info_list = str(info['f'])
  time = str(datetime.now())
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  sql = """INSERT INTO List (
    todo, created_at)
    VALUES (%s, %s)"""
  val = (info_list, time)
  cursor.execute(sql, val)
  db.commit()

def welcome(req):
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  cursor.execute("SELECT todo FROM List")
  data = cursor.fetchall()
  db.close()
  return render_to_response('templates/main.html', {'todos': data}, request=req)

def add_todo(req):
  return render_to_response('templates/todos.html', [], request=req)

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('add_todo', '/add_todo')
  config.add_view(add_todo, route_name='add_todo')

  config.add_route('add_todolist', '/add_todolist')
  config.add_view(add_todolist, route_name='add_todolist', renderer='json')

  config.add_route('welcome', '/')
  config.add_view(welcome, route_name='welcome')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  bjoern.run(app, "0.0.0.0", 6000)
