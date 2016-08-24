#Importing important libraries
import libtcodpy as libtcod
from runt import *
import pygame
from pygame.locals import *
from space import *

import random
import math
import random
import math
import time
import os 
import datetime
from compiler.ast import flatten
import sys
pygame.init()
screen_width=51
DISPLAYSURF = pygame.display.set_mode((screen_width*16, 16*screen_width*6/5),DOUBLEBUF)
pygame.display.set_caption('Drawing')
fontObj = pygame.font.Font('freesansbold.ttf', 16)
themes=[]
def console_print(x,y,message,color,backc):
	
	textSurfaceObj = fontObj.render(message, True,  color)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.left = x*16
	textRectObj.top=y*16
	DISPLAYSURF.blit(textSurfaceObj,textRectObj)
food=["zanka fruit","lean meat","zanka leaves","biscuit"]

bases=["gaddin","arbinal","branyl","resdin","chestin","narkinal","flattle"]

chemicals=["mundinal","adolite acid","dorminyl","incendite","mergin","burin acid","iecurcide","ilvenam","caecilem","curinal","mort acid","luminite","forticide","platzenite","edibisal","feurine","platzenyl","drug base","endonite","bandine","godyl"]
ladder=["terrible", "poor", "mediocre", "average","fair", "good",  "great", "superb", "fantastic", "legendary", ]
sys.stderr = open('error\errorlog.txt', 'w')
#sets screen width

bird=pygame.image.load("hack/bird.png")
blackc=pygame.image.load("hack/black.png")
bluec=pygame.image.load("hack/blue.png")
blood=pygame.image.load("hack/blood.png")
bush=pygame.image.load("hack/bush.png")
chemo=pygame.image.load("hack/chem1.png")
chemt=pygame.image.load("hack/chem2.png")
chemth=pygame.image.load("hack/chem3.png")
chemf=pygame.image.load("hack/chem4.png")
chemfi=pygame.image.load("hack/chem5.png")
chems=pygame.image.load("hack/chem6.png")
chemse=pygame.image.load("hack/chem7.png")
demon=pygame.image.load("hack/demon.png")
desertground=pygame.image.load("hack/desertground.png")
dirt=pygame.image.load("hack/dirt.png")
dirtwall=pygame.image.load("hack/dirtwall.png")

downstair=pygame.image.load("hack/downstair.png")
dumbgreyfloor=pygame.image.load("hack/dumbgreyfloor.png")
empty_h=pygame.image.load("hack/empty_h.png")
empty_h_f = pygame.transform.flip(empty_h, True, False)
exploder=pygame.image.load("hack/explode.png")
fire=pygame.image.load("hack/fire.png")
flamer=pygame.image.load("hack/flamer.png")
frog=pygame.image.load("hack/frog.png")
full_h=pygame.image.load("hack/full_h.png")
full_h_f = pygame.transform.flip(full_h, True, False)
gen_chem=pygame.image.load("hack/gen_chem.png")
grass=pygame.image.load("hack/grass.png")
green=pygame.image.load("hack/green.png")
hotground=pygame.image.load("hack/hotground.png")
hotwall=pygame.image.load("hack/hotwall.png")
hotliquid=pygame.image.load("hack/hotliquid.png")
hor_laser=pygame.image.load("hack/hor_laser.png")
hung=pygame.image.load("hack/hung.png")
hung_f=pygame.transform.flip(hung,True,False)
iceground=pygame.image.load("hack/iceground.png")
icewall=pygame.image.load("hack/icewall.png")
insectoid=pygame.image.load("hack/insectoid.png")
normalground=pygame.image.load("hack/normalground.png")
normalsecondary=pygame.image.load("hack/normalsecondary.png")
normalwall=pygame.image.load("hack/normalwall.png")
normalliquid=pygame.image.load("hack/normalliquid.png")
normaltree=pygame.image.load("hack/normaltree.png")
plants_tex=[pygame.image.load("hack/plant1.png"),pygame.image.load("hack/plant2.png"),pygame.image.load("hack/plant3.png"),pygame.image.load("hack/plant4.png"),pygame.image.load("hack/plant5.png"),pygame.image.load("hack/plant6.png")]
planetp=pygame.image.load("hack/planet.png")
playerp=pygame.image.load("hack/player.png")
postapocground=pygame.image.load("hack/postapocground.png")
postapocwall=pygame.image.load("hack/postapocwall.png")
redc=pygame.image.load("hack/red.png")
reptile=pygame.image.load("hack/reptile.png")
secondarypostapocground=pygame.image.load("hack/secondarypostapocground.png")
shield=pygame.image.load("hack/shield.png")
sand=pygame.image.load("hack/sand.png")
shooting_player=pygame.image.load("hack/shooting_player.png")
snow=pygame.image.load("hack/snow.png")
spaceship=pygame.image.load("hack/spaceship.png")
space_station=pygame.image.load("hack/space_station.png")
star=pygame.image.load("hack/star.png")
sword=pygame.image.load("hack/sword.png")
upstair=pygame.image.load("hack/upstair.png")
vert_laser=pygame.image.load("hack/vert_laser.png")
water=[pygame.image.load("hack/water1.png"),pygame.image.load("hack/water2.png"),pygame.image.load("hack/water3.png"), pygame.image.load("hack/waterbove.png")]


AQUA=(  0, 255, 255)
BLACK=(  0,   0,   0)
BLUE=(  0,  0, 255)
FUCHSIA=(255,   0, 255)
GREY=(128, 128, 128)
GREEN=(  0, 128,   0)
LIME=(  0, 255,   0)
MAROON=(128,  0,   0)
NAVY_BLUE=(  0,  0, 128)
OLIVE=(128, 128,   0)
PURPLE=(128,  0, 128)
RED=(255,   0,   0)
SILVER=(192, 192, 192)
TEAL=(  0, 128, 128)
WHITE=(255, 255, 255)
YELLOW=(255, 255,   0)













starx=[]
stary=[]
message_log=[]
for x in range(10000):
	starx.append(random.randint(0,1000))
	stary.append(random.randint(0,1000))
selected=None
#sets number of enemies spawned in the test
charnombre=0
charmelee=0

charshooter=0
charmage=0
charunarmed=0
charspeaker=0
charhacker=0
charcartographer=0
chemicals=[]
charrepair=0
charlore=0
charexplorer=0
def console_put_char_ex(x,y,png):
	recttodraw=pygame.Rect(x*16,y*16,16,16)
	if type(png)==str:
		DISPLAYSURF.blit(pygame.image.load(png).convert_alpha(),recttodraw)
	else:
		
		DISPLAYSURF.blit(png.convert_alpha(),recttodraw)

def eliminate_deadends():
	global planet
	for x in range(screen_width-1):
		for y in range(screen_width-1):
			antinections=0
			if planet[current_planet].tiles[x][y][current_floor].blocked==False:
				if x>2 and planet[current_planet].tiles[x-1][y][current_floor].blocked==True:
					antinections+=1
				if x<screen_width-2 and planet[current_planet].tiles[x+1][y][current_floor].blocked==True:
					antinections+=1
				if y>2 and planet[current_planet].tiles[x][y-1][current_floor].blocked==True:
					antinections+=1
				if  x<screen_width-2 and planet[current_planet].tiles[x][y+1][current_floor].blocked==True:
					antinections+=1
			if antinections>=3:
				print("DEAD END ELIMINATED")
				planet[current_planet].tiles[x][y][current_floor].blocked=True
				planet[current_planet].tiles[x][y][current_floor].room=None
		
				
				
	pygame.display.update()
	
	

	
	

enemies_spawned=0
number_of_planets=50
spacexmax=100
spacexmin=0-100
spaceymax=100
spaceymin=0-100
current_planet=0
wall_tile = 256 
floor_tile = 257
player_tile = 258
chemicals_made=10
orc_tile = 259
troll_tile = 260
scroll_tile = 261
healingpotion_tile = 262
sword_tile = 263
shield_tile = 264
stairsdown_tile = 265
dagger_tile = 266
player_radioactivity=0 #0
roomnum=0
fov_map=libtcod.map_new(screen_width-1, screen_width-1)
messages=[]
#libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)


messages=[""]*4
#makes screen





planet=[]
#makes inventory
inventory=[]
space_inventory=[]


current_floor=0
top_left=[0,0]
bottom_right=[49,49]
longest=0
longest_name="none"
file=open("map.txt","w+")

#creates tile class
class Item:
	def __init__(self,name,strength,x,y):
		global current_floor,current_planet
		self.name=name
		self.strength=strength
		self.x=x
		self.y=y
		self.planet=current_planet
		self.floor=current_floor
		self.number=1
		self.ascii=None
class Weapon(Item):
	__type="Weapon"
class Plant_I(Item):
	__type="PI"
class PSeed(Item):
	__type="PSeed"
class Wound:
	def __init__(self,name,loss):
		
		self.name=name
		self.loss=loss
		self.subtracted=False
		
class Armor:
	def __init__(self,name,strength,x,y):
		global current_floor,current_planet
		self.name=name
		self.strength=strength
		self.x=x
		self.y=y
		self.planet=current_planet
		self.floor=current_floor
		self.number=1
class Chemical:
	def __init__(self,name,strength,power,x,y):
		global current_floor,current_planet
		self.name=name
		self.strength=strength
		self.power=power
		self.x=x
		self.y=y
		self.taken=False
		self.planet=current_planet
		self.floor=current_floor
		self.number=1
weapons=[0]
weapons[0]=Weapon("Basic Weapon",1,None,None)
inventory.append(weapons[0])
armours=[0]
armours[0]=Armor("Basic Armour",1,None,None)
current_weapon=weapons[0]
current_armor=armours[0]
inventory.append(armours[0])
inventory.append(Chemical("mundinal",1,1,None,None))
inventory.append(Chemical("iecurcide",1,1,None,None))
inventory.append(Chemical("forticide",1,1,None,None))
inventory.append(Chemical("caecilem",1,1,None,None))
inventory.append(Chemical("incendite",1,1,None,None))
inventory.append(Chemical("dorminyl",1,1,None,None))
inventory.append(Chemical("mergin",1,1,None,None))
inventory.append(Chemical("ilvenam",1,1,None,None))
inventory.append(Chemical("gaddin",1,1,None,None))	
inventory.append(Chemical("arbinal",1,1,None,None))
inventory.append(Chemical("branyl",1,1,None,None))
inventory.append(Chemical("resdin",1,1,None,None))
inventory.append(Chemical("chestin",1,1,None,None))
inventory.append(Chemical("narkinal",1,1,None,None))
inventory.append(Chemical("flattle",1,1,None,None))							
class Tile:
	def __init__(self,blocked,path,monster_coordinate,terrain_type):
		self.blocked=blocked
		self.path=path
		self.monster_coordinate=monster_coordinate
		self.terrain_type=terrain_type
		self.stairu=[0,0]
		self.stair=[0,0]
		self.status_effect=None
		
		self.room=None
		self.theme_type=random.randint(0,1)
		self.dec=None
		self.liq=None
class Planet:
	def __init__(self,x,y,visited, player_x_coordinate,player_y_coordinate,name,theme):
		self.name=name
		self.x=x
		self.y=y
		self.visited=visited
		self.tiles=[[[Tile(True, "none","none","none") for x in xrange(2)]
			for y in xrange(screen_width-1)]
				for z in xrange(screen_width-1)]
		self.player_x_coordinate=player_x_coordinate
		self.player_y_coordinate=player_y_coordinate
		self.creature=[]
		self.floor_visited=[]
		self.color=libtcod.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.theme=theme
		for x in range(10):
			self.floor_visited.append(False) 
