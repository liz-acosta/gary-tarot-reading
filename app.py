from flask import Flask, render_template, redirect, request, url_for
import random

GARY_TAROT = [
    {'card_name': "7 of Pentacles",
    'card_meaning': "Long-term view, sustainable results, perseverance, investment.",
    'card_image_filepath': "static/img/gary-tarot/gary-tarot-0-pentacles-7.png"
    },
    {'card_name': "9 of Pentacles",
    'card_meaning': "Abundance, luxury, self-sufficiency, financial independence.",
    'card_image_filepath': "static/img/gary-tarot/gary-tarot-0-pentacles-9.png"
    },
    {'card_name': "The Fool",
    'card_meaning': "Beginnings, innocence, spontaneity, a free spirit.",
    'card_image_filepath': "static/img/gary-tarot/gary-tarot-1-0-the-fool.png"
    },
    {'card_name': "Wheel of Fortune",
    'card_meaning': "Good luck, karma, life cycles, destiny, a turning point.",
    'card_image_filepath': "static/img/gary-tarot/gary-tarot-1-10-wheel-of-fortune.png"
    },
    {'card_name': "The Tower",
    'card_meaning': "Sudden change, upheaval, chaos, revelation, awakening.",
    'card_image_filepath': "static/img/gary-tarot/gary-tarot-1-16-the-tower.jpg"
    },
    {'card_name': "The World",
    'card_meaning': "Completion, integration, accomplishment, travel.",
    'card_image_filepath': "static/img/gary-tarot/gary-tarot-1-21-the-world.png"
    },       
]

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('tarot_reading'))
    return render_template('index.html')

@app.route("/tarotreading", methods=['GET', 'POST'])
def tarot_reading():
    tarot_card = random.choice(GARY_TAROT)
    return render_template('tarotreading.html', tarot_card=tarot_card)