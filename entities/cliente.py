from entities.db import get_connection

class Cliente:
    
    def __init__(self,id,nombre,email,asiento,pelicula):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.asiento = asiento
        self.pelicula = pelicula

    def save(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "INSERT INTO clientes (nombre, email, asiento, pelicula) VALUES (%s,%s,%s,%s);"
            cursor.execute(query, (self.nombre, self.email, self.asiento, self.pelicula))
            connection.commit()
            
            self.id = cursor.lastrowid
            self.id = int(self.id)
            return self.id
        except Exception as ex:
            print("No se pudo guardar el registro correctamente: ", ex)
            return 0
        finally:
            cursor.close()
            connection.close()
    
    @classmethod
    def delete(cls, id_cliente):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM clientes WHERE id = %s"
            cursor.execute(query, (id_cliente,))
            connection.commit()
            
            #self.id = cursor.lastrowid
            
        except Exception as ex:
            print("No se pudo guardar el registro correctamente: ", ex)
            return 0
        finally:
            cursor.close()
            connection.close()
    
    @classmethod
    def get_all(cls):
        clientes = []
        
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "SELECT id, nombre, email, asiento, pelicula FROM clientes ORDER BY asiento DESC;"
            cursor.execute(query)
            
            rows = cursor.fetchall()      
                  
            for row in rows:
                cliente = cls(id=row[0], nombre=row[1], email=row[2], asiento=row[3], pelicula=row[4])
                clientes.append(cliente)
            return clientes
        except Exception as ex:
            print("no se pudieron obtener los registros", ex)
        finally:
            cursor.close()
            connection.close()
    
    @classmethod
    def cliente_update(cls,id,nombre,email,asiento,pelicula):
        
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "UPDATE clientes SET nombre = %s, email = %s, asiento = %s, pelicula = %s WHERE id = %s"
            cursor.execute(query, (nombre, email, asiento, pelicula, id))
            connection.commit()
            
        except Exception as ex:
            print("Error al actualizar", ex)
        finally:
            cursor.close()
            connection.close()
            