class monster:
	def __init__(self,x,y,goal_x_coordinate,goal_y_coordinate, capital, name,skill_level,floor,planet):
		self.x=x
		self.y=y
		self.goal_x_coordinate=goal_x_coordinate
		self.goal_y_coordinate=goal_y_coordinate
		self.capital=capital
		self.name=name
		self.skill_level=skill_level
		self.health_points=skill_level
		self.max_health=self.health_points
		self.floor=floor
		self.planet=planet
		self.status_effects=[status_effect("health", 50,1)]
		self.type=random.choice(["reptile","snake","bird","demon","insectoid","flame-being"])
		self.color=libtcod.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	def go(self):
		sleep=False
		for fect in self.status_effects:
			if fect.effect=="sleep":
				sleep=True
			
		if sleep==False and self.health_points>0 and current_planet==self.planet and current_floor==self.floor:
			return(path_finder(self.x,self.y,self.goal_x_coordinate,self.goal_y_coordinate))
	def draw(self):
		if self.type=="reptile" and self.health_points>0:
			
			console_put_char_ex(self.x, self.y, "hack/reptile.png")
		elif self.type=="snake" and self.health_points>0:
			console_put_char_ex(self.x, self.y, frog)
		elif self.type=="bird" and self.health_points>0:
			console_put_char_ex(self.x, self.y, bird)
		elif self.type=="demon" and self.health_points>0:
			console_put_char_ex(self.x, self.y, demon)
		elif self.type=="insectoid" and self.health_points>0:
			console_put_char_ex(self.x, self.y, insectoid)
		elif self.type=="flame-being" and self.health_points>0:
			
			console_put_char_ex(self.x, self.y,flamer)
			
	def move(self, x_modifier, y_modifier):
		if self.health_points>0 and current_planet==self.planet and current_floor==self.floor:
			self.x+=x_modifier
			self.y+=y_modifier		
#creates list of tiles
class status_effect:
	def __init__(self,effect, decay,power):
		self.effect=effect
		self.decay=decay
		self.power=power
		
class Player:
	def __init__(self, x,y):
		self.hunger=0
		self.x=x
		self.y=y
		self.health=100
		self.max_health=100
		self.wounds=[]
class Theme:
	def __init__(self, name, ground_tile,secondary_ground_tile,wall_tile,liquid_tile,shape,extras=None):
		self.name=name
		self.ground_tile=ground_tile
		self.secondary_ground_tile=secondary_ground_tile
		self.wall_tile=wall_tile
		self.liquid_tile=liquid_tile
		self.shape=shape
		self.extras=extras
class cPlant:
	def __init__(self, texture,harvest_item,growth_time,percent_of_obtain):
		self.texture=texture
		self.harvest_item=harvest_item
		self.growth_time=growth_time
		self.percent_of_obtain=percent_of_obtain

class Liquid:
	def __init__(self, type, inertia,depth):
		self.inertia=inertia
		self.type=type
		self.depth=depth
player_status_effects=[]
player=Player(None,None)
themes.append(Theme("post-apocalyptic", postapocground,secondarypostapocground,postapocwall,None,"dungeon",None))
themes.append(Theme("space station", postapocground,postapocground,postapocwall,None,"dungeon",None))
themes.append(Theme("normal", normalground,normalsecondary,normaltree,normalliquid,"cave",plants_tex))
themes.append(Theme("ice", iceground,iceground,icewall,normalliquid,"cave",None))
themes.append(Theme("hot", hotground,hotground,hotwall,hotliquid,"cave",None))
themes.append(Theme("desert", desertground,desertground,desertground,desertground,"cave",None))
plants=[cPlant(plants_tex[0],[Plant_I("petal",1,None,None),PSeed("fuegan",1,None,None)],50,[70,40]),cPlant(plants_tex[1],[Plant_I("sugar",1,None,None),PSeed("dulce cane",1,None,None)],45,[40,50]),cPlant(plants_tex[2],[Plant_I("fruit",1,None,None),Plant_I("leaf",1,None,None),PSeed("sanger bush",1,None,None)],50,[50,60,60]),cPlant(plants_tex[3],[PSeed("grass",1,None,None)],10,[80]),cPlant(plants_tex[4],[Plant_I("bark",1,None,None),PSeed("nochmadera",1,None,None)],60,[80,30]),cPlant(plants_tex[5],[Plant_I("nut",1,None,None),PSeed("flacon husk",1,None,None)],55,[70,45])]
def alchemy_convert(itemo,itemt):
	print("THAN")
	if itemo=='gaddin' and itemt=='arbinal' or itemo=='arbinal' and itemt=='gaddin':
		result='mundinal'
	elif itemo=='gaddin' and itemt=='branyl' or itemo=='branyl' and itemt=='gaddin':
		result=' adolite acid'
	elif itemo=='gaddin' and itemt=='resdin' or itemo=='resdin' and itemt=='gaddin':
		result='dorminyl'
	elif itemo=='gaddin' and itemt=='chestin' or itemo=='chestin' and itemt=='gaddin':
		result='incendite'
	elif itemo=='gaddin' and itemt=='narkinal' or itemo=='narkinal' and itemt=='gaddin':
		result='mergin'
	elif itemo=='gaddin' and itemt=='flattle' or itemo=='flattle' and itemt=='gaddin':
		result='burin acid'
	elif itemo=='arbinal' and itemt=='branyl' or itemo=='branyl' and itemt=='arbinal':
		result='iecurcide'
	elif itemo=='arbinal' and itemt=='resdin' or itemo=='resdin' and itemt=='arbinal':
		result='iecurcide'
	elif itemo=='arbinal' and itemt=='chestin' or itemo=='chestin' and itemt=='arbinal':
		result='caecilem'
	elif itemo=='arbinal' and itemt=='narkinal' or itemo=='narkinal' and itemt=='arbinal':
		result='curinal'
	elif itemo=='arbinal' and itemt=='flattle' or itemo=='flattle' and itemt=='arbinal':
		result='mort acid'
	elif itemo=='branyl' and itemt=='resdin' or itemo=='resdin' and itemt=='branyl':
		result='luminite'
	elif itemo=='branyl' and itemt=='chestin' or itemo=='chestin' and itemt=='branyl':
		result='forticide'
	elif itemo=='branyl' and itemt=='narkinal' or itemo=='narkinal' and itemt=='branyl':
		result='platzenite'
	elif itemo=='branyl' and itemt=='flattle' or itemo=='flattle' and itemt=='branyl':
		result='il-forticide'
	elif itemo=='resdin' and itemt=='chestin' or itemo=='chestin' and itemt=='resdin':
		result='feurine'
	elif itemo=='resdin' and itemt=='narkinal' or itemo=='narkinal' and itemt=='resdin':
		result='platzenyl'
	elif itemo=='resdin' and itemt=='flattle' or itemo=='flattle' and itemt=='resdin':
		result='drug-base'
	elif itemo=='chestin' and itemt=='narkinal' or itemo=='narkinal' and itemt=='chestin':
		result='endonite'
	elif itemo=='chestin' and itemt=='flattle' or itemo=='flattle' and itemt=='chestin':
		result='bandine'
	elif itemo=='narkinal' and itemt=='flattle' or itemo=='flattle' and itemt=='narkinal':
		result='godyl'
	else:
		
		result=False
	return(result)
#generates monster name
def monster_name():
	global longest, longest_name
	capital_consonants=["W", "R","T","Y","P","S","D","F","G","K","L","Z","C","V","B","N","M"]
	consonants=["w", "r","t","y","p","s","d","f","g","k","l","z","c","v","b","n","m"]
	vowels=["a","e","i","o","u"]
	first_letter=capital_consonants[random.randint(0,len(capital_consonants)-1)]
	name=first_letter
	
	
	start=time.clock()
	
	
	for i in xrange(random.randint(1,5)):
		name+=vowels[random.randint(0,len(vowels)-1)]+consonants[random.randint(0,len(consonants)-1)]
	name_return_array=[first_letter, name]
	return (name_return_array)

	end=time.clock()
	if (end-start)>longest:
		longest_name="monster name"
		longest=end-start	
#creates terrain
def make_terrain_types():
	global longest, longest_name

	start=time.clock()
	
	for x in xrange(screen_width-1):
		for y in xrange(screen_width-1):
			if planet[current_planet].tiles[x][y][current_floor].blocked!=True:
				planet[current_planet].tiles[x][y][current_floor].terrain_type=random.choice(["grass", "water", "dirt", "rock"])
			if planet[current_planet].tiles[x][y][current_floor].blocked==True:
				planet[current_planet].tiles[x][y][current_floor].terrain_type="wall"
	end=time.clock()
	if (end-start)>longest:
		longest_name="terrain make"
		longest=end-start
def check_for_status_effect(effelt):
	for fect in player_status_effects:
		if fect.effect==effelt:
			return True
			break
		else:
			return False
#defines room making code
def make_room(x1, x2, y1, y2):
	global longest, longest_name,roomnum
	print("("+str(x1)+", "+str(y1)+")"+" ("+str(x2)+", "+str(y2)+")")
	xt=max(x1,x2)
	xo=min(x1,x2)
	yt=max(y1,y2)
	yo=min(y1,y2)
	x1=xo
	x2=xt
	y1=yo
	y2=yt
	xlen=x2-x1
	ylen=y2-y1
	
	
	end=0
	for x in range(int(xlen)):
		
		
		for y in range(ylen):
			
			
			planet[current_planet].tiles[x1+x][y+y1][current_floor].blocked=False
			
			planet[current_planet].tiles[x1+x][y+y1][current_floor].room=roomnum
			
	start=time.clock()
	

	#for x in xrange(x2-x1):
		
		#for y in xrange(y2-y1):
			#libtcod.console_put_char_ex(0, x1+x, y1+y, "+", libtcod.blue, libtcod.black)
			#pygame.display.update()
			#planet[current_planet].tiles[x1+x][y1+y][current_floor].room=roomnum
			#if(planet[current_planet].tiles[x1+x][y1+y][current_floor].blocked==True):
				#planet[current_planet].tiles[x1+x][y1+y][current_floor].blocked=False
			#	planet[current_planet].tiles[x1+x][y1+y][current_floor].room=roomnum
			#	print("rooooomnuuuum"+str(roomnum))
			#	return True
			#else:
                
				#end=1
			#	return False
			#	break
	end=time.clock()
	if (end-start)>longest:
		longest_name="room make"
		longest=end-start
	return True
#defines a passage        
def make_passage(c1, c2, c3, type):
	global longest, longest_name
	end=0
	start=time.clock()
	if type== "y":
		print("passage ("+str(c3)+", "+str(min(c2, c1))+")"+" ("+str(c3)+", "+str(max(c2, c1))+")")
	if type== "x":
			print("passage ("+str(min(c2, c1))+", "+str(c3)+")"+" ("+str(max(c2, c1))+", "+str(c3)+")")
	for x in xrange(max(c2,c1)+1-min(c2,c1)):
	
		
		if type== "y":
			
			planet[current_planet].tiles[c3][x+min(c2, c1)][current_floor].blocked=False
			if planet[current_planet].tiles[c3][x+min(c2, c1)][current_floor].room==None:
				planet[current_planet].tiles[c3][x+min(c2, c1)][current_floor].room="passage"
		if type== "x":
			planet[current_planet].tiles[x+min(c2, c1)][c3][current_floor].blocked=False
			
			if planet[current_planet].tiles[x+min(c2, c1)][c3][current_floor].room==None:
				planet[current_planet].tiles[x+min(c2, c1)][c3][current_floor].room="passage"
	end=time.clock()
	if (end-start)>longest:
		longest_name="passage make"
		longest=end-start	   
#defines how monsters move, can be used as general pathfinder
def path_finder(start_x_coordinate,start_y_coordinate,  end_x_coordinate, end_y_coordinate):
	global longest, longest_name
	path_map=libtcod.path_new_using_map(fov_map, 0.0)
	libtcod.path_compute(path_map, start_x_coordinate,start_y_coordinate,end_x_coordinate,end_y_coordinate)
	goalcoor=[0,0]
	if not libtcod.path_is_empty(path_map):
		path_holder=libtcod.path_get(path_map, 0)
		
		goalcoor[0]=path_holder[0]-start_x_coordinate
		goalcoor[1]=path_holder[1]-start_y_coordinate
	if goalcoor[0]==1:
		pathfinding_result="x"
	elif goalcoor[0]==-1:
		pathfinding_result="-x"
	elif goalcoor[1]==1:
		pathfinding_result="y"
	elif goalcoor[1]==-1:
		pathfinding_result="-y"      
	else:
		pathfinding_result="n"
	return pathfinding_result
def check_for_able_to_move(x,y):
	global player, enemies_spawned, longest
	no_monster_there=True
	

	start=time.clock()


	for critter in creature[current_planet][current_floor]:
			
		if critter.x==player.x+x and critter.y ==player.y+y and critter.health_points>0:
			critter.health_points-=1
			no_monster_there=False
			message(critter.name+" has been hit")
		console_write (critter.capital)
		
	console_write (no_monster_there)			
	if no_monster_there==True:
		player.y += y
		player.x+=x
		
	end=time.clock()
	if (end-start)>longest:
		longest_name="check for able to move"
		longest=end-start	
		
