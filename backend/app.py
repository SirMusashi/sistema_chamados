from flask import Flask, jsonify, request
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

@app.route('/api/responsaveis', methods=['GET'])
def listar_responsaveis():
    responsaveis = Responsavel.query.all()
    return jsonify([{"id": r.id, "nome": r.nome} for r in responsaveis])

@app.route('/api/chamados', methods=['GET'])
def listar_chamados():
    chamados = Chamado.query.all()
    return jsonify([c.to_dict() for c in chamados])

@app.route('/api/chamados', methods=['POST'])
def criar_chamado():
    dados = request.get_json()

    novo_chamado = Chamado(
        titulo=dados.get('titulo'),
        descricao=dados.get('descricao'),
        prioridade=dados.get('prioridade', 'media'),
        status='aberto' 
    )

    tipo_atribuicao = dados.get('tipo_atribuicao') 
    responsavel_id = dados.get('responsavel_id')

    if tipo_atribuicao == 'manual' and responsavel_id:
        novo_chamado.responsavel_id = responsavel_id
        
    elif tipo_atribuicao == 'automatica':
        # REGRA DE NEGÓCIO: DISTRIBUIÇÃO AUTOMÁTICA
        responsaveis = Responsavel.query.all()
        responsavel_escolhido = None
        menor_quantidade = float('inf') 

        for resp in responsaveis:
            qtd_em_aberto = Chamado.query.filter(
                Chamado.responsavel_id == resp.id,
                Chamado.status.in_(['aberto', 'em andamento'])
            ).count()

            if qtd_em_aberto < menor_quantidade:
                menor_quantidade = qtd_em_aberto
                responsavel_escolhido = resp

        if responsavel_escolhido:
            novo_chamado.responsavel_id = responsavel_escolhido.id

    db.session.add(novo_chamado)
    db.session.commit()

    return jsonify(novo_chamado.to_dict()), 201

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