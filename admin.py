from bottle import static_file, route, run
# Aqui traemos diferentes cosas de bottle, como static_file, route y run
from settings import STATIC_FILES, BD
# Y traemos la constante "STATIC_FILES" del archivo de configuracion
from sql import Sql
# Ahora nos vamos a traer la clase SQL del archivo "sql.py"


@route('/static/<filename:path>')
def server_static(filename):
    archivo= static_file(filename, root=STATIC_FILES)
    return archivo

@route('/')
def home():
    bdatos = Sql(BD)
    return 'Hola Mundo'

run(host='localhost', port=8000,debug=True,reloader=True)