#how the player moves on the ground	
def handle_keys():
	global mode,player, current_floor, longest, chemicals,weapons, armours
	
	
	
	if player.health<=0:
		return(True)
	pressedreal=False
	while pressedreal==False:
		for event in pygame.event.get():
			if event.type==KEYDOWN:
	
	
				if event.key == (K_UP) and planet[current_planet].tiles[player.x][player.y-1][current_floor].blocked==False and player.health>0:
		
					check_for_able_to_move(0,0-1)
					pressedreal=True
				elif event.key == (K_DOWN) and planet[current_planet].tiles[player.x][player.y+1][current_floor].blocked==False and player.health>0:
					check_for_able_to_move(0,1)
					pressedreal=True
				elif event.key == (K_LEFT) and planet[current_planet].tiles[player.x-1][player.y][current_floor].blocked==False and player.health>0:
		
					check_for_able_to_move(0-1,0)
					pressedreal=True
				elif event.key == (K_RIGHT) and planet[current_planet].tiles[player.x+1][player.y][current_floor].blocked==False and player.health>0:
					check_for_able_to_move(1,0)
					pressedreal=True
				elif event.key == (K_KP7) and planet[current_planet].tiles[player.x-1][player.y-1][current_floor].blocked==False and player.health>0:
					check_for_able_to_move(0-1,0-1)
					pressedreal=True
				elif event.key == (K_KP9) and planet[current_planet].tiles[player.x+1][player.y-1][current_floor].blocked==False and player.health>0:
					check_for_able_to_move(1,0-1)
					pressedreal=True
				elif event.key == (K_KP1) and planet[current_planet].tiles[player.x-1][player.y+1][current_floor].blocked==False and player.health>0:
					check_for_able_to_move(0-1,1)
					pressedreal=True
				elif event.key == (K_KP3) and planet[current_planet].tiles[player.x+1][player.y+1][current_floor].blocked==False and player.health>0:
					check_for_able_to_move(1,1)
					pressedreal=True
				elif event.key == (K_SPACE):
		
					mode="space"
					pressedreal=True
				elif event.key == (K_i):
					mode="inventory"
					pressedreal=True
				elif event.key == (K_u):
					mode="mix"
					pressedreal=True
				elif event.key == (K_s):
					mode="status"
					pressedreal=True
				elif event.key == (K_a):
					mode="message"
					pressedreal=True
				elif event.key == (K_h):
					mode="medical"
					pressedreal=True
				elif event.key == (K_q):
					libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
					pressedreal=True
				elif event.key == (K_LEFTBRACKET) and player.x==planet[current_planet].tiles[0][0][current_floor].stair[0] and player.y==planet[current_planet].tiles[0][0][current_floor].stair[1]:

					message("downcf is "+str(current_floor))
					current_floor+=1
					if len(planet[current_planet].floor_visited)<current_floor+1:
						planet[current_planet].floor_visited.append(False)
					console_write("/n\ncff"+str(current_floor))
					if planet[current_planet].floor_visited[current_floor]==False:	
						mappend=[[Tile(True, "none","none","none") for x in xrange(2)]
							for y in xrange(screen_width-1)]
						planet[current_planet].tiles.append(mappend)
						console_write(len(planet[current_planet].tiles))		
						make_ground_map()
						make_all_enemies_on_floor(5)	
					player.x=planet[current_planet].tiles[0][0][current_floor].stairu[0]
					player.y=planet[current_planet].tiles[0][0][current_floor].stairu[1]
					planet[current_planet].floor_visited[current_floor]=True
					pressedreal=True
				elif event.key == (K_RIGHTBRACKET) and player.x==planet[current_planet].tiles[0][0][current_floor].stairu[0] and player.y==planet[current_planet].tiles[0][0][current_floor].stairu[1]:
					console_write("upcf is "+str(current_floor))
					message("upcf is "+str(current_floor))
					current_floor-=1
					if current_floor>=0:
			
						if planet[current_planet].floor_visited[current_floor]==False:
							make_ground_map()
							make_all_enemies_on_floor(5)	
						player.x=planet[current_planet].tiles[0][0][current_floor].stair[0]
						player.y=planet[current_planet].tiles[0][0][current_floor].stair[1]
						planet[current_planet].floor_visited[current_floor]=True
					elif current_floor<0:
						print("YAAAAAAAAAAAAAAAAAAAAS")
						mode="space"
					pressedreal=True
				elif event.key == (K_p):
					pressedreal=True
					for i in range(len(chemicals)-1):
						if len(chemicals)-1>=i and player.x==chemicals[i].x and player.y==chemicals[i].y and chemicals[i].floor==current_floor and chemicals[i].planet==current_planet:
							inventory.append(chemicals[i])
							chemicals[i].taken=True
							message("Picked up "+str(chemicals[i].name))
							del chemicals[i]
					for weapon in weapons:
						if weapon.x==player.x and weapon.y==player.y and weapon.floor==current_floor and weapon.planet==current_planet:
							inventory.append(weapon)
							weapon.x=None
							weapon.y=None
							message("Picked up a weapon of strength "+str(weapon.strength))
					for larmour in armours:
						if larmour.x==player.x and larmour.y==player.y and larmour.floor==current_floor and larmour.planet==current_planet:
							inventory.append(larmour)
							larmour.x=None
							larmour.y=None
							message("Picked up armour of strength "+str(larmour.strength))
					if planet[current_planet].tiles[player.x][player.y][current_floor].dec!=None:
						if isinstance(planet[current_planet].tiles[player.x][player.y][current_floor].dec, cPlant):
							for q in range(len(planet[current_planet].tiles[player.x][player.y][current_floor].dec.percent_of_obtain)):
								if planet[current_planet].tiles[player.x][player.y][current_floor].dec.percent_of_obtain[q]>random.randint(0,99):
									inventory.append(planet[current_planet].tiles[player.x][player.y][current_floor].dec.harvest_item[q])
						planet[current_planet].tiles[player.x][player.y][current_floor].dec=None
				elif event.key == (K_z):
					ground_draw(True)
					done_shooting=False
					message("SHOOTING MODE IS ACTIVE")
					while(done_shooting==False):
							
							
						for event in pygame.event.get():
							if event.type==KEYDOWN:
								if event.key == (K_UP):
				
									done_shooting=True
									shooting(player.x, player.y, 0,0-1)
								elif event.key == (K_DOWN):
									shooting(player.x, player.y, 0,1)
									done_shooting=True
								elif event.key ==(K_RIGHT):
									shooting(player.x, player.y, 1,0)
									done_shooting=True
								elif event.key == (K_LEFT):
									done_shooting=True
									shooting(player.x, player.y, 0-1,0)
									done_shooting=True
								elif event.key == (K_x):
									done_shooting=True
					pressedreal=True
				elif event.key == (K_t):
					DISPLAYSURF.fill((255,255,255))
					currentselection=0
					slection=None
					while slection==None:
						pygame.display.update()
			
						DISPLAYSURF.fill((255,255,255))
						for i in xrange(len(inventory)):
		
							if i==currentselection:
								clor=BLACK
				
							else:
								clor=GREY
			
							tlvt=inventory[i].strength
							if isinstance(inventory[i],Weapon):
								console_put_char_ex(0,i,"hack/sword.png")
							if isinstance(inventory[i],Armor):
								console_put_char_ex(0,i,shield)
							if isinstance(inventory[i], Chemical):
								if inventory[i].name=="arbinal":
									console_put_char_ex(0,i,chemo)
								elif inventory[i].name=="gaddin":
									console_put_char_ex(0,i,chemt)
								elif inventory[i].name=="branyl":
									console_put_char_ex(0,i,chemth)
								elif inventory[i].name=="resdin":
									console_put_char_ex(0,i,chemf)
								elif inventory[i].name=="chestin":
									console_put_char_ex(0,i,chemfi)
								elif inventory[i].name=="narkinal":
									console_put_char_ex(0,i,chems)
								elif inventory[i].name=="flattle":
									console_put_char_ex(0,i,chemse)
								else:
									console_put_char_ex(0,i, gen_chem)
							if isinstance(inventory[i],Armor) or isinstance(inventory[i],Weapon):
				
								if inventory[i].number>1:
									console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"] with strength of "+str(tlvt),clor,WHITE)
								else:
									console_print(1,i,inventory[i].name+" with strength of "+str(tlvt),clor,WHITE)
							else:
								if inventory[i].number>1:
									console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"]",clor,WHITE)
								else:
									console_print(1,i,inventory[i].name,clor,WHITE)
		
						key = libtcod.console_wait_for_keypress(False)
		
						if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
							currentselection-=1
						elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
							currentselection+=1
			
						elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
				
								slection=inventory[currentselection].name
								inventory[currentselection].number-=1
						elif key.c==ord("z"):
				
								slection=0
		
		
			
	
		
					ground_draw(True)
					done_shooting=False
					message("THROWING MODE IS ACTIVE")
					while(done_shooting==False) and slection!=0:
						key=libtcod.console_wait_for_keypress(True)
						if libtcod.console_is_key_pressed(libtcod.KEY_UP):
				
							done_shooting=True
							throwing(slection,player.x, player.y, 0,0-1)
						elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
							throwing(slection,player.x, player.y, 0,1)
							done_shooting=True
						elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
							throwing(slection,player.x, player.y, 1,0)
							done_shooting=True
						elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
							done_shooting=True
							throwing(slection,player.x, player.y, 0-1,0)
						elif key.c==ord("z"):
							done_shooting=True
				elif event.key == (K_PERIOD):
					message("waited")
	
				elif event.key == (K_g):
					DISPLAYSURF.fill((255,255,255))
					currentselection=0
					slection=None
					while slection==None:
						pygame.display.update()
			
						DISPLAYSURF.fill((255,255,255))
						for i in xrange(len(inventory)):
		
							if i==currentselection:
								clor=BLACK
				
							else:
								clor=GREY
			
							tlvt=inventory[i].strength
							if isinstance(inventory[i],Weapon):
								console_put_char_ex(0,i,"hack/sword.png")
							if isinstance(inventory[i],Armor):
								console_put_char_ex(0,i,shield)
							if isinstance(inventory[i], Chemical):
								if inventory[i].name=="arbinal":
									console_put_char_ex(0,i,chemo)
								elif inventory[i].name=="gaddin":
									console_put_char_ex(0,i,chemt)
								elif inventory[i].name=="branyl":
									console_put_char_ex(0,i,chemth)
								elif inventory[i].name=="resdin":
									console_put_char_ex(0,i,chemf)
								elif inventory[i].name=="chestin":
									console_put_char_ex(0,i,chemfi)
								elif inventory[i].name=="narkinal":
									console_put_char_ex(0,i,chems)
								elif inventory[i].name=="flattle":
									console_put_char_ex(0,i,chemse)
								else:
									console_put_char_ex(0,i, gen_chem)
							if isinstance(inventory[i],Armor) or isinstance(inventory[i],Weapon):
				
								if inventory[i].number>1:
									console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"] with strength of "+str(tlvt),clor,WHITE)
								else:
									console_print(1,i,inventory[i].name+" with strength of "+str(tlvt),clor,WHITE)
							else:
								if inventory[i].number>1:
									console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"]",clor,WHITE)
								else:
									console_print(1,i,inventory[i].name,clor,WHITE)
		
						key = libtcod.console_wait_for_keypress(False)
		
						if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
							currentselection-=1
						elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
							currentselection+=1
			
						elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
				
								slection=inventory[currentselection].name
								inventory[currentselection].number-=1
						elif key.c==ord("z"):
				
								slection=0
		
		
			
	
		
					ground_draw(True)
					done_shooting=False
					message("THROWING MODE IS ACTIVE")
					while(done_shooting==False) and slection!=0:
						key=libtcod.console_wait_for_keypress(True)
						if libtcod.console_is_key_pressed(libtcod.KEY_UP):
				
							done_shooting=True
							planting(slection,player.x, player.y, 0,0-1)
						elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
							planting(slection,player.x, player.y, 0,1)
							done_shooting=True
						elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
							planting(slection,player.x, player.y, 1,0)
							done_shooting=True
						elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
							done_shooting=True
							planting(slection,player.x, player.y, 0-1,0)
						elif key.c==ord("z"):
							done_shooting=True
				elif event.key == (K_PERIOD):
					message("waited")
	
	
	
				
	
				else:
					handle_keys()
	
				
	
		
	

