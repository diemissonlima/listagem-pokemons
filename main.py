from flask import Flask, render_template
from random import choice

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/pokemon')
def pokemon():
    dados = {
        'poke-001': {'nome': 'Bulbasaur', 'tipo': 'Planta', 'img': 'imagens/bulbasaur.gif'},
        'poke-002': {'nome': 'Ivysaur', 'tipo': 'Planta', 'img': 'imagens/ivysaur.gif'},
        'poke-003': {'nome': 'Venusaur', 'tipo': 'Planta', 'img': 'imagens/venusaur.gif'},
        'poke-004': {'nome': 'Charmander', 'tipo': 'Fogo', 'img': 'imagens/charmander.gif'},
        'poke-005': {'nome': 'Charmeleon', 'tipo': 'Fogo', 'img': 'imagens/charmeleon.gif'},
        'poke-006': {'nome': 'Charizard', 'tipo': 'Fogo', 'img': 'imagens/charizard.gif'},
        'poke-007': {'nome': 'Squirtle', 'tipo': 'Água', 'img': 'imagens/squirtle.gif'},
        'poke-008': {'nome': 'Wartortle', 'tipo': 'Água', 'img': 'imagens/wartortle.gif'},
        'poke-009': {'nome': 'Blastoise', 'tipo': 'Água', 'img': 'imagens/blastoise.gif'},
        'poke-010': {'nome': 'Caterpie', 'tipo': 'Inseto', 'img': 'imagens/caterpie.gif'},
        'poke-011': {'nome': 'Metapod', 'tipo': 'Inseto', 'img': 'imagens/metapod.gif'},
        'poke-012': {'nome': 'Butterfree', 'tipo': 'Inseto', 'img': 'imagens/butterfree.gif'},
        'poke-013': {'nome': 'Weedle', 'tipo': 'Inseto', 'img': 'imagens/weedle.gif'},
        'poke-014': {'nome': 'Kakuna', 'tipo': 'Inseto', 'img': 'imagens/kakuna.gif'},
        'poke-015': {'nome': 'Beedrill', 'tipo': 'Inseto', 'img': 'imagens/beedrill.gif'},
        'poke-016': {'nome': 'Pidgey', 'tipo': 'Normal', 'img': 'imagens/pidgey.gif'},
        'poke-017': {'nome': 'Pidgeotto', 'tipo': 'Normal', 'img': 'imagens/pidgeotto.gif'},
        'poke-018': {'nome': 'Pidgeot', 'tipo': 'Normal', 'img': 'imagens/pidgeot.gif'},
        'poke-019': {'nome': 'Rattata', 'tipo': 'Normal', 'img': 'imagens/rattata-f.gif'},
        'poke-020': {'nome': 'Raticate', 'tipo': 'Normal', 'img': 'imagens/raticate-f.gif'},
        'poke-021': {'nome': 'Spearow', 'tipo': 'Normal', 'img': 'imagens/spearow.gif'},
        'poke-022': {'nome': 'Fearow', 'tipo': 'Normal', 'img': 'imagens/fearow.gif'},
        'poke-023': {'nome': 'Ekans', 'tipo': 'Veneno', 'img': 'imagens/ekans.gif'},
        'poke-024': {'nome': 'Arbok', 'tipo': 'Veneno', 'img': 'imagens/arbok.gif'},
        'poke-025': {'nome': 'Pikachu', 'tipo': 'Elétrico', 'img': 'imagens/pikachu.gif'},
        'poke-026': {'nome': 'Raichu', 'tipo': 'Elétrico', 'img': 'imagens/raichu.gif'},
        'poke-027': {'nome': 'Sandshrew', 'tipo': 'Terra', 'img': 'imagens/sandshrew.gif'},
        'poke-028': {'nome': 'Sandslash', 'tipo': 'Terra', 'img': 'imagens/sandslash.gif'},
        'poke-029': {'nome': 'Nidoran Fêmea', 'tipo': 'Veneno', 'img': 'imagens/nidoran-f.gif'},
        'poke-030': {'nome': 'Nidorina', 'tipo': 'Veneno', 'img': 'imagens/nidorina.gif'},
        'poke-031': {'nome': 'Nidoqueen', 'tipo': 'Veneno', 'img': 'imagens/nidoqueen.gif'},
        'poke-032': {'nome': 'Nidoran Macho', 'tipo': 'Veneno', 'img': 'imagens/nidoran-m.gif'},
        'poke-033': {'nome': 'Nidorino', 'tipo': 'Veneno', 'img': 'imagens/nidorino.gif'},
        'poke-034': {'nome': 'Nidoking', 'tipo': 'Veneno', 'img': 'imagens/nidoking.gif'},
        'poke-035': {'nome': 'Clefairy', 'tipo': 'Normal', 'img': 'imagens/clefairy.gif'},
        'poke-036': {'nome': 'Clafable', 'tipo': 'Normal', 'img': 'imagens/clefable.gif'},
        'poke-037': {'nome': 'Vulpix', 'tipo': 'Fogo', 'img': 'imagens/vulpix.gif'},
        'poke-038': {'nome': 'Ninetales', 'tipo': 'Fogo', 'img': 'imagens/ninetales.gif'},
        'poke-039': {'nome': 'Jigglypuff', 'tipo': 'Normal', 'img': 'imagens/jigglypuff.gif'},
        'poke-040': {'nome': 'Wigglytuff', 'tipo': 'Normal', 'img': 'imagens/wigglytuff.gif'},
        'poke-041': {'nome': 'Zubat', 'tipo': 'Veneno', 'img': 'imagens/zubat.gif'},
        'poke-042': {'nome': 'Golbat', 'tipo': 'Veneno', 'img': 'imagens/golbat.gif'},
        'poke-043': {'nome': 'Oddish', 'tipo': 'Planta', 'img': 'imagens/oddish.gif'},
        'poke-044': {'nome': 'Gloom', 'tipo': 'PLanta', 'img': 'imagens/gloom.gif'},
        'poke-045': {'nome': 'Vileplume', 'tipo': 'Planta', 'img': 'imagens/vileplume.gif'},
        'poke-046': {'nome': 'Paras', 'tipo': 'Inseto', 'img': 'imagens/paras.gif'},
        'poke-047': {'nome': 'Parasect', 'tipo': 'Inseto', 'img': 'imagens/parasect.gif'},
        'poke-048': {'nome': 'Venonat', 'tipo': 'Inseto', 'img': 'imagens/venonat.gif'},
        'poke-049': {'nome': 'Venomoth', 'tipo': 'Inseto', 'img': 'imagens/venomoth.gif'},
        'poke-050': {'nome': 'Diglett', 'tipo': 'Terra', 'img': 'imagens/diglett.gif'},
        'poke-051': {'nome': 'Dugtrio', 'tipo': 'Terra', 'img': 'imagens/dugtrio.gif'},
        'poke-052': {'nome': 'Meowth', 'tipo': 'Normal', 'img': 'imagens/meowth.gif'},
        'poke-053': {'nome': 'Persian', 'tipo': 'Normal', 'img': 'imagens/persian.gif'},
        'poke-054': {'nome': 'Psyduck', 'tipo': 'Água', 'img': 'imagens/psyduck.gif'},
        'poke-055': {'nome': 'Golduck', 'tipo': 'Água', 'img': 'imagens/golduck.gif'},
        'poke-056': {'nome': 'Mankey', 'tipo': 'Lutador', 'img': 'imagens/mankey.gif'},
        'poke-057': {'nome': 'Primeape', 'tipo': 'Lutador', 'img': 'imagens/primeape.gif'},
        'poke-058': {'nome': 'Growlithe', 'tipo': 'Fogo', 'img': 'imagens/growlithe.gif'},
        'poke-059': {'nome': 'Arcanine', 'tipo': 'Fogo', 'img': 'imagens/arcanine.gif'},
        'poke-060': {'nome': 'Poliwag', 'tipo': 'Água', 'img': 'imagens/poliwag.gif'},
        'poke-061': {'nome': 'Poliwhirl', 'tipo': 'Água', 'img': 'imagens/poliwhirl.gif'},
        'poke-062': {'nome': 'Poliwrath', 'tipo': 'Água', 'img': 'imagens/poliwrath.gif'},
        'poke-063': {'nome': 'Abra', 'tipo': 'Psíquico', 'img': 'imagens/abra.gif'},
        'poke-064': {'nome': 'Kadabra', 'tipo': 'Psíquico', 'img': 'imagens/kadabra.gif'},
        'poke-065': {'nome': 'Alakazam', 'tipo': 'Psíquico', 'img': 'imagens/alakazam.gif'},
        'poke-066': {'nome': 'Machop', 'tipo': 'Lutador', 'img': 'imagens/machop.gif'},
        'poke-067': {'nome': 'Machoke', 'tipo': 'Lutador', 'img': 'imagens/machoke.gif'},
        'poke-068': {'nome': 'Machamp', 'tipo': 'Lutador', 'img': 'imagens/machamp.gif'},
        'poke-069': {'nome': 'Bellsprout', 'tipo': 'Planta', 'img': 'imagens/bellsprout.gif'},
        'poke-070': {'nome': 'Weepinbell', 'tipo': 'Planta', 'img': 'imagens/weepinbell.gif'},
        'poke-071': {'nome': 'Victreebel', 'tipo': 'Planta', 'img': 'imagens/victreebel.gif'},
        'poke-072': {'nome': 'Tentacool', 'tipo': 'Água', 'img': 'imagens/tentacool.gif'},
        'poke-073': {'nome': 'Tentacruel', 'tipo': 'Água', 'img': 'imagens/tentacruel.gif'},
        'poke-074': {'nome': 'Geodude', 'tipo': 'Terra', 'img': 'imagens/geodude.gif'},
        'poke-075': {'nome': 'Graveler', 'tipo': 'Terra', 'img': 'imagens/graveler.gif'},
        'poke-076': {'nome': 'Golem', 'tipo': 'Terra', 'img': 'imagens/golem.gif'},
        'poke-077': {'nome': 'Ponyta', 'tipo': 'Fogo', 'img': 'imagens/ponyta.gif'},
        'poke-078': {'nome': 'Rapidash', 'tipo': 'Fogo', 'img': 'imagens/rapidash.gif'},
        'poke-079': {'nome': 'Slowpoke', 'tipo': 'Água', 'img': 'imagens/slowpoke.gif'},
        'poke-080': {'nome': 'Slowbro', 'tipo': 'Água', 'img': 'imagens/slowbro.gif'},
    }
    poke = [
        dados['poke-001'], dados['poke-002'], dados['poke-003'], dados['poke-004'], dados['poke-005'],
        dados['poke-006'], dados['poke-007'], dados['poke-008'], dados['poke-009'], dados['poke-010'],
        dados['poke-011'], dados['poke-012'], dados['poke-013'], dados['poke-014'], dados['poke-015'],
        dados['poke-016'], dados['poke-017'], dados['poke-018'], dados['poke-019'], dados['poke-020'],
        dados['poke-021'], dados['poke-022'], dados['poke-023'], dados['poke-024'], dados['poke-025'],
        dados['poke-026'], dados['poke-027'], dados['poke-028'], dados['poke-029'], dados['poke-030'],
        dados['poke-031'], dados['poke-032'], dados['poke-033'], dados['poke-034'], dados['poke-035'],
        dados['poke-036'], dados['poke-037'], dados['poke-038'], dados['poke-039'], dados['poke-040'],
        dados['poke-041'], dados['poke-042'], dados['poke-043'], dados['poke-044'], dados['poke-045'],
        dados['poke-046'], dados['poke-047'], dados['poke-048'], dados['poke-049'], dados['poke-050'],
        dados['poke-051'], dados['poke-052'], dados['poke-053'], dados['poke-054'], dados['poke-055'],
        dados['poke-056'], dados['poke-057'], dados['poke-058'], dados['poke-059'], dados['poke-060'],
        dados['poke-061'], dados['poke-062'], dados['poke-063'], dados['poke-064'], dados['poke-065'],
        dados['poke-066'], dados['poke-067'], dados['poke-068'], dados['poke-069'], dados['poke-070'],
        dados['poke-071'], dados['poke-072'], dados['poke-073'], dados['poke-074'], dados['poke-075'],
        dados['poke-076'], dados['poke-077'], dados['poke-078'], dados['poke-079'], dados['poke-080'],
    ]
    poke1 = choice(poke)
    poke2 = choice(poke)

    return render_template('pokemon.html', poke1=poke1, poke2=poke2)


if __name__ == '__main__':
    app.run(debug=True)
