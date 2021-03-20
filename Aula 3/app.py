from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/<int:id>")
def pessoas(id):
    return jsonify({"id":id,'nome':"Erik", "profissao":"programador"})

# @app.route('/soma/<int:n1>/<int:n2>/')
# def soma(n1,n2):
#     return jsonify({"soma": n1+n2})

@app.route('/soma',methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])

        print(dados)
        return jsonify({'soma': total})
    elif request.method == 'GET':
        total = 10 + 10
        return jsonify({'soma':total})

if __name__ == '__main__':
    app.run(debug=True)
