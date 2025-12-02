from entities.db import get_connection

class Asiento:
    
    def __init__(self,id,pelicula,nombre_cliente,numero,estado):
        self.id = id
        self.pelicula = pelicula
        self.nombre_cliente = nombre_cliente
        self.numero = numero
        self.estado = estado
    
    
    def save(self):
        
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "INSERT INTO asientos (pelicula, nombre_cliente,numero,estado) VALUES (%s,%s,%d,%s);"
            cursor.execute(query, (self.pelicula, self.nombre_cliente, self.numero, self.estado ))
            connection.commit()
            
            self.id = cursor.lastrowid
            return self.id
        except Exception as ex:
            print("No se pudo guardar el registro correctamente")
            return 0
        finally:
            cursor.close()
            connection.close()
    
    
    def delete(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM asientos WHERE id = %d"
            cursor.execute(query, (self.id))
            connection.commit()
            
            return self.id
        except Exception as ex:
            print("El registro no se pudo eliminar correctamente")
            return 0
        finally:
            cursor.close()
            connection.close()