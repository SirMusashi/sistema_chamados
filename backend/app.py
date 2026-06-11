from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite que o Vue.js converse com essa API

@app.route('/api/status', methods=['GET'])
def verificar_status():
    return jsonify({"mensagem": "API do Sistema de Chamados rodando perfeitamente!"})

if __name__ == '__main__':
    # O host 0.0.0.0 é necessário para rodar dentro do Docker
    app.run(host='0.0.0.0', port=5000, debug=True)