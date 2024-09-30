# API - É um lugar para disponibiliza a consulta, criação, edição e exclusão de livros.
# 1. Objetivo - Criar um api de disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base - localhost
# 3. Endpoints -
    # - localhost/livros (GET)
    # - localhost/livros (POST)
    # - localhost/livros/id (GET)
    # - localhost/livro/id (PUT)
    # - localhost/livro/id (DELETE) 
# 4. Quais recursos - Livros


from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter',
        'autor': 'Lord Valdemiro'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter',
        'autor': 'Lord Valdemiro'
    },
    {
        'id': 3,
        'titulo': 'Harry Potter',
        'autor': 'Lord Valdemiro'
    }    
]

# Consultar todos
@app.route('/livros', methods=['GET'])
def get_all():
    return jsonify(livros)


# Consultar id
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro_by_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def edit_livro(id):
    livro_alterado = request.get_json()
    for idx, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[idx].update(livro_alterado)
            return jsonify(livros[idx])

# Criar
@app.route('/livros', methods=['POST'])
def add_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_livro(id):
    for idx, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[idx]
        
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)