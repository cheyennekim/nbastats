from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from livereload import Server
from forms import SearchForm


app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app, session_options={'autocommit': False})
app.debug = True

import models

@app.route('/', methods=['GET', 'POST'])
def all_players():
    players = models.Player.query.all()
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('first.html', players=players, form=search)


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
    Player = models.PlayerOff.query.filter_by(name=some_player).first()
    offDex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
    offNums = []
    goodStats = models.checkerG(some_player, 90.0)
    check1 = models.percentile(some_player)

    leader = models.leagueLead(check1)
    lgleader = []
    for x in leader:
        if x[0] in offDex:
            lgleader.append(x)

    linkitylst = models.iconSet(check1, some_player)
    for x in goodStats:
        if x[2] in offDex:
            offNums.append((x[0], x[1]))
    models.pieCharter(some_player)

    top = models.offtopThree(check1)

    # offNums=[('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0)]

    return render_template('readyplayer.html', player=Player, lstG=offNums, iconset = linkitylst, chart = '/static/scoreDist.png', name = Player.name, lead = lgleader)

@app.route('/<some_player>/defense')
def def_indy(some_player):

    Player = models.PlayerOff.query.filter_by(name=some_player).first()
    defDex = [28,29,30,31,32,33,34,35,36,37,38,40]    
    defNums = []
    goodStats = models.checkerG(some_player, 90.0)
    for x in goodStats:
        if x[2] in defDex:
            defNums.append((x[0], x[1]))
    return render_template('defensive.html', player=Player, lstGD=defNums)

@app.route('/<some_player>/scoutingreport')
def scouting_report(some_player):
    Player = models.PlayerOff.query.filter_by(name=some_player).first()
    defDex = [28,29,30,31,32,33,34,35,36,37,38,39]
    defNums = []
    goodStats = models.checkerG(some_player, 90.0)
    for x in goodStats:
        if x[2] in defDex:
            defNums.append((x[0], x[1]))
    return render_template('defensive.html', player=Player, lstGD=defNums)


@app.route('/allteams/<some_team>')
def teams_page(some_team):
    Teams = db.session.execute(
        'WITH temp1 as (select * from Teams, CoachedBy where Teams.teamabv = :val and Teams.teamabv = CoachedBy.team), temp2 as (select * from coaches) select * from temp1, temp2 where temp2.name = temp1.coach', {'val': some_team}).first()
    players = db.session.execute(
        'select * from isOn where team= :val', {'val': some_team})
    return render_template('team.html', team=Teams, players=players)



@app.route('/search/<searched_player>')
def search_page(searched_player):
    aplayer = models.IsOn.query.join(models.Player, models.IsOn.player == models.Player.name)\
    .filter_by(name = searched_player).first()
    
    return render_template('search.html', player = aplayer)



