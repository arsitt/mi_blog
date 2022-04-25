from re import TEMPLATE
from bottle import static_file, route, run, jinja2_view, TEMPLATE_PATH
# Aqui traemos diferentes cosas de bottle, como static_file, route y run
from settings import STATIC_FILES, BD, TEMPLATES
# Y traemos la constante "STATIC_FILES" del archivo de configuracion
from sql import Sql
# Ahora nos vamos a traer la clase SQL del archivo "sql.py"


TEMPLATE_PATH.append(TEMPLATES)
# Añadimos nuestra carpeta "templates" al template_path

@route('/static/<filename:path>')
def server_static(filename):
    archivo= static_file(filename, root=STATIC_FILES)
    return archivo

@route('/')
@jinja2_view('./templates/index.html')
def home():
    bdatos = Sql(BD)
    resp = bdatos.select('select * from posts')
    return {'posts' : resp}

@route('/post/<id:int>')
@jinja2_view('post.html')
def ver_post(id):
    bdatos = Sql(BD)
    resp = bdatos.select(f'select * from posts where id={id}')
    return {'post' : resp[0]}

run(host='localhost', port=8000,debug=True,reloader=True)