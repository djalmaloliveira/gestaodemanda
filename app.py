from flask import Flask, render_template
from flask import jsonify
import socket
#Djalma  04/12

app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Gestão de Demanda Contratada')

@app.route('/cliente.html')
def cliente():
    return render_template('cliente.html', the_title='Gestão de Demanda Contratada')

@app.route('/projeto.html')
def projeto():
    return render_template('projeto.html', the_title='Gestão de Demanda Contratada')

@app.route('/formulario.html')
def formulario():
    return render_template('formulario.html', the_title='Gestão de Demanda')

@app.route('/manual.html')
def manual():
    return render_template('manual.html', the_title='Manual da Gestão de Demanda')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Gestão de Demanda')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Gestão de Damanda - Cliente')

@app.route('/ip')
def ip():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    d = {
        "hostname": hostname,
        "IPAddr": IPAddr,
    }   
    return jsonify(d)

@app.route('/test-mysql-db-connection')
def test_db_connection():
    try:
        # google sql cloud database -- ip whitelisting test for heroku app
        from mysql.connector import connect
        cnx = connect(
            host='35.238.34.27',
            database='demo',
            user='nivratti',
            password='nivpoijkldfghcc@@', 
            port=3306
        )
        d = {
            "success": True,
            "message": "Connected to database successfully",
        }
    except Exception as e:
        d = {
            "success": False,
            "message": str(e),
        }
    return jsonify(d)

if __name__ == '__main__':
    app.run(debug=True)
