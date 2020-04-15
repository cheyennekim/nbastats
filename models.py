from sqlalchemy import sql, orm
from app import db
import math
import os
import numpy as np
from statistics import mean, median
from scipy import stats
import difflib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler


class Player(db.Model):
    __tablename__ = 'players'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name', db.String(20), primary_key=True)
    age = db.Column('age', db.Integer)

class IsOn(db.Model):
    __tablename__ = 'ison'
    __table_args__ = {'extend_existing': True}
    player = db.Column('player', db.String(20), primary_key=True)
    team = db.Column('team', db.String(20),primary_key=True)

class Teams(db.Model):
    __tablename__ = 'teams'
    __table_args__ = {'extend_existing': True}
    teamname = db.Column('teamname', db.String(50), primary_key=True) 
    teamabv = db.Column('teamabv', db.String(50))

class CoachedBy(db.Model):
    __tablename__ = "coachedby"
    __table_args__ = {'extend_existing': True}
    coach = db.Column('coach', db.String(40), primary_key=True)
    team = db.Column('team', db.String(20), primary_key=True)



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

class touchDrives(db.Model):
    __tablename__ = 'touchDrives'
    __table_args__ = {'extend_existing': True}
    name = db.Column('name', db.String(20), db.ForeignKey('player'), primary_key=True)
    touches = db.Column('touches', db.Float)
    fcTouch = db.Column('fcTouch', db.Float)
    timeOfpos = db.Column('timeOfpos', db.Float)
    avgSecTouch = db.Column('avgSecTouch', db.Float)
    ppTouch = db.Column('ppTouch', db.Float)

    elbowTouch = db.Column('elbowTouch', db.Float)
    postUps = db.Column('postUps', db.Float)
    paintTouch = db.Column('paintTouch', db.Float)
    ppElb = db.Column('ppElb', db.Float)
    ppPost = db.Column('ppPost', db.Float)

    ppPaint = db.Column('ppPaint', db.Float)
    drives = db.Column('drives', db.Float)
    dFGA = db.Column('dFGA', db.Float)
    dFGper = db.Column('dFGper', db.Float)
    dpts = db.Column('dpts', db.Float)

    dPassPer = db.Column('dPassPer', db.Float)
    dAstPer = db.Column('dAstPer', db.Float)
    dTovPer = db.Column('dTovPer', db.Float)
    dFoulPer = db.Column('dFoulPer', db.Float)

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

class mesA(db.Model):
    __tablename__ = 'mesA'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    yearStart = db.Column('yearStart', db.Float)
    position = db.Column('position', db.String(80))
    heightFT = db.Column('heightFT', db.Float)
    heightIN = db.Column('heightIN', db.Float)
    heightCM = db.Column('heightCM', db.Float)
    wingspan = db.Column('wingspan', db.Float)
    standReach = db.Column('standReach', db.Float)
    handLen = db.Column('handLen', db.Float)
    handWid = db.Column('handWid', db.Float)
    weight = db.Column('weight', db.Float)
    bodyFat = db.Column('bodyFat', db.Float)
    college = db.Column('college', db.String(80))

class mesB(db.Model):
    __tablename__ = 'mesB'
    __table_args__ = {'extend_existing': True}
    name = db.Column('player', db.String(20), db.ForeignKey('player'), primary_key=True)
    pick = db.Column('pick', db.Float)
    vert = db.Column('vert', db.String(80))
    vertNostep = db.Column('vertNostep', db.Float)
    bodyFat = db.Column('bodyFat', db.Float)
    bench = db.Column('bench', db.Float)
    agility = db.Column('agility', db.Float)
    sprint = db.Column('sprint', db.Float)
    
def games(playername):
    __table_args__ = {'extend_existing': True}
    defPlayer = PlayerDef.query.filter_by(name=playername).first()
    return defPlayer.gp

def avg(att):
    lst = []
    lstAtt = []
    lstNms = []

    def2 = PlayerDef.query.filter(PlayerDef.gp>5).all()
    for y in def2:
        lst.append(y.name)
    q1 = PlayerOff.query.filter(PlayerOff.name.in_(lst)).all()
    for x in q1:
        lstAtt.append(x.att)
        lstNms.append(x.name)
    return mean(lstAtt)


