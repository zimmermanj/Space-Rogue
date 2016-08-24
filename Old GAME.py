import random
import math
charnombre=[0,0,0,0,0]
charmelee=[0,0,0,0,0]
charshooter=[0,0,0,0,0]
charmage=[0,0,0,0,0]
charunarmed=[0,0,0,0,0]
charspeaker=[0,0,0,0,0]
charhacker=[0,0,0,0,0]
charcartographer=[0,0,0,0,0]
charrepair=[0,0,0,0,0]
charlore=[0,0,0,0,0]
charexplorer=[0,0,0,0,0]
damageperturn=[0,0,0,0,0]
halflifeperturn=[0,0,0,0,0]
edamageperturn=0
ehalflifeperturn=0
healstrength=[0]*5
poisonstrength=[0]*5
unpoisonstrength=[0]*5
def monstername():
    monadj_one=["huge", "small" ,"green", "blue", "purple", "yellow", "grey", "angry", "hungry", "muscular", "awakened", "dangerous", "one eyed"]
    monadj_two=["hairy", "hairless", "slimy", "triangular", "bug-like", "bloody", "injured"]
    monadj_three=["flying", "poisonous", "two headed"]
    montypearr=["reptile", "snake", "bird", "demon", "insectoid"]
    capconsonants=["W", "R","T","Y","P","S","D","F","G","K","L","Z","C","V","B","N","M"]
    consonants=["w", "r","t","y","p","s","d","f","g","k","l","z","c","v","b","n","m"]
    vowels=["a","e","i","o","u"]
    name=capconsonants[random.randint(0,len(capconsonants)-1)]+vowels[random.randint(0,len(vowels)-1)]+consonants[random.randint(0,len(consonants)-1)]+vowels[random.randint(0,len(vowels)-1)]+consonants[random.randint(0,len(consonants)-1)]
    monaone=monadj_one[random.randint(0, int( len( monadj_one)))-1]
    monatwo=monadj_two[random.randint(0, int( len( monadj_two)))-1]
    monathree=monadj_three[random.randint(0, int( len( monadj_three)))-1]
    montypearrd=montypearr[random.randint(0, int( len( montypearr)))-1]
    hitdiee=random.randint(1, 25)
    adjectivospormonster=("a "+monaone+" "+monatwo+" "+monathree+" "+montypearrd)
    monsterarray=[adjectivospormonster,hitdiee,name]
    return (monsterarray)
monsterarrayo=monstername()
monsterarrayt=monstername()
monsterarrayth=monstername()
monsterarrayf=monstername()
monsterarrayfi=monstername()
monsterarrays=monstername()
monsterarrayse=monstername()
monsterarraye=monstername()
monsterarrayn=monstername()
monsterarrayte=monstername()
print(monsterarrayo)
print(monsterarrayt)
print(monsterarrayth)
print(monsterarrayf)
print(monsterarrayfi)
print(monsterarrays)
print(monsterarrayse)
print(monsterarraye)
print(monsterarrayn)
print(monsterarrayte)
name=[monsterarrayo[2],monsterarrayt[2],monsterarrayth[2],monsterarrayf[2],monsterarrayfi[2],monsterarrays[2],monsterarrayse[2],monsterarraye[2],monsterarrayn[2],monsterarrayte[2],]
hitdiee=[monsterarrayo[1], monsterarrayt[1], monsterarrayth[1], monsterarrayf[1], monsterarrayfi[1], monsterarrays[1], monsterarrayse[1], monsterarraye[1], monsterarrayn[1], monsterarrayte[1], ]
adjectivospormonster=[monsterarrayo[0], monsterarrayt[0], monsterarrayth[0], monsterarrayf[0], monsterarrayfi[0], monsterarrays[0], monsterarrayse[0], monsterarraye[0], monsterarrayn[0], monsterarrayte[0], ]
ladder=["terrible", "poor", "mediocre", "average","fair", "good",  "great", "superb", "fantastic", "legendary", ]

