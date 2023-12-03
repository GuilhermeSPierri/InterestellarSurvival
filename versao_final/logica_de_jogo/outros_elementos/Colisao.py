class Colisao:
    def __init__(self):
        pass
  
    def check(self, objeto1, objeto2):
        if objeto1.colliderect(objeto2):
            return True
        else:
            return False