#makes the map for the ground
def make_ground_map():
	global longest, longest_name, planet, chemicals,roomnum,player
	roomnum=0
	chemicals=[]
	for x in range(screen_width-1):
		for y in range(screen_width-1):
			while len(planet[current_planet].tiles[x][y])<current_floor+1:
				planet[current_planet].tiles[x][y].append(Tile(True, "none","none","none"))
	
	general_variable=0
	
	stx=random.randint(0,screen_width-2)
	sty=random.randint(0,screen_width-2)
	
	planet[current_planet].tiles[0][0][current_floor].stairu=[stx,sty]
	new_x=planet[current_planet].tiles[0][0][current_floor].stairu[0]
	new_y=planet[current_planet].tiles[0][0][current_floor].stairu[1]
	new_x_two=planet[current_planet].tiles[0][0][current_floor].stairu[0]
	new_y_two=planet[current_planet].tiles[0][0][current_floor].stairu[1]
	start=time.clock()
	
	
	while general_variable<6:
		x=random.randint(2,screen_width-3)
		y=random.randint(2,screen_width-3)
		x_two=random.randint(2, screen_width-3)
		y_two=random.randint(2,screen_width-3)
		xt=max(x,x_two)
		xo=min(x,x_two)
		yt=max(y,y_two)
		yo=min(y,y_two)
		x=xo
		x_two=xt
		y=yo
		y_two=yt
	
		returnval=False
		for u in range(x_two-x):
			
			
			for v in range(y_two-y):
				
				
				
				if planet[current_planet].tiles[u+x][v+y][current_floor].blocked==False:
					
					returnval=True
		while returnval==True:
		
			x=random.randint(2,screen_width-3)
			y=random.randint(2,screen_width-3)
			x_two=random.randint(2, screen_width-3)
			y_two=random.randint(2,screen_width-3)
			xt=max(x,x_two)
			xo=min(x,x_two)
			yt=max(y,y_two)
			yo=min(y,y_two)
			x=xo
			x_two=xt
			y=yo
			y_two=yt
			returnval=False
			for u in range(x_two-x):
				
				for v in range(y_two-y):
					
					
					if planet[current_planet].tiles[u+x][v+y][current_floor].blocked==False:
						
						returnval=True
		
		make_room(x, x_two, y, y_two)
			
		
        
        
		make_passage(new_x_two, x, new_y_two, "x")
		make_passage(new_x_two, y, x, "y")
        
        
		new_x=x
		new_y=y
		new_x_two=x_two
		new_y_two=y_two
		general_variable+=1
		roomnum+=1
		
		if general_variable==5:
			stx=random.randint(x,x_two)
			sty=random.randint(y,y_two)
			while planet[current_planet].tiles[stx][sty][current_floor].blocked==True:
				stx=random.randint(x,x_two)
				sty=random.randint(y,y_two)
			
			planet[current_planet].tiles[0][0][current_floor].stair=[stx,sty]
	
	
	end=time.clock()
	if (end-start)>longest:
		longest_name="make ground map"
		longest=end-start
	
	
	while planet[current_planet].tiles[planet[current_planet].tiles[0][0][current_floor].stairu[0]][planet[current_planet].tiles[0][0][current_floor].stairu[1]][current_floor].blocked==True:
		planet[current_planet].tiles[0][0][current_floor].stairu=[random.randint(2, screen_width-1),random.randint(2,screen_width-1)]
	while planet[current_planet].tiles[planet[current_planet].tiles[0][0][current_floor].stair[0]][planet[current_planet].tiles[0][0][current_floor].stair[1]][current_floor].blocked==True:
		planet[current_planet].tiles[0][0][current_floor].stair=[random.randint(2, screen_width-1),random.randint(2,screen_width-1)]
	if planet[current_planet].theme.shape=="cave":
		cellular_automata_generator()
	if planet[current_planet].theme.name=="normal":
		for x in range(screen_width-1):
			for y in range(screen_width-1):
				if planet[current_planet].tiles[x][y][current_floor].blocked==False and random.randint(0,3)==0:
					planet[current_planet].tiles[x][y][current_floor].dec=random.choice(plants)
		for x in range(random.randint(0,10)):
			xcoor=random.randint(2,screen_width-2)
			ycoor=random.randint(2,screen_width-2)
			while planet[current_planet].tiles[xcoor][ycoor][current_floor].blocked==True:
				xcoor=random.randint(2,screen_width-2)
				ycoor=random.randint(2,screen_width-2)
			planet[current_planet].tiles[xcoor][ycoor][current_floor].liq=Liquid("water",1,random.randint(1,50))
			
		for x in range(9):
			liquid_move()
	for x in range(0):
		eliminate_deadends()
	for x in range(chemicals_made):
		typechem=random.randint(0,6)
		chemx=random.randint(2,screen_width-2)
		chemy=random.randint(2,screen_width-2)
		while planet[current_planet].tiles[chemx][chemy][current_floor].blocked==True:
			chemx=random.randint(2,screen_width-2)
			chemy=random.randint(2,screen_width-2)
		if typechem==0:
			chemicals.append(Chemical("gaddin",1,1,chemx,chemy))
		elif typechem==1:
			chemicals.append(Chemical("arbinal",1,1,chemx,chemy))
		elif typechem==2:
			chemicals.append(Chemical("branyl",1,1,chemx,chemy))
		elif typechem==3:
			chemicals.append(Chemical("resdin",1,1,chemx,chemy))
		elif typechem==4:
			chemicals.append(Chemical("chestin",1,1,chemx,chemy))
		elif typechem==5:
			chemicals.append(Chemical("narkinal",1,1,chemx,chemy))
		elif typechem==6:
			chemicals.append(Chemical("flattle",1,1,chemx,chemy))
def cellular_automata_generator():
	for x in range(screen_width-1):
		for y in range(screen_width-1):
			if random.randint(0,99)<50:
				planet[current_planet].tiles[x][y][current_floor].blocked=False
			else:
				planet[current_planet].tiles[x][y][current_floor].blocked=True
	
	for p in range(20):
		#pygame.display.update()
		#time.sleep(0.5)
		for x in range(screen_width-1):
			for y in range(screen_width-1):
				
				
				if planet[current_planet].tiles[x][y][current_floor].blocked==True:
					#console_put_char_ex(x,y,postapocground)
					neighbors=0
					if x-2<0 or planet[current_planet].tiles[x-1][y][current_floor].blocked==True:
						neighbors+=1
					if x-3<0 or planet[current_planet].tiles[x-2][y][current_floor].blocked==True:
						neighbors+=0.5
					if  x-2<0 or y+2>screen_width-1 or planet[current_planet].tiles[x-1][y+1][current_floor].blocked==True:
						neighbors+=0.5
					if  x+2>screen_width-1 or planet[current_planet].tiles[x+1][y][current_floor].blocked==True:
						neighbors+=1
					if  x+3>screen_width-1 or planet[current_planet].tiles[x+2][y][current_floor].blocked==True:
						neighbors+=0.5
					if  x+2>screen_width-1 or y-2<0 or planet[current_planet].tiles[x+1][y-1][current_floor].blocked==True:
						neighbors+=0.5
					if  y-2<0 or planet[current_planet].tiles[x][y-1][current_floor].blocked==True:
						neighbors+=1
					if  y-3<0 or planet[current_planet].tiles[x][y-2][current_floor].blocked==True:
						neighbors+=0.5
					if  y-2<0 or  x-2<0 or planet[current_planet].tiles[x-1][y-1][current_floor].blocked==True:
						neighbors+=0.5
					if  y+2>screen_width-1 or planet[current_planet].tiles[x][y+1][current_floor].blocked==True:
						neighbors+=1
					if  y+3>screen_width-1 or planet[current_planet].tiles[x][y+2][current_floor].blocked==True:
						neighbors+=0.5
					if  y+2>screen_width-1 or x+2>screen_width-1 or planet[current_planet].tiles[x+1][y+1][current_floor].blocked==True:
						neighbors+=0.5
					if  neighbors<3:
						planet[current_planet].tiles[x][y][current_floor].blocked=False
				#else:
					#console_put_char_ex(x,y,postapocwall)
				
#handles the space controls
def handle_spacekey():
	
	global longest, longest_name
	global spacex, spacey, mode
	global placex, placey
	returning=False
	console_write("(((((((("+str(longest)+"longest "+longest_name+"))))))))")
	
	message("Your acceleration is at "+str(placex)+", "+str(placey))
	message("Your location is at "+str(spacex)+", "+str(spacey))
	pressedreal=False
	while pressedreal==False:
		for event in pygame.event.get():
			if event.type==KEYDOWN:
				
				if event.key == (K_UP):
					placey -= 1
					pressedreal=True
				elif event.key == (K_DOWN):
					placey += 1
					pressedreal=True
				elif event.key == (K_LEFT):
					placex -= 1
					pressedreal=True
				elif event.key == (K_RIGHT):
					placex += 1
					pressedreal=True
				elif event.key == (K_d):
					mode="incinerate"
					pressedreal=True
				elif event.key == (K_i):
					mode="space_inventory1"
					pressedreal=True
				elif event.key == (K_l):
					returning= True
				elif  event.key == (K_z):
					space_draw()
					done_shooting=False
					message("SHOOTING MODE IS ACTIVE")
					while(done_shooting==False):
						libtcod.console_wait_for_keypress(True)
			
						done_shooting=True
						space_shooting(placex,placey)
					pressedreal=True
					pressedreal=True
		
				pressedreal=True
	top_left[0]+=placex
	bottom_right=[top_left[0]+49,top_left[1]+49]
	top_left[1]+=placey
	bottom_right=[top_left[0]+49,top_left[1]+49]
	print("foist"+str(spacex))
	spacex+=placex
	spacey+=placey
	print("sec"+str(spacex))
	#if key.c==ord("z"):
		#space_draw()
		#done_shooting=False
		#message("SHOOTING MODE IS ACTIVE")
		#while(done_shooting==False):
			#libtcod.console_wait_for_keypress(True)
			
			#done_shooting=True

	#if key.vk == libtcod.KEY_ENTER and key.lalt:
		#libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
	
	#elif key.vk == libtcod.KEY_ESCAPE:
		#return True
	return returning
