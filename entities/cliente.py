from entities.db import get_connection

class Cliente:
    
    def __init__(self,id,nombre,email,asiento):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.asiento = asiento

    def save(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "INSERT INTO clientes (nombre, email, asiento) VALUES (%s,%s,%s);"
            cursor.execute(query, (self.nombre, self.email, self.asiento))
            connection.commit()
            
            self.id = cursor.lastrowid
            return self.id
        except Exception as ex:
            print("No se pudo guardar el registro correctamente: ", ex)
            return 0
        finally:
            cursor.close()
            connection.close()
    
    
    def delete(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM clientes WHERE id = %d)"
            cursor.execute(query, (self.id))
            connection.commit()
            
            #self.id = cursor.lastrowid
            return self.id
        except Exception as ex:
            print("No se pudo guardar el registro correctamente: ", ex)
            return 0
        finally:
            cursor.close()
            connection.close()
    
    
    