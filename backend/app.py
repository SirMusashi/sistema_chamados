from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_chamados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# TABELAS DO BANCO DE DADOS

class Responsavel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    chamados = db.relationship('Chamado', backref='responsavel', lazy=True)

class Chamado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    prioridade = db.Column(db.String(20), nullable=False) 
    status = db.Column(db.String(20), nullable=False, default='aberto') 
    data_abertura = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    responsavel_id = db.Column(db.Integer, db.ForeignKey('responsavel.id'), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "data_abertura": self.data_abertura.isoformat() if self.data_abertura else None,
            "responsavel_id": self.responsavel_id,
            "responsavel_nome": self.responsavel.nome if self.responsavel else "Não atribuído"
        }

# ROTAS DA API

@app.route('/api/status', methods=['GET'])
def verificar_status():
    return jsonify({"mensagem": "API do Sistema de Chamados rodando perfeitamente!"})

# CONFIGURAÇÃO INICIAL 

def inicializar_banco():
    with app.app_context():
        db.create_all()
        
        if Responsavel.query.count() == 0:
            resp1 = Responsavel(nome='Alice Tavares')
            resp2 = Responsavel(nome='Bruno Duarte') 
            resp3 = Responsavel(nome='Carlos Silva')
            
            db.session.add_all([resp1, resp2, resp3])
            db.session.commit()
            print("Banco de dados criado e responsáveis iniciais adicionados!")

if __name__ == '__main__':
    inicializar_banco()
    app.run(host='0.0.0.0', port=5000, debug=True)