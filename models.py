from sqlalchemy import sql, orm
from app import db
import numpy as np
from statistics import mean 
from scipy import stats


class Player(db.Model):
    __tablename__ = 'players'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name', db.String(20), primary_key=True)



class PlayerOff(db.Model):
    __tablename__ = 'offStat'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    ppg = db.Column('ppg', db.Float)
    apg = db.Column('apg', db.Float)
    tov = db.Column('tov', db.Float)
    orpg = db.Column('orpg', db.Float)
    fgper = db.Column('fgper', db.Float)

    minutes = db.Column('min', db.Float)
    THptAr = db.Column('3ptAr', db.Float)
    TWptmr = db.Column('2ptmr', db.Float)
    THptr = db.Column('3ptr', db.Float)
    fbpsr = db.Column('fbpsr', db.Float)

    ftr = db.Column('ftr', db.Float)
    pipr = db.Column('pipr', db.Float)
    fgmUass = db.Column('fgmUass', db.Float)
    THptAtt = db.Column('3ptAtt', db.Float)
    THptper = db.Column('3ptper', db.Float)

    ftAtt = db.Column('ftAtt', db.Float)
    ftper = db.Column('ftper', db.Float)
    THptperD = db.Column('3ptperD', db.Float)

    def tester(self):
    	if self.minutes > 10:
    		print("ten")
    		return 10
    	else:
    		print("less")
    		return "less"


class PlayerAdvOff(db.Model):
    __tablename__ = 'advOff'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    drPts = db.Column('drPts', db.Float)
    drPer = db.Column('drPer', db.Float)
    casPts = db.Column('casPts', db.Float)
    casPer = db.Column('casPer', db.Float)
    pullPts = db.Column('pullPts', db.Float)
    pullPer = db.Column('pullPer', db.Float)
    postPts = db.Column('postPts', db.Float)
    postPer = db.Column('postPer', db.Float)
    elbPts = db.Column('elbPts', db.Float)
    elbPer = db.Column('elbPer', db.Float)

class PlayerDef(db.Model):
    __tablename__ = 'defStat'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    drpg = db.Column('drpg', db.Float)
    drebPer = db.Column('drebPer', db.Float)
    spg = db.Column('spg', db.Float)
    bpg = db.Column('bpg', db.Float)
    oppPoT = db.Column('oppPoT', db.Float)
    oppPsec = db.Column('oppPsec', db.Float)
    oppPIP = db.Column('oppPIP', db.Float)
    eightPer = db.Column('eightPer', db.Float)
    sixtTwentyPer = db.Column('sixtTwentyPer', db.Float)
    twenFourPer = db.Column('TwenFourPer', db.Float)
    gp = db.Column('gp', db.Float)
    fgDiffPer = db.Column('fgDiffPer', db.Float)
    def __repr__(self):
        return self.name


def games(playername):
    defPlayer = PlayerDef.query.filter_by(name=playername).first()
    return defPlayer.gp

def ppg(percentile):
    lst = []
    lstPts = []
    lstNms = []
    dict2 = {}
    pts=0
    denom=0
    off1 = PlayerOff.query.all()
    def1 = PlayerDef.query.all()
    def2 = PlayerDef.query.filter(PlayerDef.gp>5).all()
    off2 = PlayerAdvOff.query
    for y in def2:
        lst.append(y.name)

    # joiner = db.Model.query(PlayerOff, PlayerDef).outerjoin(PlayerDef, PlayerOff.name==PlayerDef.name).all()
    q1 = PlayerOff.query.filter(PlayerOff.name.in_(lst)).all()
    for x in q1:
        lstPts.append(x.ppg)
        lstNms.append(x.name)
    # for player in q1: 
    #     pts+=player.ppg
    #     denom+=1
    return np.percentile(lstPts, percentile)

def avg(att):
    lst = []
    lstAtt = []
    lstNms = []
    dict2 = {}
    pts=0
    denom=0
    off1 = PlayerOff.query.all()
    def1 = PlayerDef.query.all()
    def2 = PlayerDef.query.filter(PlayerDef.gp>5).all()
    off2 = PlayerAdvOff.query
    for y in def2:
        lst.append(y.name)

    # joiner = db.Model.query(PlayerOff, PlayerDef).outerjoin(PlayerDef, PlayerOff.name==PlayerDef.name).all()
    q1 = PlayerOff.query.filter(PlayerOff.name.in_(lst)).all()
    for x in q1:
        lstAtt.append(x.att)
        lstNms.append(x.name)
    # for player in q1: 
    #     pts+=player.ppg
    #     denom+=1
    return mean(lstAtt)

def ppgPer(pt):
    lst = []
    lstPts = []
    lstNms = []
    dict2 = {}

    Ans = []

    off1 = PlayerOff.query.all()
    def1 = PlayerDef.query.all()
    def2 = PlayerDef.query.filter(PlayerDef.gp>5).all()
    
    
    result = [r.drPts for r in PlayerAdvOff.query]
    for x in result:
        print(x)

    for y in def2:
        lst.append(y.name)

    # joiner = db.Model.query(PlayerOff, PlayerDef).outerjoin(PlayerDef, PlayerOff.name==PlayerDef.name).all()
    q1 = PlayerOff.query.filter(PlayerOff.name.in_(lst)).all()
    for x in q1:
        lstPts.append(x.ppg)

    Ans.append(stats.percentileofscore(lstPts, pt))


print(ppgPer(28))


       
    






        