def setDic():
    playDict = {}
    off = PlayerOff.query.all()
    #all playerOff instances in offStat table
    def1 = PlayerDef.query.all()
    #all playerDef instances in defStat table
    off2 = PlayerAdvOff.query.all()
    #all playerAdvOff instances in advOff table
    off3 = touchDrives.query.all()

    for r in off:
        playDict[r.name] = [r.ppg, r.apg, r.tov, r.orpg, r.fgper, r.minutes, r.THptAr, r.TWptmr, r.THptr, r.fbpsr, r.ftr, r.pipr, r.fgmUass, r.THptAtt, r.THptper, r.ftAtt, r.ftper, r.THptperD]
        
   
    for p in off2:
        if p.name in playDict:
            playDict[p.name].append(p.drPts) 
            playDict[p.name].append(p.drPer)
            playDict[p.name].append(p.casPts)  
            playDict[p.name].append(p.casPer) 
            playDict[p.name].append(p.pullPts) 
            playDict[p.name].append(p.pullPer) 
            playDict[p.name].append(p.postPts)
            playDict[p.name].append(p.postPer)
            playDict[p.name].append(p.elbPts)  
            playDict[p.name].append(p.elbPer)  
        else:
            playDict[p.name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            playDict[p.name].append(p.drPts) 
            playDict[p.name].append(p.drPer)
            playDict[p.name].append(p.casPts)  
            playDict[p.name].append(p.casPer) 
            playDict[p.name].append(p.pullPts) 
            playDict[p.name].append(p.pullPer) 
            playDict[p.name].append(p.postPts)
            playDict[p.name].append(p.postPer)
            playDict[p.name].append(p.elbPts)  
            playDict[p.name].append(p.elbPer)  

    for k in def1:
        if k.name in playDict:
            playDict[k.name].append(k.drpg) 
            playDict[k.name].append(k.drebPer)
            playDict[k.name].append(k.spg)  
            playDict[k.name].append(k.bpg) 
            playDict[k.name].append(k.oppPoT) 
            playDict[k.name].append(k.oppPsec) 
            playDict[k.name].append(k.oppPIP)
            playDict[k.name].append(k.eightPer)
            playDict[k.name].append(k.sixtTwentyPer)  
            playDict[k.name].append(k.twenFourPer)  
            playDict[k.name].append(k.gp) 
            if k.gp < 7:
                playDict[k.name].append(0)
            else:
                playDict[k.name].append(1)
            playDict[k.name].append(k.fgDiffPer) 
        else:
            playDict[k.name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            playDict[k.name].append(k.drpg) 
            playDict[k.name].append(k.drebPer)
            playDict[k.name].append(k.spg)  
            playDict[k.name].append(k.bpg) 
            playDict[k.name].append(k.oppPoT) 
            playDict[k.name].append(k.oppPsec) 
            playDict[k.name].append(k.oppPIP)
            playDict[k.name].append(k.eightPer)
            playDict[k.name].append(k.sixtTwentyPer)  
            playDict[k.name].append(k.twenFourPer)  
            playDict[k.name].append(k.gp) 
            playDict[k.name].append(k.fgDiffPer) 
    for x,y in playDict.items():
        if (len(y) != 41):
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
    for k in off3:
        if k.name in playDict:
            playDict[k.name].append(k.touches) 
            playDict[k.name].append(k.fcTouch)
            playDict[k.name].append(k.timeOfpos)  
            playDict[k.name].append(k.avgSecTouch) 
            playDict[k.name].append(k.ppTouch) 
            playDict[k.name].append(k.elbowTouch) 
            playDict[k.name].append(k.postUps)
            playDict[k.name].append(k.paintTouch)
            playDict[k.name].append(k.ppElb)  
            playDict[k.name].append(k.ppPost)  
            playDict[k.name].append(k.ppPaint) 
            playDict[k.name].append(k.drives) 

            playDict[k.name].append(k.dFGA) 
            playDict[k.name].append(k.dFGper)
            playDict[k.name].append(k.dpts)
            playDict[k.name].append(k.dPassPer)  
            playDict[k.name].append(k.dAstPer)  
            playDict[k.name].append(k.dTovPer) 
            playDict[k.name].append(k.dFoulPer) 
        else:
            playDict[k.name] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x,y in playDict.items():
        if (len(y) != 60):
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
            playDict[x].append(0)
  
    return playDict
dic = setDic()
testlist=[]
stat_list = []
#stat_list in form of: [ (1, (3.0, 4.5, 5.0)), (2, (6.0, 2.0, 4.9))] with first num representing what statistic and list representing all values from all players
df = pd.DataFrame(data=dic)

for i in range((df.shape[0])): 
    #this is to input NBA wholistic data to calculate individual percentiles
    stat_list.append((i,[]))
    for x in range(df.shape[1]):
        if (df.iloc[39, x] == 1) and (df.iloc[5, x] > 5):
            stat_list[i][1].append(df.iloc[i,x])


# for x,y in dic.items():
#     if y[39]==1:
#         testlist.append(y[28])


# print("what we got", stats.percentileofscore(stat_list[28][1], 9))
# print("what old got", stats.percentileofscore(testlist, 9))

def percentile(playerName):
    ans = []
    for i in range(df.shape[0]):
        num = round(stats.percentileofscore((stat_list[i][1]), df.loc[i,playerName]), 2)
        ans.append(num)
    return ans

def checkerG(name, good):
    index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 40: "fgDiffPer", 41: "touches", 42: "fcTouch", 43: "timeOfpos", 44: "avgSecTouch", 45: "ppTouch", 46: "elbowTouch", 47: "postUps", 48: "paintTouch", 49: "ppElb", 50: "ppPost", 51: "ppPaint", 52: "drives", 53: "dFGA", 54: "dFGper", 55: "dpts", 56: "dPassPer", 57: "dAstPer", 58: "dTovPer", 59: "dFoulPer"}
    check1 = percentile(name)
    lstG = []
    for x in range(len(check1)):
        if x != 39:
            if check1[x] > good:
                lstG.append((check1[x], index[x], x))
    return lstG

def checkerB(name, bad):
    index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 40: "fgDiffPer", 41: "touches", 42: "fcTouch", 43: "timeOfpos", 44: "avgSecTouch", 45: "ppTouch", 46: "elbowTouch", 47: "postUps", 48: "paintTouch", 49: "ppElb", 50: "ppPost", 51: "ppPaint", 52: "drives", 53: "dFGA", 54: "dFGper", 55: "dpts", 56: "dPassPer", 57: "dAstPer", 58: "dTovPer", 59: "dFoulPer"}
    check1 = check(name)
    lstB = []
    for x in range(len(check1)):
        if check1[x] < bad:
            lstB.append((check1[x], index[x]))
    return lstB

