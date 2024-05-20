# This Is Compiled Python File 

import  csv
infile=open(r'C:\Users\lenovo\PycharmProjects\batch682\Program\matches.csv','r')
def showTeams():
    print('----select a team----')
    print('1. Sunrisers Hyderabad')
    print('2. Rising Pune Supergiant')
    print('3. Kolkata Knight Riders')
    print('4. Chennai Super Kings')
    print('5. Rajasthan Royals')
    print('6. Royal Challengers Bangalore')
    print('7. Mumbai Indians')
    print('8. Kings XI Punjab')
    print('9. Deccan Chargers')
    print('10. Kochi Tuskers Kerala')

    teamnum=int(input("please enter team name / Number: "))

    if teamnum==1:
        team='Sunrisers Hyderabad'
    elif teamnum==2:
        team='Rising Pune Supergiant'
    elif teamnum==3:
        team='Kolkata Knight Riders'
    elif teamnum==4:
        team='Chennai Super Kings'
    elif teamnum==5:
        team='Rajasthan Royals'
    elif teamnum==6:
        team='Royal Challengers Bangalore'
    elif teamnum==7:
        team='Mumbai Indians'
    elif teamnum==8:
        team='Kings XI Punjab'
    elif teamnum==9:
        team='Deccan Chargers'
    elif teamnum==10:
        team='Kochi Tuskers Kerala'

    return  team

def tossWin(team):
    with open('matches.csv') as ipl:
        read=csv.DictReader(ipl)
        print(read)
        totalToss=0
        wonToss=0
        for rows in read:
            if rows['TEAM1']==team or rows['TEAM2']==team:
               totalToss +=1
            if rows['TOSS_WINNER']==team:
                wonToss +=1
    return totalToss,wonToss
def yearWise_WonPlayed(team):
    with open('matches.csv') as ipl:
        read=csv.DictReader(ipl)
        stat={}
        year=set([rec['SEASON']for rec in read])

        for sec in year:
            total=0
            won=0
            ipl.seek(0)
            for rows in read:
                if (rows['TEAM1']==team and rows['SEASON']==sec or rows['TEAM2']==team and rows['SEASON']==sec):
                    total +=1
                    if rows['WINNER']==team and rows['SEASON']==sec:
                        won +=1
            stat[sec]={'Total':total,'Won':won}
        return stat
def locationWise(team) :
    with open('matches.csv') as vivoipl:
        check=csv.DictReader(vivoipl)
        report={}
        location=set([record['CITY'] for record in check])

        for city in location:
            total=0
            won=0
            vivoipl.seek(0)
            for rows in check:
                if (rows['TEAM1']==team and rows['CITY']==city or rows['TEAM2']==team and rows['CITY']==city):
                    total +=1
                    if rows['WINNER']==team and rows['CITY']==city:
                        won +=1
            report[city]={'total':total,'won':won}
        return report