def ground_draw(shooting_mode):
	global player, longest, longest_name,screen_width
	player.max_health=100
	libtcod.map_compute_fov(fov_map, player.x,player.y,0,light_walls=True,algo=libtcod.FOV_DIAMOND)
	DISPLAYSURF.fill((0,0,0))
	
	for x in range(screen_width-1):
		for y in range(screen_width-1):
			if y<screen_width-1 and x<screen_width-1:
				if planet[current_planet].tiles[x][y][current_floor].blocked==True:
						
					libtcod.map_set_properties(fov_map,x,y,False,False)
			
				else:
						
					libtcod.map_set_properties(fov_map,x,y,True,True)
	
	start=time.clock()
	for x in range(screen_width-2):
		rat_s=(screen_width)/(x+0.001)
		rat_h=(float(player.max_health)/float(player.health)+0.00001)
		
		if rat_s >rat_h :
			console_put_char_ex (x+1,screen_width,redc)
		else:
			console_put_char_ex (x+1,screen_width,bluec)
	console_put_char_ex (0,screen_width,full_h_f)
	if player.health==player.max_health:
		console_put_char_ex (screen_width-1,screen_width,full_h)
	else:
		console_put_char_ex (screen_width-1,screen_width,empty_h)
	console_print (1,screen_width,"You are at "+str(player.health)+"/"+str(player.max_health)+" health",WHITE,BLACK)
	for x in range(screen_width-2):
		rat_s=(screen_width)/(x+0.001)
		rat_h=(float(100))/(float(player.hunger)+0.00001)
		
		if rat_s >rat_h :
			console_put_char_ex (x+1,screen_width+1,green)
		else:
			console_put_char_ex (x+1,screen_width+1,bluec)
	console_put_char_ex (0,screen_width+1,hung_f)
	if player.hunger==100:
		console_put_char_ex (screen_width-1,screen_width+1,hung)
	else:
		console_put_char_ex (screen_width-1,screen_width+1,empty_h)
	console_print (1,screen_width+1,"You are at "+str(player.hunger)+"/"+str(100)+" hunger",WHITE,BLACK)
	if check_for_status_effect("blind")!=True:
		for x in xrange(screen_width-1):
			for y in xrange(screen_width-1):
				
				for chemical in chemicals:
					if libtcod.map_is_in_fov(fov_map,chemical.x,chemical.y) and chemical.taken==False and chemical.floor==current_floor and chemical.planet==current_planet:
						if chemical.name=="arbinal":
							console_put_char_ex(chemical.x, chemical.y, chemo)
						elif chemical.name=="gaddin":
							console_put_char_ex(chemical.x, chemical.y, chemt)
						elif chemical.name=="branyl":
							console_put_char_ex(chemical.x, chemical.y, chemth)
						elif chemical.name=="resdin":
							console_put_char_ex(chemical.x, chemical.y, chemf)
						elif chemical.name=="chestin":
							console_put_char_ex(chemical.x, chemical.y, chemfi)
						elif chemical.name=="narkinal":
							console_put_char_ex(chemical.x, chemical.y, chems)
						elif chemical.name=="flattle":
							console_put_char_ex(chemical.x, chemical.y, chemse)
						
				for weapon in weapons:
				
					if hasattr(weapon,"x") and libtcod.map_is_in_fov(fov_map,weapon.x,weapon.y) and weapon.floor==current_floor and weapon.planet==current_planet and weapon.x!=None and weapon.y!=None:
						console_put_char_ex(weapon.x,weapon.y,sword)
				for larmour in armours:
					if hasattr(larmour,"x") and libtcod.map_is_in_fov(fov_map,larmour.x,larmour.y) and larmour.floor==current_floor and larmour.planet==current_planet  and larmour.x!=None and larmour.y!=None:
						console_put_char_ex(larmour.x,larmour.y,shield)
				
				if player.health>0 and libtcod.map_is_in_fov(fov_map,x,y):
					#
					
					if planet[current_planet].tiles[x][y][current_floor].theme_type==0:
						console_put_char_ex(x, y, planet[current_planet].theme.ground_tile)
					else:
						console_put_char_ex(x, y, planet[current_planet].theme.secondary_ground_tile)
					if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect!=None and planet[current_planet].tiles[x][y][current_floor].status_effect.effect=="fire":
						console_put_char_ex(x, y, fire)
					
					if planet[current_planet].tiles[x][y][current_floor].dec!=None:
						
						console_put_char_ex(x, y, planet[current_planet].tiles[x][y][current_floor].dec.texture)
							
				if planet[current_planet].tiles[x][y][current_floor].blocked==True and player.health>0 and libtcod.map_is_in_fov(fov_map,x,y):
					#
					libtcod.console_set_default_foreground(0, libtcod.white)
					
					console_put_char_ex(x,y,planet[current_planet].theme.wall_tile)
				
				libtcod.console_set_default_foreground(0, libtcod.white)
				
				for critter in creature[current_planet][current_floor]:
				
					if libtcod.map_is_in_fov(fov_map,critter.x,critter.y):
						critter.draw()
			
				if shooting_mode==False:
					console_put_char_ex(player.x, player.y, playerp)
				if shooting_mode==True:
				
					console_put_char_ex(player.x, player.y, shooting_player)
				if planet[current_planet].tiles[x][y][current_floor].liq!=None  and libtcod.map_is_in_fov(fov_map,x,y):
					
					if planet[current_planet].tiles[x][y][current_floor].liq.depth<4:
						console_put_char_ex(x,y,water[planet[current_planet].tiles[x][y][current_floor].liq.depth-1])
						
					else:
						console_put_char_ex(x,y,water[3])
				if x==planet[current_planet].tiles[0][0][current_floor].stair[0] and y==planet[current_planet].tiles[0][0][current_floor].stair[1] and libtcod.map_is_in_fov(fov_map,x,y):
					console_put_char_ex(x, y, downstair)
				if x==planet[current_planet].tiles[0][0][current_floor].stairu[0] and y==planet[current_planet].tiles[0][0][current_floor].stairu[1] and libtcod.map_is_in_fov(fov_map,x,y):
					console_put_char_ex(x, y, upstair)
	else:
		DISPLAYSURF.fill((0,0,0))
	if player.health<=0:
		for x in xrange(screen_width-1):
			for y in xrange(screen_width-1):
				
				console_print(x, y, random.choice(["D","E","A","D"]), WHITE,BLACK)
	message_display()			
	#for p in range(roomnum+1):
		#color=libtcod.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		#for x in range(screen_width-1):
			#for y in range(screen_width-1):
				#if planet[current_planet].tiles[x][y][current_floor].room==p or planet[current_planet].tiles[x][y][current_floor].room=="passage":
					#libtcod.console_put_char_ex(0, x, y, "#", color, libtcod.black)
	pygame.display.update()
	end=time.clock()
	if (end-start)>longest:
		longest_name="drawn"
		longest=end-start
	
