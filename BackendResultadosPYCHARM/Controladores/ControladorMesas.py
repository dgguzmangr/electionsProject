from Repositorios.RepositorioMesadeVotacion import RepositorioMesadeVotacion
from Modelos.MesadeVotacion import MesadeVotacion

#Clase Controlador Mesas
class ControladorMesas():

    # Metodo Constructor de clase controlador mesas#
    def __init__(self):
        self.RepositorioMesadeVotacion = RepositorioMesadeVotacion()

#Metodo index repositorio mesa de votacion
    def index(self):
        return self.RepositorioMesadeVotacion.findAll()

#Metodo crear repositorio mesa de votacion
    def create(self, laMesadeVotacion):
        nuveaMesadeVotacion = MesadeVotacion(laMesadeVotacion)
        return self.RepositorioMesadeVotacion.save(nuveaMesadeVotacion)

#Metodo buscar por ID
    def show(self,id):
        laMesadeVotacion = MesadeVotacion(self.repositorioMesadeVotacion.findById(id))
        return laMesadeVotacion.__dict__

#Metodo actualizar repositorio Mesa de votacion
    def update(self, id, laMesadeVotacion):
        MesadeVotacionActual = MesadeVotacion(self.repositorioMesadeVotacion.findById(id))
        MesadeVotacionActual.NumerodeMesa = laMesadeVotacion["Número de mesa"]
        MesadeVotacionActual.NumerodeCedulasInscritas = laMesadeVotacion["Número de cédulas inscritas"]
        return self.RepositorioMesadeVotacion.save(MesadeVotacionActual)

#Metodo eliminar por ID repositorio mesa de votacion
    def delete(self, id):
        return self.repositorioMesadeVotacion.delete(id)