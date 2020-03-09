from models.vector import Vector

class VectorManager: 
    __instance = None

    def __init__(self):
        if VectorManager.__instance == None: 
            VectorManager.__instance = self
            self.vectors = []
        else: 
            raise Exception("Trying to create another instance of a singelton class") 
    
    @staticmethod
    def get_instance(): 
        if VectorManager.__instance == None: 
            VectorManager()
        return VectorManager.__instance

    def add_vector(self, name, desc): 
        v = Vector(name, desc)
        self.vectors.append(v)

    def vector_exists(self, name): 
        for vector in self.vectors: 
            if vector.getName() == name: 
                return True
        return False

    def get_vectors(self): 
        return self.vectors

    def get_vector_by_name(self, name): 
        for vector in self.get_vectors(): 
            if vector.getName() == name: 
                return vector
        return None

    def update_vector(self, vector_name, name, desc): 
        for vector in self.vectors: 
            if vector.getName() == vector_name: 
                vector.setName(name)
                vector.setDesc(desc)

    def delete_vector(self, name):
        if self.vector_exists(name): 
            for vector in self.vectors: 
                if vector.getName() == name: 
                    self.vectors.remove(vector) 
                    del vector