def leagueLead(perc):
    index = {0: "ppg", 1: "apg", 2: "tov", 3: "orpg", 4: "fgper", 5: "minutes", 6: "THptAr", 7: "TWptmr", 8: "THptr", 9: "fbpsr", 10: "ftr", 11: "pipr", 12: "fgmUass", 13: "THptAtt", 14: "THptper", 15: "ftAtt", 16: "ftper", 17: "THptperD", 18: "drPts", 19: "drPer", 20: "casPts", 21: "casPer", 22: "pullPts", 23: "pullPer", 24: "postPts", 25: "postPer", 26: "elbPts", 27: "elbPer", 28: "drpg", 29: "drebPer", 30: "spg", 31: "bpg", 32: "oppPoT", 33: "oppPsec", 34: "oppPIP", 35: "eightPer", 36: "sixTwentyPer", 37: "twenFourPer", 38: "gp", 40: "fgDiffPer", 41: "touches", 42: "fcTouch", 43: "timeOfpos", 44: "avgSecTouch", 45: "ppTouch", 46: "elbowTouch", 47: "postUps", 48: "paintTouch", 49: "ppElb", 50: "ppPost", 51: "ppPaint", 52: "drives", 53: "dFGA", 54: "dFGper", 55: "dpts", 56: "dPassPer", 57: "dAstPer", 58: "dTovPer", 59: "dFoulPer"}
    ans = []
    for x in range(len(perc)):
        if perc[x] == 100.0:
            ans.append((x,index[x]))
    return ans

