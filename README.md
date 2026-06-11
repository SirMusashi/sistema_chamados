# Sistema de Controle de Chamados Internos 

Este repositório contém a minha solução para o **Desafio Técnico Full Stack (Nível Básico)** para o processo seletivo do time de engenharia de software da **Codificar**.

##  Sobre o Projeto

O objetivo deste projeto é construir a primeira versão de um sistema para organizar e gerenciar pedidos de suporte interno de uma empresa. A aplicação visa resolver o problema de descentralização das solicitações (feitas por WhatsApp, e-mail, etc.) e equilibrar a carga de trabalho da equipe de suporte através de uma distribuição inteligente.

##  Justificativa de Arquitetura e Escolhas Tecnológicas (Item 1.2)

O escopo do desafio enfatiza a importância da **produtividade em times pequenos**, **redução de atrito** e **facilidade de execução local** por qualquer membro do time. Pensando nisso, estruturei a solução com as seguintes tecnologias:

* **Backend: Python com Flask**
  * **Por quê?** Python oferece uma sintaxe limpa e alta produtividade. O Flask, sendo um microframework, é leve, direto ao ponto e perfeito para construir APIs RESTful rápidas e eficientes sem a sobrecarga de ferramentas que não seriam utilizadas neste escopo inicial.
* **Frontend: Vue.js**
  * **Por quê?** O Vue.js permite a criação de interfaces reativas de forma muito intuitiva. Sua excelente componentização ajuda a manter o código limpo (DRY) e facilita a manutenção, alinhando-se com a necessidade de reduzir o atrito no desenvolvimento do lado do cliente.
* **Banco de Dados: SQLite**
  * **Por quê?** Para garantir que a aplicação seja executável localmente sem dor de cabeça. O SQLite dispensa a instalação e configuração de servidores de banco de dados pesados, rodando a partir de um único arquivo local.
* **Infraestrutura: Docker e Docker Compose**
  * **Por quê?** Atendendo diretamente ao requisito **6.1**, o uso de containers garante que qualquer pessoa da equipe da Codificar possa rodar o projeto com apenas um comando, sem se preocupar com versões de pacotes, instalação de linguagens ou conflitos de ambiente.

## Diário de Desenvolvimento

Para demonstrar a evolução e o funcionamento do sistema, documentei as etapas de desenvolvimento e as telas da aplicação:

### Estrutura de pastas:
![Estrutura de pastas](./imagens/01%20estrutura%20de%20pastas.png)

---
Desenvolvido por Bruno Duarte para o processo seletivo da Codificar.