def charactercreation():
    tlvt=0
    while tlvt<5:
        charnombre[tlvt]=input("name")
        charmelee[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charmelee[tlvt]]+" melee fighter")
        charshooter[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charshooter[tlvt]]+" shooter")
        charmage[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charmage[tlvt]]+" psionic")
        charunarmed[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charunarmed[tlvt]]+" unarmed fighter")
        charspeaker[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charspeaker[tlvt]]+" speaker")
        charhacker[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charhacker[tlvt]]+" hacker")
        charcartographer[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charcartographer[tlvt]]+" cartographer")
        charrepair[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charrepair[tlvt]]+" repair")
        charlore[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charlore[tlvt]]+" lore knower")
        charexplorer[tlvt]=random.randint(0,4)
        print(charnombre[tlvt]+ " is a "+ladder[charexplorer[tlvt]]+" explorer")
        healstrength[tlvt]=random.randint(0,1)
        poisonstrength[tlvt]=random.randint(0,1)
        unpoisonstrength[tlvt]=random.randint(0,1)
        tlvt+=1
charactercreation()

print(charnombre[0]+ "is a"+ladder[charmelee[0]]+" melee fighter")
def combat(type):
    creatua=random.randint(0,9)
    print("You encounter a "+name[creatua]+", "+adjectivospormonster[creatua])
    
    ehp=int(hitdiee[creatua])
    if type==0:
        php=[charmelee[0]*6, charmelee[1]*6, charmelee[2]*6, charmelee[3]*6, charmelee[4]*6, ]
        
    if type==1:
        php=[charshooter[0]*6, charshooter[1]*6, charshooter[2]*6, charshooter[3]*6, charshooter[4]*6, ]
        
    if type==2:
        php=[charmage[0]*6, charmage[1]*6, charmage[2]*6, charmage[3]*6, charmage[4]*6, ]
    if type==3:
        php=[charunarmed[0]*6, charunarmed[1]*6, charunarmed[2]*6, charunarmed[3]*6, charunarmed[4]*6, ]
    edamage=ehp
    ehp=ehp*6
    damagep=php
    end=0
    while(ehp>0 and php[0]+php[1]+php[2]+php[3]+php[4]):
        findstrongest=0
        strongest=0
        while(findstrongest<5):
            if(php[findstrongest]>=php[0]and php[findstrongest]>=php[1]and php[findstrongest]>=php[2]and php[findstrongest]>=php[3]and php[findstrongest]>=php[4]):
                strongest=findstrongest
                findstrongest+=5
            findstrongest+=1
        edamage=int(ehp/6)
        print(name[creatua]+' hits you.')
        lenumberp=php[strongest]-(random.randint(edamage, int(edamage*6)))
        php[strongest]=lenumberp
        print(str(charnombre[strongest])+'\'s health is now '+str(php[strongest]))
        if(php[0]<0):
            php[0]=0    
        if(php[1]<0):
            php[1]=0
        if(php[2]<0):
            php[2]=0
        if(php[3]<0):
            php[3]=0
        if(php[4]<0):
            php[4]=0
        if((php[0]+php[1]+php[2]+php[3]+php[4])<0):
            end=1
            print('You are defeated.')
        if(ehp>0 and php[0]>0):
            choice = input("choice")
            if(choice=="fire" and damagep[0]>0):
                print("Fire used.")
                lenumberp=ehp-(random.randint(int(damagep[0]/6), int(damagep[0])))
                ehp=lenumberp
                print('Enemy health is now '+str(ehp))
        if(ehp>0 and php[1]>0):
            choice = input("choice")
            if(choice=="fire" and damagep[1]>0 ):
                print("Fire used.")
                lenumberp=ehp-(random.randint(int(damagep[1]/6), int(damagep[1])))
                ehp=lenumberp
                print('Enemy health is now '+str(ehp))
        if(ehp>0 and php[2]>0):
            choice = input("choice")
            if(choice=="fire" and damagep[2]>0):
                print("Fire used.")
                lenumberp=ehp-(random.randint(int(damagep[2]/6), int(damagep[2])))
                ehp=lenumberp
                print('Enemy health is now '+str(ehp))
        if(ehp>0 and php[3]>0):
            choice = input("choice")
            if(choice=="fire" and damagep[3]>0):
                print("Fire used.")
                lenumberp=ehp-(random.randint(damagep[3]/6, int(damagep[3])))
                ehp=lenumberp
                print('Enemy health is now '+str(ehp))
        if(ehp>0 and php[4]>0):
            choice = input("choice")
            if(choice=="fire" and damagep[4]>0):
                print("Fire used.")
                lenumberp=ehp-(random.randint(int(damagep[4]/6), int(damagep[4])))
                ehp=lenumberp
                print('Enemy health is now '+str(ehp))
            if(choice=="heal" and damagep[4]>0 and healstrength>0):
                healthhealed=random.randint(1,10)*healstrength
                print("health healed "+healthhealed)
                
        if(ehp<=0):
            end=1
            print('Enemy defeated.')
