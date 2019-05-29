from flask import Flask


app = Flask(__name__)

@app.route('/ola',methods=['GET'])
def ola_mundo():
    return "Olá mundo!", 200

if __name__ == '__main__':
    print("Servidor no ar")
    app.run(host='0.0.0.0',debug=True)