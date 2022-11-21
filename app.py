from flask import Flask, render_template, request

import elden_ring

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"

@app.route("/monsters/")
@app.route("/monsters/<item_id>")
def monsters(item_id=None):
    engine = elden_ring.MonstersData()
    monsters = engine.load()

    if item_id:
        item = engine.get(item_id)
    else:
        item = None

    return render_template('monsters.html', item=item, monsters=monsters)

@app.route("/weapons/")
@app.route("/weapons/<item_id>")
def weapons(item_id=None):
    engine = elden_ring.WeaponsData()
    weapons = engine.load()

    if item_id:
        item = engine.get(item_id)
    else:
        item = None

    return render_template('weapons.html', item=item, weapons=weapons)

@app.route("/ammos/")
@app.route("/ammos/<item_id>")
def ammos(item_id=None):
    engine = elden_ring.ArrowsData()
    arrows = engine.load()

    if item_id:
        item = engine.get(item_id)
    else:
        item = None

    return render_template('ammos.html', item=item, arrows=arrows)
