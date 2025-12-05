from flask import Flask, request, render_template, jsonify
from entities.asiento import Asiento
from entities.cliente import Cliente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_cliente', methods=['POST'])
def save_cliente():
    
    data = request.get_json()
    

    cliente = Cliente(id=0, nombre=data['nombre'], email=data['email'], asiento=data['asiento'], pelicula=data['pelicula'])
    
    asiento = Asiento(id=0,pelicula=data['pelicula'], id_cliente=cliente.save(),numero=data['asiento'],estado='ocupado')
    asiento.save()
    if cliente.id == 0:
        return jsonify({"success":True, "id":cliente.id}), 201
    else:
        return jsonify({"success" : False,}), 500


@app.route('/clientes_confirmados', methods=['GET', 'POST'])
def mostrar_clientes():
    
    return render_template('lista_clientes.html', clientes=Cliente.get_all())

if __name__ == "__main__":
    app.run(port=5079, host='0.0.0.0')