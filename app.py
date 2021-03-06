from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from livereload import Server
from forms import SearchForm
import os

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app, session_options={'autocommit': False})
app.debug = True

import models
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
	
@app.route('/', methods=['GET', 'POST'])
def all_players():
    players = models.Player.query.all()
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('first.html', players=players, form=search)


@app.route('/allplayers',methods=['GET', 'POST'])
def allplayer_page():
    players = models.IsOn.query.join(models.Player, models.IsOn.player == models.Player.name)\
        .add_columns(models.IsOn.player, models.IsOn.team, models.Player.age)
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('allplayers.html', players=players, form=search)


@app.route('/allteams', methods=['GET', 'POST'])
def allteams_page():
    teams = models.Teams.query.join(models.CoachedBy, models.Teams.teamabv == models.CoachedBy.team)\
        .add_columns(models.Teams.teamname, models.Teams.teamabv, models.CoachedBy.coach)
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('allteams.html', teams=teams, form=search)


@app.route('/<some_player>',methods=['GET', 'POST'])
def some_player_page(some_player):
    Player = models.PlayerOff.query.filter_by(name=some_player).first()
    offDex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
    offNums = []
    #lst of stat percentiles greater than 90 using goodStats
    goodStats = models.checkerG(some_player, 90.0)
    #lst of all stat percentiles greater than 90
    pcent = models.percentile(some_player)
    #lst of each stat percentile
    leader = models.leagueLead(pcent)
    #lst of each stat that is exactly 100th percentile
    lgleader = []
    #lst of each offensive league leading stat
    for x in leader:
        #get offensive league leading stats
        if x[0] in offDex:
            lgleader.append(x)

    iconlst = models.iconSet(pcent, some_player)
    #list of icons with statistical descriptions
    for x in goodStats:
        #creating lst of stat percentiles greater than 90
        if x[3] in offDex:
            offNums.append((x[0], x[1], x[2]))
    
    models.pieCharter(some_player)
    models.compOff(some_player)
    models.compOff2(some_player)

    top = models.offtopThree(pcent)

    # offNums=[('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0),('fg%', 80.0)]
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('readyplayer.html', player=Player, lstG=offNums, iconset = iconlst, name = Player.name, lead = lgleader, form=search)

@app.route('/<some_player>/defense',methods=['GET', 'POST'])
def def_indy(some_player):

    Player = models.PlayerOff.query.filter_by(name=some_player).first()
    PlayerDef = models.PlayerDef.query.filter_by(name=some_player).first()
    defDex = [28,29,30,31,32,33,34,35,36,37,38,40]    
    defNums = []
    goodStats = models.checkerG(some_player, 90.0)
    for x in goodStats:
        if x[3] in defDex:
            defNums.append((x[0], x[1], x[2]))
    models.compDef(some_player)
    models.compDef2(some_player)
    pcent = models.percentile(some_player)
    #lst of each stat percentile
    leader = models.leagueLead(pcent)
    #lst of each stat that is exactly 100th percentile
    lgleader = []
    #lst of each offensive league leading stat
    for x in leader:
        #get offensive league leading stats
        if x[0] in defDex:
            lgleader.append(x)

    iconlst = models.iconSetD(pcent, some_player)
    #list of icons with statistical descriptions
    
    models.pieCharter(some_player)
    models.compOff(some_player)
    models.compOff2(some_player)

    defPhoto = []
    if PlayerDef.fgDiffPer > 0:
        defPhoto.append(PlayerDef.fgDiffPer)
        defPhoto.append("UPUP.svg")
    else:
        defPhoto.append(PlayerDef.fgDiffPer)
        defPhoto.append("DOWNDOWN.svg")

    top = models.offtopThree(pcent)
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('defensive.html', player=Player, lstG=defNums, iconset = iconlst, name = Player.name, lead = lgleader, defend = defPhoto, form =search)

@app.route('/<some_player>/scoutingreport',methods=['GET', 'POST'])
def scouting_report(some_player):
    Player = models.PlayerOff.query.filter_by(name=some_player).first()
    playSal = models.salary.query.filter_by(name=some_player).first()

    LandaSalary = models.kNearSalary(some_player, 5)
    comps = models.kNearProduction(some_player, 5)
    LandaSalary = "{:,}".format(round(LandaSalary))
    salary = playSal.nineteen
    salary = "{:,}".format(round(salary))
    offPS = models.offPS(some_player)
    defPS = models.defPS(some_player)
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('scoutingreport.html', player=Player, LandaSal = LandaSalary, sal = salary, form=search, name = Player.name, ops = offPS, comp = comps, dps = defPS)


@app.route('/allteams/<some_team>',methods=['GET', 'POST'])
def teams_page(some_team):
    Teams = db.session.execute(
        'WITH temp1 as (select * from Teams, CoachedBy where Teams.teamabv = :val and Teams.teamabv = CoachedBy.team), temp2 as (select * from coaches) select * from temp1, temp2 where temp2.name = temp1.coach', {'val': some_team}).first()
    players = db.session.execute(
        'select * from isOn where team= :val', {'val': some_team})
    search = SearchForm(request.form)
    search_string = search.data['search']
    if request.method == 'POST':
        return search_page(search_string)
    return render_template('team.html', team=Teams, players=players, form=search)



@app.route('/search/<searched_player>', methods=['GET', 'POST'])
def search_page(searched_player):
    searched_player = "%{}%".format(searched_player.lower())
    aplayers = models.IsOn.query.join(models.Player, models.IsOn.player == models.Player.name)\
    .filter(models.Player.name.ilike(searched_player)).all()
    return render_template('search.html', players = aplayers)



