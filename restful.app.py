from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import Skills

app = Flask(__name__)
api = Api(app)

livroDeReceitas = [
    {
        "Titulo": "Bolo de Brigadeiro",
        "Ingredientes":[
            "1 lata de leite condensado",
            "3 ovos",
            "1/2 xícara (chá) de chocolate em pó",
            "1 xícara (chá) de leite",
            "2 colheres (sopa) de manteiga sem sal"
        ],
        "Modo de preparo": "No liquidificador bata todos os ingredientes até que estejam incorporados, depois Unte com manteiga e povilhe com açúcar uma forma redonda média com furo central e despeje o conteúdo do liquidificador, em seguido leve a forma ao forno, por aproximadamente 1 hora, por fim, retire a forma do forno, e coloque o colo em um prato grande, e cubra-o com granulado de brigadeiro à vontade e sirva o bolo.",
        "Rendimento": "12 fatias"
    },
    {
        "Titulo": "Pudim de Doce de Leite com Coco",
        "Ingredientes":[
            "1 xícara (chá) de açúcar",
            "1/2 xícara (chá) de água fervendo",
            "400 gramas de doce de leite",
            "3 ovos",
            "100 ml de leite",
            "200 ml de leite de coco",
            "1 xícara (chá) de coco ralado"
        ],
        "Modo de preparo": "Em uma panela com fundo largo coloque o açúcar, quando ele derreter totalmente e virar cor de caramelo acrescente a água fervente, misture bem até que todos os pedacinhos estejam bem dissolvidos e deixe reduzir um pouco nesta etapa não misture mais. Em seguida, despeje na sua forma com furo central. No liquidificador bata o doce de leite, o leite, o leite de coco e os ovos até que estejam incorporados. Adicione o coco ralado e bata novamente. Despeje a mistura do liquidificador na forma já com a calda. Cubra com papel alumínio e leve ao forno em banho-maria a 200° por aproximadamente 1h e 10min, ou até que esteja firme. Espere esfriar um pouco e leve a geladeira por 4 horas. Desenforme e sirva o bolo.",
        "Rendimento": "10 fatias"
    }
]

class Receitas(Resource):
    def get(self):
        return {"status": 200, "data": livroDeReceitas}

    def post(self):
        newReceita = json.loads(request.data)
        print(newReceita)
        newReceita["id"]=len(livroDeReceitas) +1
        livroDeReceitas.append(newReceita)
        return {
            "message": "Created!",
            "newValue": newReceita
        }

class Receita(Resource):
    def get(self, indice):
        try:
            return livroDeReceitas[indice]
        except IndexError:
            mensagem = "O índice {} não foi encontrado no array".format(indice)
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }
        except:
            mensagem = "Erro desconhecido"
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }

    def put(self, indice):
        newReceita =json.loads(request.data)
        livroDeReceitas[indice] = newReceita
        return {
            "message": "Updated!",
            "newValue": newReceita
        }

    def delete(self, indice):
        livroDeReceitas.pop(indice)
        return {
            "message": "Deleted!",
            "arrayAtual": livroDeReceitas
        }

api.add_resource(Receitas, "/receitas/")
api.add_resource(Receita, "/receitas/<int:indice>")
api.add_resource(Skills, "/skills/")

if __name__ == '__main__':
    app.run(debug=True)