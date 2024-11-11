from flask import Flask, jsonify, request

app = Flask(__name__)

informacoes = [
    {
        "id": 1,
        "pergunta": "O que é ciática?",
        "resposta": "A ciática é uma dor que se irradia ao longo do nervo ciático, que se estende da parte inferior da coluna até as pernas."
    },
    {
        "id": 2,
        "pergunta": "Quais são os sintomas da ciática?",
        "resposta": "Os sintomas incluem dor na parte inferior das costas, dor que irradia pela perna, fraqueza nas pernas e formigamento."
    },
    {
        "id": 3,
        "pergunta": "Como tratar a ciática?",
        "resposta": "O tratamento pode incluir fisioterapia, medicamentos anti-inflamatórios, exercícios e, em casos graves, cirurgia."
    }
]

#consultar
@app.route('/info',methods = ['GET'])
def ver_informacoes():
    return jsonify(informacoes)

#ver por id
@app.route('/info/<int:id>', methods=['GET'])
def ver_informacoes_id(id):
    for informacao in informacoes:
        if informacao.get('id') == id:
            return jsonify(informacao)

#Editar
@app.route('/info/<int:id>', methods=['PUT'])
def editar_informacoes_id(id):
    info_alterada = request.get_json()
    for indice,informacao in enumerate(informacoes):
        if informacao.get('id') == id:
            informacoes[indice].update(info_alterada)
            return jsonify(informacoes[indice])

#criar
@app.route('/info', methods=['POST'])
def add_informacoes():
    nova_info = request.get_json()
    informacoes.append(nova_info)

    return jsonify(informacoes)

#excluir
@app.route('/info/<int:id>', methods=['DELETE'])
def excluir_informacoes(id):
    for indice, informacao in enumerate(informacoes):
        if informacao.get('id') == id:
            del informacoes[indice]
        
    return jsonify(informacoes)
    

if __name__ == '__main__':
    app.run(debug=True)