#defines ground gameplay
def groundplay():
	global longest, longest_name,planet, player_radioactivity, chemicals,current_floor,current_planet, mode
	global player, player,weapons,armours
	print(weapons)
	print(str(current_planet)+"CW IS = "+str(planet[current_planet].theme.name))
	player.hunger+=1
	if player.hunger>=100:
		player.health=0-1
	for wound in player.wounds:
		if wound.subtracted==False:
			player.max_health-=wound.loss
			wound.subtracted=True
	if player.health>player.max_health:
		player.health=player.max_health
	print("THE CURRENT FLOOR IS"+str(current_floor))
	if current_floor<0:
		current_floor=0
	
	console_write("((s))"+str(longest)+longest_name+"((e))")
	
	ground_draw(False)
	start=time.clock()
	for leffect in range(len(player_status_effects)):
		
		print("asd"+str(player_status_effects[leffect]))
		
		thing=player_status_effects[leffect].effect
		if thing=="poison":
			player.health=int(player.health*player_status_effects[leffect].power)
		player_status_effects[leffect].decay-=1
		print("dec="+str(player_status_effects[leffect].decay))
		if player_status_effects[leffect].decay<1:
			print("EEHEHEHEJFDHSKLFHSK")
			
			del player_status_effects[leffect]
	
	if player.x==0 and player.y==0:
		player.y=planet[current_planet].tiles[0][0][current_floor].stair[1]
		player.x=planet[current_planet].tiles[0][0][current_floor].stair[0]
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			if planet[current_planet].tiles[x][y][current_floor].liq!=None:
				print(planet[current_planet].tiles[x][y][current_floor].liq.type)
				if planet[current_planet].tiles[x][y][current_floor].liq.depth>1 and random.randint(1,planet[current_planet].tiles[x][y][current_floor].liq.inertia)==1:
					if x+2<=screen_width-1 and planet[current_planet].tiles[x+1][y][current_floor].liq!=None and planet[current_planet].tiles[x+1][y][current_floor].blocked==False and planet[current_planet].tiles[x+1][y][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or x+2<=screen_width-1 and planet[current_planet].tiles[x+1][y][current_floor].liq==None:
						if planet[current_planet].tiles[x+1][y][current_floor].liq==None:
							planet[current_planet].tiles[x+1][y][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x+1][y][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
					elif y+2<=screen_width-1 and planet[current_planet].tiles[x][y+1][current_floor].liq !=None and planet[current_planet].tiles[x][y+1][current_floor].blocked==False  and planet[current_planet].tiles[x][y+1][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or y+2<=screen_width-1 and planet[current_planet].tiles[x][y+1][current_floor].liq==None:
						if planet[current_planet].tiles[x][y+1][current_floor].liq==None:
							planet[current_planet].tiles[x][y+1][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x][y+1][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
					elif x-2>=1 and planet[current_planet].tiles[x-1][y][current_floor].liq!=None  and planet[current_planet].tiles[x-1][y][current_floor].blocked==False and planet[current_planet].tiles[x-1][y][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or x-2>=1 and planet[current_planet].tiles[x-1][y][current_floor].liq==None:
						if planet[current_planet].tiles[x-1][y][current_floor].liq==None:
							planet[current_planet].tiles[x-1][y][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x-1][y][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
					elif y-2<=screen_width-1 and planet[current_planet].tiles[x][y-1][current_floor].liq!=None and planet[current_planet].tiles[x][y-1][current_floor].blocked==False and planet[current_planet].tiles[x][y-1][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or y-2<=screen_width-1 and planet[current_planet].tiles[x][y-1][current_floor].liq==None:
						if planet[current_planet].tiles[x][y-1][current_floor].liq==None:
							planet[current_planet].tiles[x][y-1][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x][y-1][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
			if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect!=None and planet[current_planet].tiles[x][y][current_floor].status_effect !=0:
				planet[current_planet].tiles[x][y][current_floor].dec=None
				planet[current_planet].tiles[x][y][current_floor].theme_type=1
				planet[current_planet].tiles[x][y][current_floor].status_effect.decay-=1
				if planet[current_planet].tiles[x][y][current_floor].status_effect.decay <=0:
					del(planet[current_planet].tiles[x][y][current_floor].status_effect)
				if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect.effect=="fire":
					if x ==player.x and y ==player.y:
						player.health=int(player.health/2)
						
						player.wounds.append(Wound("burn",int(0.33*player.max_health)))
					print(str(x)+","+str(y)+" is on fire")
					tivt=random.randint(0,1)
					if tivt==0:
						planet[current_planet].tiles[x][y][current_floor].blocked=False
					else:
						
						direction=random.choice(["up","down","left","right"])
						print(direction)
						if direction=="up" and y+1<screen_width-2:
							planet[current_planet].tiles[x][y+1][current_floor].status_effect=status_effect("fire", 3,1)
							
						if direction=="down" and y-1>0:
							planet[current_planet].tiles[x][y-1][current_floor].status_effect=status_effect("fire", 3,1)
						if direction=="left" and x-1>0:
							planet[current_planet].tiles[x-1][y][current_floor].status_effect=status_effect("fire", 3,1)
						if direction=="right" and x+1<screen_width-2:
							planet[current_planet].tiles[x+1][y][current_floor].status_effect=status_effect("fire", 3,1)
	end=time.clock()
	if (end-start)>longest:
		longest_name="fov_set"
		longest=end-start
	start=time.clock()
	for i in range(len(inventory)):
		for z in range(len(inventory)):
			if len(inventory)-1>=i and len(inventory)-1>=z and inventory[i].name==inventory[z].name and i!=z:
				inventory[i].number+=1
				del inventory[z]
	
	end=time.clock()
	if (end-start)>longest:
		longest_name="check if player is on weapon"
		longest=end-start		
	start=time.clock()
	if player_radioactivity>0:
		player.health=player.health-(player_radioactivity)
	player_radioactivity=int(player_radioactivity/2)
	
	ground_draw(False)
	end=time.clock()
	if (end-start)>longest:
		longest_name="armour if player is on"
		longest=end-start
	
	start=time.clock()
	
	
	
	end=time.clock()
	if (end-start)>longest:
		longest_name="stat effect test"
		longest=end-start		
	
	sleep=False
	for fect in player_status_effects:
		if fect.effect=="sleep":
			sleep=True
			
	if sleep!=True:	
		exit=handle_keys()
	
	
	console_write(longest_name)
	
	look(libtcod.mouse_get_status().cx,libtcod.mouse_get_status().cy)
	
	for i in range(len(creature[current_planet][current_floor])):
		start=time.clock()
		if i<=len(creature[current_planet][current_floor])-1:
			if hasattr(planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor],"status_effect") and planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].status_effect!=None and planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].status_effect.effect=="fire":
				creature[current_planet][current_floor][i].status_effects.append(status_effect("fire",3,1))
			console_write("weenus")
			while len(creature[current_planet][current_floor][i].status_effects)>5:
				del(creature[current_planet][current_floor][i].status_effects[0])
			for other_critter in creature[current_planet][current_floor]:
			
				for fect in creature[current_planet][current_floor][i].status_effects:
				
					if fect.effect=="fire":
						if creature[current_planet][current_floor][i].type!="flame-being":
							creature[current_planet][current_floor][i].health_points-=1
						if creature[current_planet][current_floor][i].x==other_critter.x:
							if creature[current_planet][current_floor][i].y-1>2 and creature[current_planet][current_floor][i].y-1==other_critter.y:
								other_critter.status_effects.append(status_effect("fire",3,1))
							if creature[current_planet][current_floor][i].y+1<screen_width-2 and creature[current_planet][current_floor][i].y+1==other_critter.y:
								other_critter.status_effects.append(status_effect("fire",3,1))
						if creature[current_planet][current_floor][i].y==other_critter.y:
							if creature[current_planet][current_floor][i].x-1>2 and creature[current_planet][current_floor][i].x-1==other_critter.x:
								other_critter.status_effects.append(status_effect("fire",3,1))
							if creature[current_planet][current_floor][i].x+1<screen_width-2 and creature[current_planet][current_floor][i].x+1==other_critter.x:
								other_critter.status_effects.append(status_effect("fire",3,1))
			end=time.clock()
			if (end-start)>longest:
				longest_name="movin enemies"
				longest=end-start
			for fect in creature[current_planet][current_floor][i].status_effects:
				for fectt in creature[current_planet][current_floor][i].status_effects:
					if fect.effect==fectt.effect:
						del fectt
			if creature[current_planet][current_floor][i].type=="flame-being":
				planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].status_effect=status_effect("fire",3,1)
			if creature[current_planet][current_floor][i].health_points>0  and current_planet==creature[current_planet][current_floor][i].planet and current_floor==creature[current_planet][current_floor][i].floor:
				if creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y ==player.y:
					creature[current_planet][current_floor][i].health_points-=current_weapon.strength
					
				creature[current_planet][current_floor][i].goal_x_coordinate=player.x
				creature[current_planet][current_floor][i].goal_y_coordinate=player.y
				dorg=0
				if player.health>0:
					dorg=creature[current_planet][current_floor][i].go()
			
				if dorg=="x":	
					creature[current_planet][current_floor][i].move(1,0)
			
				elif dorg=="-x":
					creature[current_planet][current_floor][i].move(-1,0)
			
				elif dorg=="y":
					creature[current_planet][current_floor][i].move(0,1)
			
				elif dorg=="-y":
					creature[current_planet][current_floor][i].move(0,-1)
				if creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y and i<=len(creature[current_planet][current_floor])-1:
					message(creature[current_planet][current_floor][i].name+" did "+str(creature[current_planet][current_floor][i].health_points-current_armor.strength)+" damage to the player")
					player.health-=creature[current_planet][current_floor][i].skill_level-current_armor.strength
				
					player.wounds.append(Wound("scratch",int(0.1*player.max_health)))
					
				
				if dorg=="x" and creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y:	
					creature[current_planet][current_floor][i].move(-1,0)
			
				elif dorg=="-x" and creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y:
					creature[current_planet][current_floor][i].move(1,0)
			
				elif dorg=="y" and creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y:
					creature[current_planet][current_floor][i].move(0,-1)
			
				elif dorg=="-y" and creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y:
					creature[current_planet][current_floor][i].move(0,1)
				if player.y+1<screen_width-2 and creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y+1 and player_radioactivity>50:
					creature[current_planet][current_floor][i].health_points-=(player_radioactivity-50)
					
				elif player.x-1>2 and creature[current_planet][current_floor][i].x==player.x-1 and creature[current_planet][current_floor][i].y==player.y and player_radioactivity>50:
					creature[current_planet][current_floor][i].health_points-=(player_radioactivity-50)
					
				elif player.x+1<screen_width-2 and creature[current_planet][current_floor][i].x==player.x+1 and creature[current_planet][current_floor][i].y==player.y and player_radioactivity>50:
					creature[current_planet][current_floor][i].health_points-=(player_radioactivity)
					
				elif player.y-1>2 and creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y-1 and player_radioactivity>50:
					creature[current_planet][current_floor][i].health_points-=(player_radioactivity)
					
			
		
			if creature[current_planet][current_floor][i].health_points<0  and current_planet==creature[current_planet][current_floor][i].planet and current_floor==creature[current_planet][current_floor][i].floor:
				monster_death(creature[current_planet][current_floor][i].x,creature[current_planet][current_floor][i].y)
			
				
				del creature[current_planet][current_floor][i]
			
			
	if sleep!=True and exit==True:
		return True
	end=time.clock()
	if (end-start)>longest:
		longest_name="movin enemies"
		longest=end-start		
	ground_draw(False)
	
	
		
for x in range(number_of_planets):
	
	planet.append(Planet(random.randint(-100,100),random.randint(-100,100),False,0,0,monster_name()[1],random.choice(themes) ))
	print("the planet"+str(x)+" at "+str(planet[x].x)+", "+str(planet[x].y)+" is "+planet[x].theme.name)
def message(message):
	global messages, player
	messages[0]=messages[1]
	messages[1]=messages[2]
	messages[2]=messages[3]
	messages[3]=message
	message_log.append(message)
def message_display():
	global messages, player
	
	first_blank=True
	
	for i in xrange(4):	
		console_print(0,screen_width+i+2,"                                                                         ",WHITE,BLACK)
		console_print (0,screen_width+i+2,messages[i],WHITE,BLACK)
			
			
			
		pygame.display.update()
	
def space_draw():
	
	DISPLAYSURF.fill((0,0,0))
	message_display()
	pygame.display.update()
	
	
	
	

	for x in range(len(starx)):		
				
		
		if stary[x]-top_left[1]<screen_width-1 and starx[x]<bottom_right[0] and stary[x]<bottom_right[1] and starx[x]>top_left[0] and stary[x]>top_left[1]:
				
			console_put_char_ex(starx[x]-top_left[0],stary[x]-top_left[1], star)
	
			
	
	
	
	for x in xrange(number_of_planets):
		
		if planet[x].y-top_left[1]<screen_width-1 and planet[x].x<bottom_right[0] and planet[x].y<bottom_right[1] and planet[x].x>top_left[0] and planet[x].y>top_left[1]:
			if planet[x].theme.name != "space station":
				console_put_char_ex(planet[x].x-top_left[0],planet[x].y-top_left[1], planetp)
			else:
				console_put_char_ex(planet[x].x-top_left[0],planet[x].y-top_left[1], space_station)
	
	#libtcod.console_put_char(0, spacex-top_left[0], spacey-top_left[1], "$", libtcod.BKGND_NONE)
	console_put_char_ex(24, 24, spaceship)
	
			
	
	
	
	pygame.display.update()
#defines how the game plays in space
def spaceplay():
	global planet,mode, player, number_of_planets, spacexmax,spacexmin,spaceymax,spaceymin,current_planet
	global placex, placey
	
	
	space_draw()
	if spacex>spacexmax:
		spacexmax=spacex
	if spacex<spacexmin:
		spacexmin=spacex
	if spacey>spaceymax:
		spaceymax=spacey
	if spacey<spaceymin:
		spacexmax=spacex
	exit=False
	if handle_spacekey():
		for i in xrange(len(planet)):
			if spacex==planet[i].x and spacey==planet[i].y :
				placex=0
				placey=0
				if planet[i].visited==False:
					current_planet=i
					player.x=random.randint(0,screen_width-1)
					player.y=random.randint(0,screen_width-1)
					planet[i].player_x_coordinate=player.x
					planet[i].player_y_coordinate=player.y
					#creates entire map
					current_planet=i
					while len(planet)>len(creature):
						row=[]
					
					
						row.append([[0]])
						creature.append(row)
					console_write(creature)
					make_ground_map()
				
					make_all_enemies_on_floor(10)
			
					make_terrain_types()

				planet[i].visited=True
				current_planet=i
			
				player.x=planet[current_planet].tiles[0][0][current_floor].stairu[0]
				player.y=planet[current_planet].tiles[0][0][current_floor].stairu[1]
			
			
			
				mode="ground"
				for x in xrange (screen_width-1):
					for y in xrange(screen_width-1):
					
						if planet[current_planet].tiles[x][y][current_floor].blocked==True:
							
							libtcod.map_set_properties(fov_map,x,y,False,False)
						else:
						
							libtcod.map_set_properties(fov_map,x,y,True,True)
					
						
	#if spacexmax-50<spacex:
		#for x in range(100):
			#planet.append(Planet(random.randint(spacexmax,spacexmax+100),random.randint(spaceymin,spaceymax),False,0,0,monster_name()[1] ))
			#print(x)
		#spacexmax+=100
	#if spaceymax-50<spacey:
		#for x in range(100):
			#planet.append(Planet(random.randint(spacexmin,spacexmax),random.randint(spaceymax,spaceymax+100),False,0,0,monster_name()[1] ))
			#print(x)
		#spacexmax+=100
	#if spacexmin+50>spacex:
		#for x in range(100):
			#planet.append(Planet(random.randint(spacexmin-100,spacexmin),random.randint(spaceymin,spaceymax),False,0,0,monster_name()[1] ))
			#print(x)
		#spacexmax-=100
	#if spaceymin+50>spacey:
		#for x in range(100):
			#planet.append(Planet(random.randint(spacexmin,spacexmax),random.randint(spaceymin-100,spaceymin),False,0,0,monster_name()[1] ))
			#print(x)
		#spacexmax-=100
	
		
	if exit==True:
			return True
			
#Randomly places the player down. PRE-ALPHA CODE        
def explode(stx,sty,vel):
	
	lent=0
	while vel>0:
		lent+=1
		vel-=1
		for x in range(lent):
			
			planet[current_planet].tiles[stx+x][sty+x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx+x,sty+x):
				console_put_char_ex(stx+x, sty+x, exploder)
			planet[current_planet].tiles[stx-x][sty+x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx-x,sty+x):
				console_put_char_ex( stx-x, sty+x, exploder)
			planet[current_planet].tiles[stx+x][sty-x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx+x,sty-x):
				console_put_char_ex(stx+x, sty-x, exploder)
			planet[current_planet].tiles[stx][sty+x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx,sty+x):
				console_put_char_ex(stx, sty+x, exploder)
			planet[current_planet].tiles[stx+x][sty][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx+x,sty):
				console_put_char_ex(stx+x, sty, exploder)
			planet[current_planet].tiles[stx-x][sty-x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx-x,sty-x):
				console_put_char_ex(stx-x, sty-x, exploder)
			planet[current_planet].tiles[stx][sty-x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx,sty-x):
				console_put_char_ex(stx, sty-x, exploder)
			planet[current_planet].tiles[stx-x][sty][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx-x,sty):
				console_put_char_ex( stx-x, sty, exploder)
			pygame.display.update()
			

placex=0
placey=0


	
creature=[]
def monster_death(x,y):
	global current_floor
	if random.randint(0,1)==0:
		weapons.append(Weapon("weapon"+str(random.randint(0,10000)),random.randint(1,current_floor+1),x,y))
	else:
		armours.append(Armor("armor"+str(random.randint(0,10000)),random.randint(1,current_floor+1),x,y))
	
def make_all_enemies_on_floor(enemies_spawned):
	global creature,current_floor,current_planet
	
	
	
	
	
	for l in range(enemies_spawned):
		
		
			
			
		enemyc=[random.randint(2, screen_width-2), random.randint(2, screen_width-2)]

		while planet[current_planet].tiles[enemyc[0]][enemyc[1]][current_floor].blocked==True:
			enemyc[0]=random.randint(2, screen_width-2)
			enemyc[1]=random.randint(2, screen_width-2)
		while len(creature[current_planet])<current_floor+1:
			creature[current_planet].append([0])
		
		creature[current_planet][current_floor].append(monster(enemyc[0],enemyc[1],player.x,player.y, monster_name()[0],monster_name()[1],random.randint(1,current_floor+4),current_floor,current_planet ))
	
	
	del creature[current_planet][current_floor][0]
	
	
	
def shooting(currentx,currenty, x,y):
	loops=1
	monster_hit=False
	
	while  random.randint(1,loops)<5 and currentx+x<screen_width-1 and currentx+x>=0 and currenty+y>=0 and currenty+y<screen_width-1 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True and monster_hit==False:
		if currentx!=player.x or currenty!=player.y:
			libtcod.console_set_default_foreground(0, libtcod.red)
			if math.fabs(x)> math.fabs(y):	
				console_put_char_ex(currentx,currenty,hor_laser)
			if  math.fabs(y)> math.fabs(x):	
				console_put_char_ex(currentx,currenty,vert_laser)
			libtcod.console_set_default_foreground(0, libtcod.white)
			pygame.display.update()
			time.sleep(0.1)
		loops+=1
		currentx+=x
		currenty+=y
		for i in xrange(len(creature[current_planet][current_floor])):
			
			if creature[current_planet][current_floor][i].x==currentx and creature[current_planet][current_floor][i].y==currenty and creature[current_planet][current_floor][i].health_points>0:
				message(creature[current_planet][current_floor][i].name+" has been hit")
				monster_hit=True
				planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
				if planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True:
					creature[current_planet][current_floor][i].x+=x
					creature[current_planet][current_floor][i].y+=y
				
				creature[current_planet][current_floor][i].health_points-=random.randint(1,5)*(current_weapon.strength)
				
				i=enemies_spawned
	if random.randint(1,loops)<5 and random.randint(1,10)!=1 and currentx+x<screen_width-1 and currentx+x<screen_width-1 and currenty+y<screen_width-1 and currentx+x>=0 and currenty+y>=0 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked==True:
		planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
def space_shooting(x,y):
	global spacex,spacey, planet
	loops=1
	monster_hit=False
	currentx=24
	currenty=24
	while  random.randint(1,loops)<5 and currentx+x<screen_width-1 and currentx+x>=0 and currenty+y>=0 and currenty+y<screen_width-1 and monster_hit==False:
		
		if currentx!=spacex or currenty!=spacey:
			libtcod.console_set_default_foreground(0, libtcod.red)	
			libtcod.console_put_char(0,currentx,currenty,"~", libtcod.BKGND_NONE)
			libtcod.console_set_default_foreground(0, libtcod.white)
			pygame.display.update()
			time.sleep(0.1)
		loops+=1
		currentx+=x
		currenty+=y
		for i in xrange(len(planet)):
			message("workss")
			console_write(currentx)
			console_write(planet[i].x)
			if planet[i].x==currentx and planet[i].y==currenty:
				
				message(planet[i].name+" has been hit")
				monster_hit=True
				print("EYEYEYEYEYEYE")
				del planet[i]
				
				
				
				
				
				
		print("current="+str(currentx)+","+str(currenty))
def throwing(chemical,currentx,currenty, x,y):
	loops=1
	monster_hit=False
	
	
	while  random.randint(1,loops)<5 and currentx+x<screen_width-1 and currentx+x>=0 and currenty+y>=0 and currenty+y<screen_width-1 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True and monster_hit==False:
		print("ZOOOOOOOOO"+str(currentx)+" "+str(currenty)+" "+str(x)+" "+str(y))
		if currentx!=player.x or currenty!=player.y:
			print("zoop")
			libtcod.console_set_default_foreground(0, libtcod.blue)	
			libtcod.console_put_char_ex(0,currentx,currenty,"~", libtcod.white,libtcod.black)
			libtcod.console_set_default_foreground(0, libtcod.white)
			pygame.display.update()
			time.sleep(0.1)
		loops+=1
		
		currentx+=x
		currenty+=y
		for i in xrange(len(creature[current_planet][current_floor])):
			if creature[current_planet][current_floor][i].x==currentx and creature[current_planet][current_floor][i].y==currenty:
				message(creature[current_planet][current_floor][i].name+" has been hit")
				monster_hit=True
				planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
				
				if chemical=="mundinal":
					creature[current_planet][current_floor][i].health_points=player.health*2
					
				elif chemical=="iecurcide":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("poison",16,0.75))
					
					
				elif chemical=="adolite acid":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("poison",12,0.5))
					
					
				elif chemical=="forticide":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("poison",24,0.5))
					
					
				elif chemical=="caecilem":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("blind",12,1))
				
				
					
					
				
					
				elif chemical=="dorminyl":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("sleep",12,1))
					
				elif chemical=="ilvenam":
					for c in range(len(creature[current_planet][current_floor][i].status_effects)):
						if c<=len(creature[current_planet][current_floor][i].status_effects)-1 and creature[current_planet][current_floor][i].status_effects[c].effect=="poison":
							del creature[current_planet][current_floor][i].status_effects[c]
					
				elif chemical=="mergin":
					if hasattr(planet[current_planet].tiles[currentx][currenty][current_floor], "status_effect") and planet[current_planet].tiles[currentx][currenty][current_floor].status_effect!=None and planet[current_planet].tiles[currentx][currenty][current_floor].status_effect.effect=="fire":
						del planet[current_planet].tiles[currentx][currenty][current_floor].status_effect
					
					
				
				
				i=enemies_spawned
	
	if chemical=="incendite":
		planet[current_planet].tiles[currentx][currenty][current_floor].status_effect=status_effect("fire",6,1)
	elif chemical=="platzenyl":
		explode(currentx,currenty,5)
	if random.randint(1,loops)<5 and random.randint(1,10)!=1 and currentx+x<screen_width-1 and currentx+x<screen_width-1 and currenty+y<screen_width-1 and currentx+x>=0 and currenty+y>=0 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked==True:
		planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
