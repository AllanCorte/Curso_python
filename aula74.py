# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

# python -m venv venv
# venv\Scripts\activate para ativar meu ambiente

# pip freeze > requirements.txt
''''''
'''
python -m venv venv: Cria um ambiente virtual chamado venv 
na pasta atual. Um ambiente virtual isola as dependências do seu projeto.
activate: Ativa o ambiente virtual no Windows, 
fazendo com que os pacotes instalados fiquem 
restritos a esse ambiente.
pip freeze > requirements.txt: Gera um arquivo chamado 
requirements.txt com a lista de todos os pacotes e versões 
instalados no ambiente virtual. Esse arquivo é útil para 
compartilhar as dependências do projeto com outras pessoas 
ou para instalar as mesmas dependências em outro ambiente 
usando pip install -r requirements.txt.''''''
'''
