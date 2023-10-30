from figuras import * 

class Circulo(Figura):

    def dibujar(self, ventana, punto1, punto2):
        
        radio = ((punto1[0] - punto2[0]) * 2 + (punto1[1] - punto2[1]) * 2) ** 0.5
        
        pygame.draw.circle(ventana, (255, 0, 0), punto1, int(radio))