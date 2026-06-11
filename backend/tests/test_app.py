import pytest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente

def test_verificar_status(cliente):
    
    resposta = cliente.get('/api/status')
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert "mensagem" in dados
    assert dados["mensagem"] == "API do Sistema de Chamados rodando perfeitamente!"