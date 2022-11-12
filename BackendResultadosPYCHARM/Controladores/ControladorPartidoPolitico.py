from Repositorios.RepositorioPartidopolitico import RepositorioPartidopolitico
from Modelos.Partidopolitico import Partidopolitico

#Definicion de la clase que contiene los metodos CRUD
class ControladorPartidoPolitico():

    def __init__(self):
        self.RepositorioPartidopolitico = RepositorioPartidopolitico()
#Metodo index Controlador partido politico
    def index(self):
        return self.RepositorioPartidopolitico.findAll()
#Metodo crear Controlador partido politico
    def create(self,elPartidoPolitico):
        nuevoPartidopolitico = Partidopolitico(elPartidoPolitico)
        return self.RepositorioPartidopolitico.save(nuevoPartidopolitico)
#Metodo Mostrar por ID Controlador partido politico
    def show(self,id):
        elPartidoPolitico = Partidopolitico(self.RepositorioPartidopolitico.findById(id))
        return elPartidoPolitico.__dict__
#Metodo actualizar partido politico por ID
    def update(self, id, elPartidopolitico):
        PartidoPoliticoActual = Partidopolitico(self.RepositorioPartidopolitico.findById(id))
        PartidoPoliticoActual.nombre = elPartidopolitico["Nombre"]
        PartidoPoliticoActual.lema = elPartidopolitico["Lema"]
        return self.RepositorioPartidopolitico.save(PartidoPoliticoActual)

    # Borra un partido politico #
    def delete(self, id):
        return self.RepositorioPartidopolitico.delete(id)