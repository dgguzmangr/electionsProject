from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartidopolitico import RepositorioPartidopolitico
from Modelos.Candidato import Candidato
from Modelos.Partidopolitico import Partidopolitico

#Metodos CRUD controlador candidato
class ControladorCandidato():

    # Metodo Constructor de clase controlador Candidato#
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartidopol = RepositorioPartidopolitico()

#Metodo index controlador candidato
    def index(self):
        return self.repositorioCandidato.findAll()
#Metodo crear controlador candidatos
    def create(self,losCandidatos):
        nuevo_candidato = Candidato(losCandidatos)
        return self.repositorioCandidato.save(nuevo_candidato)

#Metodo mostrar controlador candidatos
    def show(self,id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
#Metodo actualizar Controlador candidatos
    def update(self, id, losCandidatos):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        elCandidato.Cedula = losCandidatos["Cedula"]
        elCandidato.NoResolucion = losCandidatos["NoResolucion"]
        elCandidato.Nombre = losCandidatos ["Nombre"]
        elCandidato.Apellido = losCandidatos["Apellido"]
        return self.repositorioCandidato.save(elCandidato)

#Metodo eliminar Controlador candidatos
    def delete(self, id):
        return self.repositorioCandidato.delete(id)

    # Asignar un candidato a un partido #
    def asignarCandidato(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partidopolitico(self.repositorioPartidopol.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)