def planting(chemical,currentx,currenty, x,y):
	loops=1
	monster_hit=False
	
	
	while  random.randint(1,loops)<5 and currentx+x<screen_width-1 and currentx+x>=0 and currenty+y>=0 and currenty+y<screen_width-1 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True and monster_hit==False:
		print("ZOOOOOOOOO"+str(currentx)+" "+str(currenty)+" "+str(x)+" "+str(y))
		if currentx!=player.x or currenty!=player.y:
			print("zoop")
			libtcod.console_set_default_foreground(0, libtcod.blue)	
			libtcod.console_put_char_ex(0,currentx,currenty,"~", libtcod.white,libtcod.black)
			libtcod.console_set_default_foreground(0, libtcod.white)
			pygame.display.update()
			time.sleep(0.1)
		loops+=1
		
		currentx+=x
		currenty+=y
		for i in xrange(len(creature[current_planet][current_floor])):
			if creature[current_planet][current_floor][i].x==currentx and creature[current_planet][current_floor][i].y==currenty:
				message(creature[current_planet][current_floor][i].name+" has been hit")
				monster_hit=True
				planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
				
				if chemical=="mundinal":
					creature[current_planet][current_floor][i].health_points=player.health*2
					
				elif chemical=="iecurcide":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("poison",16,0.75))
					
					
				elif chemical=="adolite acid":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("poison",12,0.5))
					
					
				elif chemical=="forticide":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("poison",24,0.5))
					
					
				elif chemical=="caecilem":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("blind",12,1))
				
				
					
					
				
					
				elif chemical=="dorminyl":
					creature[current_planet][current_floor][i].status_effects.append(status_effect("sleep",12,1))
					
				elif chemical=="ilvenam":
					for c in range(len(creature[current_planet][current_floor][i].status_effects)):
						if c<=len(creature[current_planet][current_floor][i].status_effects)-1 and creature[current_planet][current_floor][i].status_effects[c].effect=="poison":
							del creature[current_planet][current_floor][i].status_effects[c]
					
				elif chemical=="mergin":
					if hasattr(planet[current_planet].tiles[currentx][currenty][current_floor], "status_effect") and planet[current_planet].tiles[currentx][currenty][current_floor].status_effect!=None and planet[current_planet].tiles[currentx][currenty][current_floor].status_effect.effect=="fire":
						del planet[current_planet].tiles[currentx][currenty][current_floor].status_effect
					
					
				
				
				i=enemies_spawned
	
	if chemical=="incendite":
		planet[current_planet].tiles[currentx][currenty][current_floor].status_effect=status_effect("fire",6,1)
	elif chemical=="platzenyl":
		explode(currentx,currenty,5)
	if random.randint(1,loops)<5 and random.randint(1,10)!=1 and currentx+x<screen_width-1 and currentx+x<screen_width-1 and currenty+y<screen_width-1 and currentx+x>=0 and currenty+y>=0 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked==True:
		planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
def inventory_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player, weapons,armours
	DISPLAYSURF.fill((255,255,255))
	clor=None
	while mode=="inventory":
		for i in xrange(len(inventory)):
			if i<=len(inventory)-1 and inventory[i].number<1:
				del inventory[i]
		DISPLAYSURF.fill((255,255,255))
		for i in xrange(len(inventory)):
			
			if i==currentselection:
				clor=BLACK
				
			else:
				clor=GREY
			
			tlvt=inventory[i].strength
			if isinstance(inventory[i],Weapon):
				console_put_char_ex(0,i,"hack/sword.png")
			if isinstance(inventory[i],Armor):
				console_put_char_ex(0,i,shield)
			if isinstance(inventory[i], Chemical):
				if inventory[i].name=="arbinal":
					console_put_char_ex(0,i,chemo)
				elif inventory[i].name=="gaddin":
					console_put_char_ex(0,i,chemt)
				elif inventory[i].name=="branyl":
					console_put_char_ex(0,i,chemth)
				elif inventory[i].name=="resdin":
					console_put_char_ex(0,i,chemf)
				elif inventory[i].name=="chestin":
					console_put_char_ex(0,i,chemfi)
				elif inventory[i].name=="narkinal":
					console_put_char_ex(0,i,chems)
				elif inventory[i].name=="flattle":
					console_put_char_ex(0,i,chemse)
				else:
					console_put_char_ex(0,i, gen_chem)
			if isinstance(inventory[i],Armor) or isinstance(inventory[i],Weapon):
				
				if inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"] with strength of "+str(tlvt),clor,WHITE)
				else:
					console_print(1,i,inventory[i].name+" with strength of "+str(tlvt),clor,WHITE)
			else:
				if i<=len(inventory)-1 and inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"]",clor,WHITE)
				else:
					console_print(1,i,inventory[i].name,clor,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
			currentselection+=1
			
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
			if isinstance(inventory[currentselection],Weapon):
				current_weapon=inventory[currentselection]
			elif isinstance(inventory[currentselection],Armor):
				current_armor=inventory[currentselection]
			elif isinstance(inventory[currentselection],Chemical):
				if inventory[currentselection].name=="mundinal":
					player.health+=int(player.max_health/4)
					inventory[currentselection].number-=1
				elif inventory[currentselection].name=="curinal":
					player.health=player.health*4
					inventory[currentselection].number-=1
				elif inventory[currentselection].name=="iecurcide":
					player_status_effects.append(status_effect("poison",16,0.75))
					
					inventory[currentselection].number-=1
					currentselection=0
				elif inventory[currentselection].name=="adolite acid":
					player_status_effects.append(status_effect("poison",12,0.5))
					
					inventory[currentselection].number-=1
					currentselection=0
				elif inventory[currentselection].name=="forticide":
					player_status_effects.append(status_effect("poison",24,0.5))
					
					inventory[currentselection].number-=1
					currentselection=0
				elif inventory[currentselection].name=="mort acid":
					player_status_effects.append(status_effect("poison",48,0.5))
					
					inventory[currentselection].number-=1
					currentselection=0
				elif inventory[currentselection].name=="caecilem":
					player_status_effects.append(status_effect("blind",12,1))
					
					inventory[currentselection].number-=1
					currentselection=0
				elif inventory[currentselection].name=="incendite":
					planet[current_planet].tiles[player.x][player.y][current_floor].status_effect=status_effect("fire",6,1)
					inventory[currentselection].number-=1
				elif inventory[currentselection].name=="platzenyl":
					explode(player.x,player.y,5)
					inventory[currentselection].number-=1
				elif inventory[currentselection].name=="godyl":
					planet[current_planet].tiles[player.x][player.y][current_floor].status_effect=status_effect("gas",6,1)
					inventory[currentselection].number-=1
				elif inventory[currentselection].name=="dorminyl":
					player_status_effects.append(status_effect("sleep",12,1))
					inventory[currentselection].number-=1
				elif inventory[currentselection].name=="ilvenam":
					for c in range(len(player_status_effects)):
						if c<=len(player_status_effects)-1 and player_status_effects[c].effect=="poison":
							del player_status_effects[c]
					inventory[currentselection].number-=1
				elif inventory[currentselection].name=="mergin":
					if hasattr(planet[current_planet].tiles[player.x][player.y][current_floor], "status_effect") and planet[current_planet].tiles[player.x][player.y][current_floor].status_effect!=None and planet[current_planet].tiles[player.x][player.y][current_floor].status_effect.effect=="fire":
						del planet[current_planet].tiles[player.x][player.y][current_floor].status_effect
					
					inventory[currentselection].number-=1
		elif key.c==ord("z"):
			mode="ground"
		
			
	
		pygame.display.update()
def medical_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player, weapons,armours
	DISPLAYSURF.fill((255,255,255))
	while mode=="medical":
		pygame.display.update()
		DISPLAYSURF.fill((255,255,255))
		if len(player.wounds)<1:
			libtcod.console_set_default_foreground(0, libtcod.black)
			console_print(0,0,"No wounds",BLACK,WHITE)
		for i in xrange(len(player.wounds)):
		
			if i==currentselection:
				clor=BLACK
				
			else:
				clor=GREY
			
			
			
			
			console_print(0,i,player.wounds[i].name+" with loss of "+str(player.wounds[i].loss),clor,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(player.wounds)!=0 and currentselection!=len(player.wounds)-1:
			currentselection+=1
			
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
			player.health-=player.wounds[currentselection].loss
			player.max_health+=player.wounds[currentselection].loss
			del player.wounds[currentselection]
		elif key.c==ord("z"):
			mode="ground"
		
def messagelog(currentselection):
	global inventory, mode, current_weapon,current_armor, player, weapons,armours,message_log
	temp_log=message_log
	DISPLAYSURF.fill((255,255,255))
	
		
	while mode=="message":
		pygame.display.update()
		DISPLAYSURF.fill((255,255,255))
	
		for i in xrange(len(message_log)):
			
			
			libtcod.console_set_default_foreground(0, libtcod.grey)
			
			
			
			
			console_print(0,i,message_log[i+currentselection],BLACK,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(player.wounds)!=0 and currentselection!=len(player.wounds)-1:
			currentselection+=1
			
		
		elif key.c==ord("z"):
			mode="ground"			
	
def mix_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player, selected
	name=None
	DISPLAYSURF.fill((255,255,255))
	while mode=="mix":
		for i in xrange(len(inventory)):
			if len(inventory)-1>=i and inventory[i].number<1:
				del inventory[i]
		DISPLAYSURF.fill((255,255,255))
		for i in xrange(len(inventory)):
			
			if i==currentselection:
				clor=BLACK
			elif i==selected:
				clor=GREEN	
			else:
				clor=GREY
			
			tlvt=inventory[i].strength
			if isinstance(inventory[i],Weapon):
				console_put_char_ex(0,i,"hack/sword.png")
			if isinstance(inventory[i],Armor):
				console_put_char_ex(0,i,shield)
			if isinstance(inventory[i], Chemical):
				if inventory[i].name=="arbinal":
					console_put_char_ex(0,i,chemo)
				elif inventory[i].name=="gaddin":
					console_put_char_ex(0,i,chemt)
				elif inventory[i].name=="branyl":
					console_put_char_ex(0,i,chemth)
				elif inventory[i].name=="resdin":
					console_put_char_ex(0,i,chemf)
				elif inventory[i].name=="chestin":
					console_put_char_ex(0,i,chemfi)
				elif inventory[i].name=="narkinal":
					console_put_char_ex(0,i,chems)
				elif inventory[i].name=="flattle":
					console_put_char_ex(0,i,chemse)
				else:
					console_put_char_ex(0,i, gen_chem)
			if isinstance(inventory[i],Armor) or isinstance(inventory[i],Weapon):
				
				if inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"] with strength of "+str(tlvt),clor,WHITE)
				else:
					console_print(1,i,inventory[i].name+" with strength of "+str(tlvt),clor,WHITE)
			else:
				if inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"]",clor,WHITE)
				else:
					console_print(1,i,inventory[i].name,clor,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
			currentselection+=1
			
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER) and selected==None:
			
			selected=currentselection
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER) and selected!=currentselection:
			name=alchemy_convert(inventory[currentselection].name,inventory[selected].name)
			print(str(name))
			if name!=None and name!=False:
				inventory[currentselection].number-=1
				if currentselection<selected:
					inventory[selected ].number-=1
				else:
					inventory[selected].number-=1
				inventory.append(Chemical(name,1,1,None,None))
			
			selected=None
		
		elif key.c==ord("z") and selected== None:
			selected=None
			mode="ground"
		
			
		if currentselection!=None and selected!=0 and selected!=currentselection and selected!=None and name!=False and name!=None:
			
			message(alchemy_convert(inventory[currentselection].name,inventory[selected].name))
			message_display()
	
		pygame.display.update()