def iconSet(checkerG, player):
    ftSpecial = "whistle.svg"
    threeBall = "target.svg"
    quickWball = "clockFast.svg"
    driver = "driver.svg"
    pos = "possession.svg"
    time = "time.svg"
    workhorse = "shield.png"
    TO = "warning.svg"
    stateFarm = "assist.svg"
    

    linkitylist=[]
    if checkerG[10] > 80:
        linkitylist.append((ftSpecial, "Free Throw Specialist", "Percentage of Points from Free Throws: " + str(df.loc[10,player])))
    if checkerG[14] > 80:
        linkitylist.append((threeBall, "Long Range Specialist", "Three Point Percentage: " + str(df.loc[14,player])))
    if checkerG[18] > 80 and (checkerG[53] > 80 or checkerG[52] > 80):
        linkitylist.append((driver, "Driver", "Driving PPG: " + str(df.loc[18,player])))
    if checkerG[43] > 85:
        linkitylist.append((pos, "Ball Dominant", "Time of Possession per game: " + str(df.loc[43,player])))
    if checkerG[44] > 80:
        linkitylist.append((time, "Ball Holder", "Average Time per possession: " + str(df.loc[44,player])))
    if checkerG[44] < 20:
        linkitylist.append((quickWball, "Hot Potato", "Average Time per possession: " + str(df.loc[44,player])))
    if checkerG[5] > 85:
        linkitylist.append((workhorse, "Work Horse", "Minutes per game: " + str(df.loc[5,player])))
    if checkerG[2] > 85:
        linkitylist.append((TO, "Turnover Hazard", "Turnovers per game: " + str(df.loc[2,player])))
    if checkerG[1] > 85:
        linkitylist.append((stateFarm, "Distributor", "Assists per game: " + str(df.loc[1,player])))
    return linkitylist
# print(iconSet(percentile("Jayson Tatum")))

def pieCharter(some_player):
    plt.close('all')
    labels = 'Free Throws', 'Mid Range', 'Three Pointers', 'Paint', 'Fast Break'
    Player = PlayerOff.query.filter_by(name=some_player).first()
    sizes = [Player.ftr, Player.TWptmr, Player.THptr, Player.pipr, Player.fbpsr]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'magenta']

    # Plot
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    # plt.savefig('/Users/daniellanda/Desktop/NBA_316/nbastats/templates/' + some_player + 'scoreDist.svg')
    strFile = "/Users/daniellanda/Desktop/NBA_316/nbastats/static/iscoreDist_" + Player.name + ".svg"
    plt.savefig(strFile)
    plt.close()
    return None

def offtopThree(percentiles):
    offDex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
    first=0
    firstdex=0
    second=0
    seconddex=0
    third=0
    thirddex=0
    lst=[]
    for x in range(len(percentiles)):
        if x in offDex:
            perc = percentiles[x]
            if perc>first:
                first=perc
                firstdex=x
            elif perc>second:
                second=perc
                seconddex=x
            elif perc>third:
                third=perc
                thirddex=x
            else:
                None
    lst.append((firstdex, first))
    lst.append((seconddex, second))
    lst.append((thirddex, third))
    return lst

dfScale = df.T
scalar = MinMaxScaler()
dfScale[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,28,29,30,31,32,33,34,35,36,37,38,40]] = scalar.fit_transform(dfScale[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,28,29,30,31,32,33,34,35,36,37,38,40]])
rowLabels = dfScale.index.values

def euc(lst1, lst2):
    sum = 0
    for x in range(len(lst1)):
        minus = lst1[x]-lst2[x]
        sq = minus*minus
        sum+=sq
    return math.sqrt(sum)

def kNear(player, k):
    dude = dfScale.loc[player].values.tolist()
    closest = {}
    closestNames = []
    minu = 100
    ans = []
    similarity = []
    for x in rowLabels:
        if x != player:
            comp = dfScale.loc[x].values.tolist()
            dist = euc(dude, comp)
            if dist < minu:
                minu = dist
                closest[x] = dist
                closestNames.append(x)
    kclosest = closestNames[-1*k:]
    for k in kclosest:
        similarity.append(closest[k])
    ans.append(kclosest)
    ans.append(similarity)
    return ans

# print(dfScale.loc[['James Harden']])
# B = pd.Series(dfScale.loc[['LeBron James']])
xx = dfScale.loc[['LeBron James']]
y = dfScale.loc[['James Harden']]
dude = dfScale.loc["James Harden"].values.tolist()
print(kNear("Stephen Curry", 3))
# dude1 = dfScale.loc["LeBron James"].values.tolist()
# print(euc(dude,dude1))
# dude = dfScale.loc["Russell Westbrook"].values.tolist()
# dude1 = dfScale.loc["Russell Westbrook"].values.tolist()
# print(euc(dude,dude1))
#dfScale = MINMAX SCALED VERSION OF DF
# print(dfScale)
# maxi = dfScale.max()

# print(dfScale.max())
# print(dfScale.idxmax())
# data = stat_list[15][1]
# plt.hist(data, bins='auto')

# plt.show()
# for player, numbers in df.iteritems():
#     print(numbers)
# for col in df.columns:
#     print(col)
# df1 = pd.concat(df[', axis=1, keys=headers)
# df.plot.hist(alpha=0.5);

# Player = PlayerOff.query.filter_by(name="Patrick Beverley").first()    

