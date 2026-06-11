import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, Responsavel, Chamado

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    
    with app.test_client() as cliente:
        with app.app_context():
            db.create_all()
            resp1 = Responsavel(nome='Alice')
            resp2 = Responsavel(nome='Bruno Duarte')
            resp3 = Responsavel(nome='Carlos')
            db.session.add_all([resp1, resp2, resp3])
            db.session.commit()
            
        yield cliente
        
        with app.app_context():
            db.drop_all()

def test_verificar_status(cliente):
    resposta = cliente.get('/api/status')
    assert resposta.status_code == 200

def test_distribuicao_automatica(cliente):
    
    dados_chamado_1 = {
        "titulo": "Impressora quebrada",
        "descricao": "Não imprime",
        "tipo_atribuicao": "automatica"
    }
    resposta_1 = cliente.post('/api/chamados', json=dados_chamado_1)
    assert resposta_1.status_code == 201
    assert resposta_1.get_json()["responsavel_id"] == 1

    dados_chamado_2 = {
        "titulo": "Sem internet",
        "descricao": "Cabo solto",
        "tipo_atribuicao": "automatica"
    }
    resposta_2 = cliente.post('/api/chamados', json=dados_chamado_2)
    assert resposta_2.status_code == 201
    assert resposta_2.get_json()["responsavel_id"] == 2