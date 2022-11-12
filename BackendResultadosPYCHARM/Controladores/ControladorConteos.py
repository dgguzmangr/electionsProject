from Repositorios.RepositorioConteodevotos import RepositorioConteodevotos
from Repositorios.RepositorioMesadeVotacion import RepositorioMesadeVotacion
from Repositorios.RepositorioCandidato import RepositorioCandidato

from Modelos.Conteodevotos import Conteodevotos
from Modelos.MesadeVotacion import MesadeVotacion
from Modelos.Candidato import Candidato


class ControladorConteos():

    # Metodo Constructor de clase controlador Conteos#
    def __init__(self):
        self.repositorioConteodevotos = RepositorioConteodevotos()
        self.repositorioMesadevotacion = RepositorioMesadeVotacion()
        self.repositorioCandidato = RepositorioCandidato()

    # Devuelve todos los conteos #
    def index(self):
        return self.repositorioConteodevotos.findAll()

    # Crea un conteo #
    def create(self,losConteos, id_mesa, id_candidato):
        nuevo_conteo = Conteodevotos(losConteos)
        lamesa = MesadeVotacion(self.repositorioMesadevotacion.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevo_conteo.mesadevotacion = lamesa
        nuevo_conteo.candidato = elCandidato
        return self.repositorioConteodevotos.save(nuevo_conteo)

    # Muestra un conteo por criterio id #
    def show(self,id):
        elConteo = Conteodevotos(self.repositorioConteodevotos.findById(id))
        return elConteo.__dict__

    # Actualiza un conteo#
    def update(self, id, losConteos):
        el_conteo = Conteodevotos(self.repositorioConteodevotos.findById(id))
        el_conteo.Id = losConteos["Id"]
        el_conteo.Numero_de_mesa = losConteos["Numero de mesa"]
        el_conteo.id_Candidato = losConteos["Id Candidato"]
        el_conteo.id_Partido_politico = losConteos["Id Partido Politico"]
        el_conteo.Numero_de_votos = losConteos["Numero de votos"]
        return self.repositorioConteodevotos.save(el_conteo)

    # Borra un conteo #
    def delete(self, id):
        return self.repositorioConteodevotos.delete(id)