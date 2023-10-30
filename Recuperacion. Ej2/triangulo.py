from figuras import *
class Triangulo(Figura):

    def dibujar(self, ventana, punto1, punto2):
        
        punto3 = ((punto1[0] + punto2[0]) / 2, (punto1[1] + punto2[1]) / 2)
        
        pygame.draw.polygon(ventana, (0, 255, 0), [punto1, punto2, punto3])