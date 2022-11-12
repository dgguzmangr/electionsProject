from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

###################################################################
###########   variables globales y sus importaciones   ############
###################################################################

from Controladores.ControladorMesas import ControladorMesas
miControladorMesa = ControladorMesas()

from Controladores.ControladorConteos import ControladorConteos
miControladorConteo = ControladorConteos()

from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()

from Controladores.ControladorPartidoPolitico import ControladorPartidoPolitico
miControladorPartido = ControladorPartidoPolitico()

###################################################################
###########            probar el servicio              ############
###################################################################
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

###################################################################
########### metodos de controlador de Mesa de Votación ############
###################################################################

#Obtener listado de mesas GET
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

#Metodo crear mesa POST
@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

#Metodo obtener mesa de votacion por ID GET
@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

#Metodo actualizar mesa de votacion PUT
@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

#Metodo eliminar mesa de votacion DELETE
@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)



###################################################################
########### metodos de controlador de Conteos de Votos ############
###################################################################

#Metodo obtener conteo de votos GET
@app.route("/resultados", methods=['GET'])
def getConteos():
    json = miControladorConteo.index()
    return jsonify(json)

#Metodo crear conteos POST
@app.route("/resultados", methods=['POST'])
def crearConteo():
    data = request.get_json()
    json = miControladorConteo.create(data)
    return jsonify(json)

#Metodo actulizar conteos pos ID
@app.route("/resultados/<string:id>", methods=['GET'])
def getConteo(id):
    json = miControladorConteo.show(id)
    return jsonify(json)

#Metodo actualizar conteos PUT
@app.route("/resultados/<string:id>", methods=['PUT'])
def modificarConteo(id):
    data = request.get_json()
    json = miControladorConteo.update(id, data)
    return jsonify(json)

#Metodo eliminar conteo DELETE
@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarConteo(id):
    json = miControladorConteo.delete(id)
    return jsonify(json)

###################################################################
###########    metodos de controlador de Candidato     ############
###################################################################

@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCanditato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

###################################################################
########### metodos de controlador de Partido politico  ###########
###################################################################


#Obtener partidos politicos Metodo GET
@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

#Crear partido politico metodo POST
@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

#Obtener Partido politico por ID metodo GET
@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

#Obtener datos de partido politico y actualizar metodo PUT
@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

#Metodo eliminar partido
@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

###################################################################

###################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