wall=[0]*401
walllength=(math.sqrt(len(wall)-1)/2)
up=[0]*int((len(wall)-1)/4)
print(int(math.sqrt((len(wall))-1)))
down=[0]*int((len(wall)-1)/4)
left=[0]*int((len(wall)-1)/4)
right=[0]*int((len(wall)-1)/4)
number=3
tlv=0
while tlv<(len(wall)-1)/4:
    up[tlv]=number
    number+=4
    tlv+=1
number=1
tlv=0
while tlv<(len(wall)-1)/4:
    down[tlv]=number
    number+=4
    tlv+=1
number=2
tlv=0
while tlv<(len(wall)-1)/4:
    right[tlv]=number
    number+=4
    tlv+=1
number=4
tlv=0
while tlv<(len(wall)-1)/4:
    left[tlv]=number
    number+=4
    tlv+=1
number=4
tlv=0
while tlv<math.sqrt((len(wall)-1)/4):
    wall[number]=1
    number+=int(math.sqrt((len(wall)-1)/4)*4)
    tlv+=1
number=1
tlv=0
while tlv<math.sqrt((len(wall)-1)/4):
    wall[int(number)]=1
    number+=4
    tlv+=1
number=(len(wall)-1)-1
tlv=0
while tlv<math.sqrt((len(wall)-1)/4):
    wall[number]=1
    number-=4
    tlv+=1
number=(len(wall)-1)-2
tlv=0
while tlv<math.sqrt((len(wall)-1)/4):
    wall[int(number)]=1
    number-=math.sqrt((len(wall)-1)/4)*4
    tlv+=1
print("g")
newwall=random.randint(1, (len(wall)-1))
wallcount=0
newwallcountnum=((walllength-1)*(walllength-1))-(walllength-2)
print(newwallcountnum)
attempts=0
while wallcount<newwallcountnum and attempts<(4*int(len(wall))):
    print(attempts)
    attempts+=1
    newwall=random.randint(1, (len(wall)-1))
    tlv=0
    newwalltype=0

    while(newwalltype==0):

        if up[tlv]==newwall:
            newwalltype="up"
        if down[tlv]==newwall:
            newwalltype="down"
        if left[tlv]==newwall:
            newwalltype="left"
        if right[tlv]==newwall:
            newwalltype="right"
        tlv+=1

    newwalltouches=0
    if newwalltype=='up':
        if len(wall)-1>=newwall-1 and wall[newwall-1]==1:

            newwalltouches+=1
        if len(wall)-1>=newwall+1 and wall[newwall+1]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-4 and wall[newwall-4]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall+4 and wall[newwall+4]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall and wall[newwall]==1:
            newwalltouches+=3

        if len(wall)-1>=newwall+int((2*(math.sqrt(len(wall)-1)))-1):
            if wall[newwall+int((2*(math.sqrt(len(wall))))-1)]==1:
                newwalltouches+=1

        if len(wall)-1 >= newwall+int((2*(math.sqrt(len(wall)-1)))+1) and wall[int(newwall+((walllength-1)*4)+5)]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-1 and wall[newwall-1]==1 and len(wall)-1>=newwall+int((2*(math.sqrt(len(wall)-1)))-1):
            newwalltouches-=1

        if len(wall)-1>=newwall+1 and wall[newwall+1]==1 and len(wall)-1>=newwall+int((2*(math.sqrt(len(wall)-1)))+1) and wall[newwall+int((2*(math.sqrt(len(wall))))+1)]==1:
            newwalltouches-=1

    if newwalltype=='down':
        if len(wall)-1>=newwall+3 and wall[newwall+3]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall+1 and wall[newwall+1]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-4 and wall[newwall-4]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall+4 and wall[newwall+4]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall and wall[newwall]==1:
            newwalltouches+=3

        if len(wall)-1>=newwall-int((2*(math.sqrt(len(wall))))-1) and wall[newwall-int((2*(math.sqrt(len(wall))))-1)]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-int((2*(math.sqrt(len(wall))))+1) and wall[newwall-int((2*(math.sqrt(len(wall))))+1)]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall+3 and wall[newwall+3]==1 and len(wall)-1>=newwall-int((2*(math.sqrt(len(wall))))+1) and wall[newwall-int((2*(math.sqrt(len(wall))))+1)]==1:
            newwalltouches-=1

        if len(wall)-1>=newwall+1 and wall[newwall+1]==1 and len(wall)-1>=newwall-int((2*(math.sqrt(len(wall))))-1) and wall[newwall-int((2*(math.sqrt(len(wall))))-1)]==1:
            newwalltouches-=1

    if newwalltype=='left':
        if len(wall)-1>=newwall-3 and wall[newwall-3]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-1 and wall[newwall-1]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-5 and wall[newwall-5]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-7 and wall[newwall-7]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall and wall[newwall]==1:
            newwalltouches+=3

        if len(wall)-1>=newwall+(walllength*4) and wall[int(newwall+(walllength*4))]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-(walllength*4) and wall[int(newwall-(walllength*4))]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-3 and wall[newwall-3]==1 and len(wall)-1>=newwall-7 and wall[newwall-7]==1:
            newwalltouches-=1

        if len(wall)-1>=newwall-1 and wall[newwall-1]==1 and len(wall)-1>=newwall-5 and wall[newwall-5]==1:
            newwalltouches-=1

    if newwalltype=='right':
        if len(wall)-1>=newwall+3 and wall[newwall+3]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall+1 and wall[newwall+1]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall+5 and wall[newwall+5]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-1 and wall[newwall-1]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall and wall[newwall]==1:
            newwalltouches+=3

        if len(wall)-1>=newwall+(walllength*4) and wall[int(newwall+(walllength*4))]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall-(walllength*4) and wall[int(newwall-(walllength*4))]==1:
            newwalltouches+=1

        if len(wall)-1>=newwall+3 and wall[newwall+3]==1 and len(wall)-1>=newwall-1 and wall[newwall-1]==1:
            newwalltouches-=1

        if len(wall)-1>=newwall+1 and wall[newwall+1]==1 and len(wall)-1>=newwall+5 and wall[newwall+5]==1:
            newwalltouches-=1



    if(newwalltouches<2 and (len(wall)-1)>=newwall):

        wall[newwall]=1
        if newwalltype=='left' and (len(wall)-1)>=newwall-6:
            wall[newwall-6]=1
        if newwalltype=='right' and (len(wall)-1)>=newwall+6:
            wall[newwall+6]=1
        if newwalltype=='up' and (len(wall)-1)>=newwall+int(((walllength-1)*4)+2):
            wall[newwall+int(((walllength-1)*4)+2)]=1
        if newwalltype=='down' and (len(wall)-1)>=newwall-int(((walllength-1)*4)+2):
            wall[newwall-int(((walllength-1)*4)+2)]=1
        wallcount+=1

