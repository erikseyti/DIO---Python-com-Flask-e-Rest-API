from flask_restful import Resource

listaHabilidades = ['Python','Java',"Flask",'Django']

class Habilidades(Resource):
    def get(self):
        return listaHabilidades
