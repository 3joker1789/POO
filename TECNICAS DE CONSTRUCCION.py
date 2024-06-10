print('UNIVERSIDAD ESTATAL AMAZONICA')
print('Ramiro Saritama')
print('Paralelo "B"')
class heroe:
    nombre= 'Default'
    fuerza = 0
    IQ = 0
    vida= 0
    recursos = 0


    def __init__(self,nombre,fuerza,IQ,vida,recursos):
       self.nombre = nombre
       self.fuerza = fuerza
       self.IQ = IQ
       self.vida = vida
       self.recursos = recursos









mi_heroe= heroe('Batman',25,180,100,1000000)
print('El nombre del jugador es',mi_heroe.nombre)
print('La fuerza  del jugador es',mi_heroe.fuerza)
print('El IQ  del jugador es',mi_heroe.IQ)
print('La vida del jugador es',mi_heroe.vida)
print('Los recursos  del jugador es',mi_heroe.recursos)