def incinerate_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player
	DISPLAYSURF.fill((255,255,255))
	while mode=="incinerate" and len(inventory)>0:
		DISPLAYSURF.fill((255,255,255))
		for i in xrange(len(inventory)):
		
			if i==currentselection:
				clor=BLACK
				
			else:
				clor=GREY
			
			tlvt=inventory[i].strength
			if isinstance(inventory[i],Weapon):
				console_put_char_ex(0,i,"hack/sword.png")
			if isinstance(inventory[i],Armor):
				console_put_char_ex(0,i,shield)
			if isinstance(inventory[i], Chemical):
				if inventory[i].name=="arbinal":
					console_put_char_ex(0,i,chemo)
				elif inventory[i].name=="gaddin":
					console_put_char_ex(0,i,chemt)
				elif inventory[i].name=="branyl":
					console_put_char_ex(0,i,chemth)
				elif inventory[i].name=="resdin":
					console_put_char_ex(0,i,chemf)
				elif inventory[i].name=="chestin":
					console_put_char_ex(0,i,chemfi)
				elif inventory[i].name=="narkinal":
					console_put_char_ex(0,i,chems)
				elif inventory[i].name=="flattle":
					console_put_char_ex(0,i,chemse)
				else:
					console_put_char_ex(0,i, gen_chem)
			if isinstance(inventory[i],Armor) or isinstance(inventory[i],Weapon):
				
				if inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"] with strength of "+str(tlvt),clor,WHITE)
				else:
					console_print(1,i,inventory[i].name+" with strength of "+str(tlvt),clor,WHITE)
			else:
				if inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"]",clor,WHITE)
				else:
					console_print(1,i,inventory[i].name,clor,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
			currentselection+=1
			
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
			
			del inventory[currentselection]
			currentselection=0
		elif key.c==ord("z"):
			mode="space"
		
			
	
		pygame.display.update()
	if len(inventory)==0:
		mode="space"
def status_screen():
	global inventory, mode
	DISPLAYSURF.fill((255,255,255))
	while mode=="status":
		DISPLAYSURF.fill((255,255,255))
		
		
		libtcod.console_set_default_foreground(0, libtcod.black)	
		console_print(0,0,"You have a "+current_weapon.name+" equipped.",BLACK,WHITE)
		console_print(0,1,"You have a "+current_armor.name+" equipped as armour.",BLACK,WHITE)
		console_print(0,2,"You are on planet "+planet[current_planet].name,BLACK,WHITE)
		console_print(0,3,"You have "+str(player.health)+" health.",BLACK,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		
		if key.c==ord("z"):
			mode="ground"
		
			
	
		pygame.display.update()
def liquid_move():
	global planet
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			if planet[current_planet].tiles[x][y][current_floor].liq!=None:
				print(planet[current_planet].tiles[x][y][current_floor].liq.type)
				if planet[current_planet].tiles[x][y][current_floor].liq.depth>1 and random.randint(1,planet[current_planet].tiles[x][y][current_floor].liq.inertia)==1:
					if x+2<=screen_width-1 and planet[current_planet].tiles[x+1][y][current_floor].liq!=None and planet[current_planet].tiles[x+1][y][current_floor].blocked==False and planet[current_planet].tiles[x+1][y][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or x+2<=screen_width-1 and planet[current_planet].tiles[x+1][y][current_floor].liq==None:
						if planet[current_planet].tiles[x+1][y][current_floor].liq==None:
							planet[current_planet].tiles[x+1][y][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x+1][y][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
					elif x-2>=1 and planet[current_planet].tiles[x-1][y][current_floor].liq!=None  and planet[current_planet].tiles[x-1][y][current_floor].blocked==False and planet[current_planet].tiles[x-1][y][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or x-2>=1 and planet[current_planet].tiles[x-1][y][current_floor].liq==None:
						if planet[current_planet].tiles[x-1][y][current_floor].liq==None:
							planet[current_planet].tiles[x-1][y][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x-1][y][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
					if y+2<=screen_width-1 and planet[current_planet].tiles[x][y+1][current_floor].liq !=None and planet[current_planet].tiles[x][y+1][current_floor].blocked==False  and planet[current_planet].tiles[x][y+1][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or y+2<=screen_width-1 and planet[current_planet].tiles[x][y+1][current_floor].liq==None:
						if planet[current_planet].tiles[x][y+1][current_floor].liq==None:
							planet[current_planet].tiles[x][y+1][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x][y+1][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
					
					elif y-2<=screen_width-1 and planet[current_planet].tiles[x][y-1][current_floor].liq!=None and planet[current_planet].tiles[x][y-1][current_floor].blocked==False and planet[current_planet].tiles[x][y-1][current_floor].liq.depth<planet[current_planet].tiles[x][y][current_floor].liq.depth or y-2<=screen_width-1 and planet[current_planet].tiles[x][y-1][current_floor].liq==None:
						if planet[current_planet].tiles[x][y-1][current_floor].liq==None:
							planet[current_planet].tiles[x][y-1][current_floor].liq=planet[current_planet].tiles[x][y][current_floor].liq
						planet[current_planet].tiles[x][y-1][current_floor].liq.depth=planet[current_planet].tiles[x][y][current_floor].liq.depth-1
						planet[current_planet].tiles[x][y][current_floor].liq.depth-=1
def space_inventory_screen():
	global inventory, mode, current_weapon,current_armor, player
	DISPLAYSURF.fill((255,255,255))
	currentselection=0
	while mode=="space_inventory1":
		DISPLAYSURF.fill((255,255,255))
		for i in xrange(len(inventory)):
		
			if i==currentselection:
				clor=BLACK
				
			else:
				clor=GREY
			
			tlvt=inventory[i].strength
			if isinstance(inventory[i],Weapon):
				console_put_char_ex(0,i,"hack/sword.png")
			if isinstance(inventory[i],Armor):
				console_put_char_ex(0,i,shield)
			if isinstance(inventory[i], Chemical):
				if inventory[i].name=="arbinal":
					console_put_char_ex(0,i,chemo)
				elif inventory[i].name=="gaddin":
					console_put_char_ex(0,i,chemt)
				elif inventory[i].name=="branyl":
					console_put_char_ex(0,i,chemth)
				elif inventory[i].name=="resdin":
					console_put_char_ex(0,i,chemf)
				elif inventory[i].name=="chestin":
					console_put_char_ex(0,i,chemfi)
				elif inventory[i].name=="narkinal":
					console_put_char_ex(0,i,chems)
				elif inventory[i].name=="flattle":
					console_put_char_ex(0,i,chemse)
				else:
					console_put_char_ex(0,i, gen_chem)
			if isinstance(inventory[i],Armor) or isinstance(inventory[i],Weapon):
				
				if inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"] with strength of "+str(tlvt),clor,WHITE)
				else:
					console_print(1,i,inventory[i].name+" with strength of "+str(tlvt),clor,WHITE)
			else:
				if inventory[i].number>1:
					console_print(1,i,inventory[i].name+"["+str(inventory[i].number)+"]",clor,WHITE)
				else:
					console_print(1,i,inventory[i].name,clor,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
			currentselection+=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
			mode="space_inventory2"	
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
			space_inventory.append(inventory[currentselection])
			del inventory[currentselection]
		elif key.c==ord("z"):
			mode="space"
		
			
	
		pygame.display.update()
	while mode=="space_inventory2":
		DISPLAYSURF.fill(WHITE)
		for i in xrange(len(space_inventory)):
		
			if i==currentselection:
				clor=WHITE
				
			else:
				clor=GREY
			
			tlvt=space_inventory[i].strength
			
			
			console_print(0,i,space_inventory[i].name+" with strength of "+str(tlvt),clor,WHITE)
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
			currentselection+=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
			mode="space_inventory1"	
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
			inventory.append(space_inventory[currentselection])
			del space_inventory[currentselection]
		elif key.c==ord("z"):
			mode="space"
		
			
	
		pygame.display.update()
def look(xc,yc):
	for critter in creature[current_planet][current_floor]:
		if critter.x ==xc and critter.y == yc:
			message(critter.name)
spacex=24
spacey=24

mode="space"

	


	
console_write(planet[0].tiles[0][0][0].blocked)

while not libtcod.console_is_window_closed():
	print(longest_name)
	if mode=="ground":
		
		if groundplay()==True:
			break
	elif mode=="space":
		
		if spaceplay()==True:
			break
	elif mode=="inventory":
		inventory_screen(0)
	elif mode=="status":
		status_screen()
	elif mode=="message":
		messagelog(0)
	elif mode=="mix":
		mix_screen(0)
	elif mode=="medical":
		medical_screen(0)
	elif mode=="incinerate":
		incinerate_screen(0)
	elif mode=="space_inventory1":
		space_inventory_screen()
sys.stderr.close()
sys.stderr = sys.__stderr__	
		
