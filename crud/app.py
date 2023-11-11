'''
*Nombre: Monserrat Orduña Basaldua
*Descripcion: CRUD
*Fecha:10/11/2023
'''

# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST


import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('nombre')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM peliculas')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))


@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO peliculas(nombre,duracion ) VALUES(?,?)'
    cursor.execute(insert, [record['nombre'], record['duracion']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()  
    delete = 'DELETE FROM peliculas WHERE nombre= ?'
    cursor.execute(delete, [record['nombre']])
    conn.commit()
    conn.close()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE peliculas SET duracion= ? WHERE nombre= ?'
    cursor.execute(delete, [record['duracion'], record['nombre']])
    conn.commit()
    conn.close()
    return jsonify(record)
app.run(debug=True)