tlv=1
while tlv<len(wall):


    tlv+=1
currentposx=1
currentposy=1
currentup=3
currentdown=1
currentleft=4
currentright=2
norkle=0
while currentposy <(math.sqrt(len(wall)-1)/2) or currentposx<(math.sqrt(len(wall)-1)/2):
    move=input('move?')
    if(random.randint(1,10)>8):
        combat(random.randint(0,3))
    if move=='r' and currentposx<=(math.sqrt(len(wall)-1)/2) and int(len(wall))>=currentright and wall[int(currentright)]==0 :
        currentup+=4
        currentdown+=4
        currentleft+=4
        currentright+=4
        currentposx+=1
    if move=='l' and currentposx>=2 and int(len(wall))>=currentleft and wall[int(currentleft)]==0 :
        currentup-=4
        currentdown-=4
        currentleft-=4
        currentright-=4
        currentposx-=1
    if move=='u' and currentposy<=(math.sqrt(len(wall)-1)/2) and int(len(wall))>=currentup and wall[int(currentup)]==0 :
        currentup+=(walllength)*4
        currentdown+=(walllength)*4
        currentleft+=(walllength)*4
        currentright+=(walllength)*4
        currentposy+=1
    if move=='d' and currentposy>=2 and int(len(wall))>=currentdown and  wall[int(currentdown)]==0 :
        print('down works')
        currentup-=(walllength)*4
        currentdown-=(walllength)*4
        currentleft-=(walllength)*4
        currentright-=(walllength)*4
        currentposy-=1
print(str(currentposx)+', '+str(currentposy))
print(str(currentright)+" "+str(currentleft)+" "+str(currentup)+" "+str(currentdown))
overallinputthang=input("You see a big factory. Do you enter it? (y or n)")
if(overallinputthang=="y"):
    print("You enter a small room with dingy corridors.")
    combat(random.randint(0,3))
    
