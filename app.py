from flask import Flask, render_template
app = Flask(__name__)

pokemons = [
    ['Guaraná  R$: 4.50', 'https://corintios.com.br/cantina/wp-content/uploads/2018/01/guarana_lata.jpg'],
    ['Pizza R$: 2.50', 'https://img.stpu.com.br/?img=https://s3.amazonaws.com/pu-mgr/default/a0R0f000010xA7GEAU/5c489cd8e4b0842c9b1b6c10.jpg&w=710&h=462'],
    ['Suco R$: 24.90', 'https://casafiesta.fbitsstatic.net/img/p/suco-de-laranja-integral-prats-900ml-66809/233677.jpg?w=800&h=800&v=no-change'],
    ['Lanche R$: 18.50', 'https://img.stpu.com.br/?img=https://s3.amazonaws.com/pu-mgr/default/a0R0f00000zTEo1EAG/5b3a7b01e4b0f1518ff176df.jpg&w=710&h=462']
]

@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo='Pokédex',
        pokemons=pokemons
    )

@app.route('/poke/<int:id>')
def pokemon(id):
    poke = pokemons[id]
    return render_template(
        'pokemon.html',
        pokemon=poke
    )

if __name__ == '__main__':
    app.run()