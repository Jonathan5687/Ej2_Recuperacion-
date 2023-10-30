from figuras import * 
class Rectangulo(Figura):

    
    def dibujar(self, ventana, punto1, punto2):
        
        ancho = abs(punto1[0] - punto2[0])
        alto = abs(punto1[1] - punto2[1])

        pygame.draw.rect(ventana, (0, 0, 255), (punto1[0], punto1[1], ancho, alto))