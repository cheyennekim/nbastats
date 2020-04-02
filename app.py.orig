from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, session_options={'autocommit': False})

import models


@app.route('/')
def all_players():
     players = models.Player.query.all()
     return render_template('first.html', players=players)


@app.route('/allplayers')
def allplayer_page():
    players = models.IsOn.query.join(models.Player, models.IsOn.player == models.Player.name)\
    	.add_columns(models.IsOn.player, models.IsOn.team, models.Player.age)
    return render_template('allplayers.html', players=players)

@app.route('/allteams')
def allteams_page():
	teams = models.Teams.query.join(models.CoachedBy, models.Teams.teamabv == models.CoachedBy.team)\
		.add_columns(models.Teams.teamname, models.Teams.teamabv, models.CoachedBy.coach)
	return render_template('allteams.html', teams=teams)

@app.route('/<some_player>')
def some_player_page(some_player):
	PlayerAdv = models.PlayerAdvOff.query.filter_by(name=some_player).first()
	Player = models.PlayerOff.query.filter_by(name=some_player).first()
	pD = models.PlayerDef.query.filter_by(name=some_player).first()

	percentFG = models.percentile(some_player, 3)
	tot = "str"
	type1 = "type"

	boo = models.check(some_player)






	return render_template('player.html', player = Player, player1 = PlayerAdv, pDef = pD, str = tot, type = type1, last = percentFG, verdict = boo)
	# return render_template('player.html')
