#Importing important libraries
import libtcodpy as libtcod
from runt import *
import random
import math
import random
import math
import time
import os 
import datetime
from compiler.ast import flatten
import sys
ladder=["terrible", "poor", "mediocre", "average","fair", "good",  "great", "superb", "fantastic", "legendary", ]
sys.stderr = open('error\errorlog.txt', 'w')
#sets screen width
screen_width=51
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
def charactercreation():
	global charcartographer, charexplorer,charhacker,charlore,charmage,charmelee,charnombre,charrepair,charshooter,charspeaker,charunarmed
	charnombre="Your character"
	charmelee=random.randint(0,4)
	libtcod.console_print(0,0,4,charnombre+ " is a "+ladder[charmelee]+" melee fighter")
	charshooter=random.randint(0,4)
	libtcod.console_print(0,0,5,charnombre+ " is a "+ladder[charshooter]+" shooter")
	charmage=random.randint(0,4)
	libtcod.console_print(0,0,6,charnombre+ " is a "+ladder[charmage]+" psionic")
	charunarmed=random.randint(0,4)
	libtcod.console_print(0,0,7,charnombre+ " is a "+ladder[charunarmed]+" unarmed fighter")
	charspeaker=random.randint(0,4)
	libtcod.console_print(0,0,8,charnombre+ " is a "+ladder[charspeaker]+" speaker")
	charhacker=random.randint(0,4)
	libtcod.console_print(0,0,9,charnombre+ " is a "+ladder[charhacker]+" hacker")
	charcartographer=random.randint(0,4)
	libtcod.console_print(0,0,10,charnombre+ " is a "+ladder[charcartographer]+" cartographer")
	charrepair=random.randint(0,4)
	libtcod.console_print(0,0,11,charnombre+ " is a "+ladder[charrepair]+" repair")
	charlore=random.randint(0,4)
	libtcod.console_print(0,0,12,charnombre+ " is a "+ladder[charlore]+" lore knower")
	charexplorer=random.randint(0,4)
	libtcod.console_print(0,0,13,charnombre+ " is a "+ladder[charexplorer]+" explorer")
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
		
				
				libtcod.console_put_char_ex(0, x, y, "A", libtcod.white, libtcod.black)
	libtcod.console_flush()
	
	

	
	
charactercreation()
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
libtcod.console_set_custom_font('terminal16x16_gs_ro - Copy.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)

messages=[""]*4
#makes screen
libtcod.console_init_root(screen_width, screen_width*6/5, 'Game', False)
libtcod.sys_set_fps(60)
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
class Weapon:
	def __init__(self,name,strength,x,y):
		global current_floor,current_planet
		self.name=name
		self.strength=strength
		self.x=x
		self.y=y
		self.planet=current_planet
		self.floor=current_floor
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
		self.blood=False
		self.room=None
	
class Planet:
	def __init__(self,x,y,visited, player_x_coordinate,player_y_coordinate,name):
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
			if self.health_points>0.66*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 2, libtcod.white, libtcod.black)
			elif self.health_points<0.66*self.max_health and self.health_points>0.33*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 26, libtcod.white, libtcod.black)
			elif self.health_points<0.33*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 27, libtcod.white, libtcod.black)
		elif self.type=="snake" and self.health_points>0:
			libtcod.console_put_char_ex(0, self.x, self.y, 3, libtcod.white, libtcod.black)
		elif self.type=="bird" and self.health_points>0:
			libtcod.console_put_char_ex(0, self.x, self.y, 4, self.color, libtcod.white)
		elif self.type=="demon" and self.health_points>0:
			if self.health_points>0.66*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 5, libtcod.white, libtcod.black)
			elif self.health_points<0.66*self.max_health and self.health_points>0.33*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 28, libtcod.white, libtcod.black)
			elif self.health_points<0.33*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 29, libtcod.white, libtcod.black)	
		elif self.type=="insectoid" and self.health_points>0:
			libtcod.console_put_char_ex(0, self.x, self.y, 6,  self.color, libtcod.white)
		elif self.type=="flame-being" and self.health_points>0:
			if self.health_points>0.66*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 22, libtcod.white, libtcod.black)
			elif self.health_points<0.66*self.max_health and self.health_points>0.33*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 30, libtcod.white, libtcod.black)
			elif self.health_points<0.33*self.max_health:
				libtcod.console_put_char_ex(0, self.x, self.y, 31, libtcod.white, libtcod.black)
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
		self.x=x
		self.y=y
		self.health=100
		self.max_health=100
		self.wounds=[]
player_status_effects=[]
player=Player(None,None)


def alchemy_convert(itemo,itemt):
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
		
		result=""
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
			#libtcod.console_flush()
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
	global mode,player, current_floor, longest
	
	
	key = libtcod.console_wait_for_keypress(True)
	if player.health<=0:
		return(True)
	
	
	
	if libtcod.console_is_key_pressed(libtcod.KEY_UP) and planet[current_planet].tiles[player.x][player.y-1][current_floor].blocked==False and player.health>0:
		
		check_for_able_to_move(0,0-1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and planet[current_planet].tiles[player.x][player.y+1][current_floor].blocked==False and player.health>0:
		check_for_able_to_move(0,1)
	
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT) and planet[current_planet].tiles[player.x-1][player.y][current_floor].blocked==False and player.health>0:
		
		check_for_able_to_move(0-1,0)
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT) and planet[current_planet].tiles[player.x+1][player.y][current_floor].blocked==False and player.health>0:
		check_for_able_to_move(1,0)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP7) and planet[current_planet].tiles[player.x-1][player.y-1][current_floor].blocked==False and player.health>0:
		check_for_able_to_move(0-1,0-1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP9) and planet[current_planet].tiles[player.x+1][player.y-1][current_floor].blocked==False and player.health>0:
		check_for_able_to_move(1,0-1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP1) and planet[current_planet].tiles[player.x-1][player.y+1][current_floor].blocked==False and player.health>0:
		check_for_able_to_move(0-1,1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP3) and planet[current_planet].tiles[player.x+1][player.y+1][current_floor].blocked==False and player.health>0:
		check_for_able_to_move(1,1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_SPACE):
		
		mode="space"
	elif key.c==ord("i"):
		mode="inventory"
	elif key.c==ord("u"):
		mode="mix"
	elif key.c==ord("s"):
		mode="status"
	elif key.c==ord("a"):
		mode="message"
	elif key.c==ord("h"):
		mode="medical"
	elif key.c==ord("z"):
		ground_draw(True)
		done_shooting=False
		message("SHOOTING MODE IS ACTIVE")
		while(done_shooting==False):
			key=libtcod.console_wait_for_keypress(True)
			if libtcod.console_is_key_pressed(libtcod.KEY_UP):
				
				done_shooting=True
				shooting(player.x, player.y, 0,0-1)
			elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
				shooting(player.x, player.y, 0,1)
				done_shooting=True
			elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
				shooting(player.x, player.y, 1,0)
				done_shooting=True
			elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
				done_shooting=True
				shooting(player.x, player.y, 0-1,0)
			elif key.c==ord("x"):
				done_shooting=True
	elif key.c==ord("t"):
		for x in xrange (screen_width-1):
			for y in xrange(screen_width-1):
				libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
		currentselection=0
		slection=None
		while slection==None:
			libtcod.console_flush()
			
			for x in xrange(screen_width):
				for y in xrange(screen_width):
					libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
			for i in xrange(len(inventory)):
		
				if i==currentselection:
					libtcod.console_set_default_foreground(0, libtcod.white)
				
				else:
					libtcod.console_set_default_foreground(0, libtcod.grey)
			
				tlvt=inventory[i].strength
			
			
				libtcod.console_print(0,0,i,inventory[i].name+" with strength of "+str(tlvt))
		
			key = libtcod.console_wait_for_keypress(False)
		
			if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
				currentselection-=1
			elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
				currentselection+=1
			
			elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
				
					slection=inventory[currentselection].name
			elif key.c==ord("z"):
				
					slection=0
		
		
			
	
		libtcod.console_flush()
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
	elif key.c==ord("."):
		message("waited")
	
	
	
	else:
		handle_keys()
	

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
		
	elif key.vk == libtcod.KEY_ESCAPE:
		return True

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
	
	for x in range(0):
		eliminate_deadends()
	while planet[current_planet].tiles[planet[current_planet].tiles[0][0][current_floor].stairu[0]][planet[current_planet].tiles[0][0][current_floor].stairu[1]][current_floor].blocked==True:
		planet[current_planet].tiles[0][0][current_floor].stairu=[random.randint(2, screen_width-1),random.randint(2,screen_width-1)]
	while planet[current_planet].tiles[planet[current_planet].tiles[0][0][current_floor].stair[0]][planet[current_planet].tiles[0][0][current_floor].stair[1]][current_floor].blocked==True:
		planet[current_planet].tiles[0][0][current_floor].stair=[random.randint(2, screen_width-1),random.randint(2,screen_width-1)]
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
	
#handles the space controls
def handle_spacekey():
	
	global longest, longest_name
	global spacex, spacey, mode
	global placex, placey
	console_write("(((((((("+str(longest)+"longest "+longest_name+"))))))))")
	
	message("Your acceleration is at "+str(placex)+", "+str(placey))
	message("Your location is at "+str(spacex)+", "+str(spacey))
	pressedreal=False
	while pressedreal==False:
		key = libtcod.console_wait_for_keypress(True)
		libtcod.console_disable_keyboard_repeat()
		if libtcod.console_is_key_pressed(libtcod.KEY_UP)==True:
			placey -= 1
			pressedreal=True
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
			placey += 1
			pressedreal=True
		elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
			placex -= 1
			pressedreal=True
		elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
			placex += 1
			pressedreal=True
		elif key.c==ord("d"):
			mode="incinerate"
			pressedreal=True
		elif key.c==ord("i"):
			mode="space_inventory1"
			pressedreal=True
		
		elif key.c==ord("z"):
			space_draw()
			done_shooting=False
			message("SHOOTING MODE IS ACTIVE")
			while(done_shooting==False):
				libtcod.console_wait_for_keypress(True)
			
				done_shooting=True
				space_shooting(placex,placey)
			pressedreal=True
			pressedreal=True
		elif libtcod.console_is_key_pressed(libtcod.KEY_CHAR):
			pressedreal=True
	top_left[0]+=placex
	bottom_right=[top_left[0]+49,top_left[1]+49]
	top_left[1]+=placey
	bottom_right=[top_left[0]+49,top_left[1]+49]
	print("foist"+str(spacex))
	spacex+=placex
	spacey+=placey
	print("sec"+str(spacex))
	if key.c==ord("z"):
		space_draw()
		done_shooting=False
		message("SHOOTING MODE IS ACTIVE")
		while(done_shooting==False):
			libtcod.console_wait_for_keypress(True)
			
			done_shooting=True

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
	
	elif key.vk == libtcod.KEY_ESCAPE:
		return True
	
def ground_draw(shooting_mode):
	global player, longest, longest_name
	libtcod.map_compute_fov(fov_map, player.x,player.y,0,light_walls=True,algo=libtcod.FOV_DIAMOND)
	for x in xrange (screen_width):
		for y in xrange((screen_width*6/5)):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)		
			if y<screen_width-1 and x<screen_width-1:
				if planet[current_planet].tiles[x][y][current_floor].blocked==True:
						
					libtcod.map_set_properties(fov_map,x,y,False,False)
			
				else:
						
					libtcod.map_set_properties(fov_map,x,y,True,True)
	
	start=time.clock()
	libtcod.console_print (0,0,screen_width,"You are at "+str(player.health)+"/"+str(player.max_health)+" health")
	if check_for_status_effect("blind")!=True:
		for x in xrange(screen_width-1):
			for y in xrange(screen_width-1):
				for chemical in chemicals:
					if libtcod.map_is_in_fov(fov_map,chemical.x,chemical.y) and chemical.taken==False and chemical.floor==current_floor and chemical.planet==current_planet:
						if chemical.name=="arbinal":
							libtcod.console_put_char_ex(0, chemical.x, chemical.y, 7, libtcod.white, libtcod.black)
						elif chemical.name=="gaddin":
							libtcod.console_put_char_ex(0, chemical.x, chemical.y, 8, libtcod.white, libtcod.black)
						elif chemical.name=="branyl":
							libtcod.console_put_char_ex(0, chemical.x, chemical.y, 9, libtcod.white, libtcod.black)
						elif chemical.name=="resdin":
							libtcod.console_put_char_ex(0, chemical.x, chemical.y, 10, libtcod.white, libtcod.black)
						elif chemical.name=="chestin":
							libtcod.console_put_char_ex(0, chemical.x, chemical.y, 11, libtcod.white, libtcod.black)
						elif chemical.name=="narkinal":
							libtcod.console_put_char_ex(0, chemical.x, chemical.y, 12, libtcod.white, libtcod.black)
						elif chemical.name=="flattle":
							libtcod.console_put_char_ex(0, chemical.x, chemical.y, 13, libtcod.white, libtcod.black)
						
				for weapon in weapons:
				
					if hasattr(weapon,"x") and libtcod.map_is_in_fov(fov_map,weapon.x,weapon.y) and weapon.floor==current_floor and weapon.planet==current_planet:
						libtcod.console_put_char_ex(0,weapon.x,weapon.y,24, libtcod.grey, libtcod.white)
				for larmour in armours:
					if hasattr(larmour,"x") and libtcod.map_is_in_fov(fov_map,larmour.x,larmour.y) and larmour.floor==current_floor and larmour.planet==current_planet:
						libtcod.console_put_char_ex(0,larmour.x,larmour.y,23, libtcod.grey, libtcod.white)
				if planet[current_planet].tiles[x][y][current_floor].blocked==True and player.health>0 and libtcod.map_is_in_fov(fov_map,x,y):
					libtcod.console_set_default_foreground(0, libtcod.white)
					
					libtcod.console_put_char_ex(0, x, y, "#",  libtcod.white, libtcod.black)
				elif planet[current_planet].tiles[x][y][current_floor].blocked==False and player.health>0 and libtcod.map_is_in_fov(fov_map,x,y) :
					#CHAR_CHECKBOX_UNSET
					
					
					libtcod.console_put_char_ex(0, x, y, " ", libtcod.white, libtcod.white)
					if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect!=None and planet[current_planet].tiles[x][y][current_floor].status_effect.effect=="fire":
						libtcod.console_put_char_ex(0, x, y, 14, libtcod.white, libtcod.black)
					elif planet[current_planet].tiles[x][y][current_floor].blood==True:
						libtcod.console_put_char_ex(0, x, y, 15, libtcod.white, libtcod.black)
				else:
					libtcod.console_put_char(0,x,y," ", libtcod.BKGND_NONE)
				libtcod.console_set_default_foreground(0, libtcod.white)
				
				for critter in creature[current_planet][current_floor]:
				
					if libtcod.map_is_in_fov(fov_map,critter.x,critter.y):
						critter.draw()
			
				if shooting_mode==False:
					libtcod.console_put_char_ex(0, player.x, player.y, 1, libtcod.white, libtcod.black)
				if shooting_mode==True:
				
					libtcod.console_put_char_ex(0, player.x, player.y, 18, libtcod.white, libtcod.black)
				if x==planet[current_planet].tiles[0][0][current_floor].stair[0] and y==planet[current_planet].tiles[0][0][current_floor].stair[1] and libtcod.map_is_in_fov(fov_map,x,y):
					libtcod.console_put_char_ex(0, x, y, 16, libtcod.white, libtcod.black)
				if x==planet[current_planet].tiles[0][0][current_floor].stairu[0] and y==planet[current_planet].tiles[0][0][current_floor].stairu[1] and libtcod.map_is_in_fov(fov_map,x,y):
					libtcod.console_put_char_ex(0, x, y, 17, libtcod.white, libtcod.black)
	else:
		for x in xrange(screen_width-1):
			
			for y in xrange(screen_width-1):
				libtcod.console_put_char(0,x,y," ", libtcod.BKGND_NONE)
	if player.health<=0:
		for x in xrange(screen_width-1):
			for y in xrange(screen_width-1):
				
				libtcod.console_put_char(0, x, y, random.choice(["D","E","A","D"]), libtcod.BKGND_NONE)
	message_display()			
	#for p in range(roomnum+1):
		#color=libtcod.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		#for x in range(screen_width-1):
			#for y in range(screen_width-1):
				#if planet[current_planet].tiles[x][y][current_floor].room==p or planet[current_planet].tiles[x][y][current_floor].room=="passage":
					#libtcod.console_put_char_ex(0, x, y, "#", color, libtcod.black)
	libtcod.console_flush()
	end=time.clock()
	if (end-start)>longest:
		longest_name="drawn"
		longest=end-start
	
#defines ground gameplay
def groundplay():
	global longest, longest_name,planet, player_radioactivity, chemicals,current_floor,current_planet, mode
	global player, player,weapons,armours
	print(weapons)
	print("CW IS = "+str(current_weapon.name))
	for wound in player.wounds:
		if wound.subtracted==False:
			player.max_health-=wound.loss
			wound.subtracted=True
	if player.health>player.max_health:
		player.health=player.max_health
	print("THE CURRENT FLOOR IS"+str(current_floor))
	if current_floor<0:
		current_floor=0
	for i in range(len(chemicals)-1):
		if len(chemicals)-1>=i and player.x==chemicals[i].x and player.y==chemicals[i].y and chemicals[i].floor==current_floor and chemicals[i].planet==current_planet:
			inventory.append(chemicals[i])
			chemicals[i].taken=True
			message("Picked up "+str(chemicals[i].name))
			del chemicals[i]
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
			
			if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect!=None and planet[current_planet].tiles[x][y][current_floor].status_effect !=0:
				
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

	
	for weapon in weapons:
		if weapon.x==player.x and weapon.y==player.y and weapon.floor==current_floor and weapon.planet==current_planet:
			inventory.append(weapon)
			weapon.x=None
			weapon.y=None
			message("Picked up a weapon of strength "+str(weapon.strength))
	end=time.clock()
	if (end-start)>longest:
		longest_name="check if player is on weapon"
		longest=end-start		
	start=time.clock()
	if player_radioactivity>0:
		player.health=player.health-(player_radioactivity)
	player_radioactivity=int(player_radioactivity/2)
	for larmour in armours:
		if larmour.x==player.x and larmour.y==player.y and larmour.floor==current_floor and larmour.planet==current_planet:
			inventory.append(larmour)
			larmour.x=None
			larmour.y=None
			message("Picked up armour of strength "+str(larmour.strength))
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
					planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
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
					planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
				
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
					planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
				elif player.x-1>2 and creature[current_planet][current_floor][i].x==player.x-1 and creature[current_planet][current_floor][i].y==player.y and player_radioactivity>50:
					creature[current_planet][current_floor][i].health_points-=(player_radioactivity-50)
					planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
				elif player.x+1<screen_width-2 and creature[current_planet][current_floor][i].x==player.x+1 and creature[current_planet][current_floor][i].y==player.y and player_radioactivity>50:
					creature[current_planet][current_floor][i].health_points-=(player_radioactivity)
					planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
				elif player.y-1>2 and creature[current_planet][current_floor][i].x==player.x and creature[current_planet][current_floor][i].y==player.y-1 and player_radioactivity>50:
					creature[current_planet][current_floor][i].health_points-=(player_radioactivity)
					planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
			if creature[current_planet][current_floor][i].health_points>0  and current_planet==creature[current_planet][current_floor][i].planet and current_floor==creature[current_planet][current_floor][i].floor:
				libtcod.map_set_properties(fov_map,creature[current_planet][current_floor][i].x,creature[current_planet][current_floor][i].y,False,False)
		
			if creature[current_planet][current_floor][i].health_points<0  and current_planet==creature[current_planet][current_floor][i].planet and current_floor==creature[current_planet][current_floor][i].floor:
				monster_death(creature[current_planet][current_floor][i].x,creature[current_planet][current_floor][i].y)
			
				planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
				del creature[current_planet][current_floor][i]
			
			
	if sleep!=True and exit==True:
		return True
	end=time.clock()
	if (end-start)>longest:
		longest_name="movin enemies"
		longest=end-start		
	ground_draw(False)
	if player.x==planet[current_planet].tiles[0][0][current_floor].stair[0] and player.y==planet[current_planet].tiles[0][0][current_floor].stair[1]:
		console_write("downcf is "+str(current_floor))
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
		
	elif player.x==planet[current_planet].tiles[0][0][current_floor].stairu[0] and player.y==planet[current_planet].tiles[0][0][current_floor].stairu[1]:
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
	
		
for x in xrange(number_of_planets):
	planet.append(Planet(random.randint(-100,100),random.randint(-100,100),False,0,0,monster_name()[1] ))

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
	
	for i in xrange(3):	
		libtcod.console_print(0,0,screen_width+i+1,"                                                                         ")
		libtcod.console_print (0,0,screen_width+i+1,messages[i])
			
			
			
		libtcod.console_flush()
	
def space_draw():
	
	for x in xrange (screen_width):
		for y in xrange((screen_width*6/5)):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	
	libtcod.console_flush()
	
	
	
	

	for x in range(len(starx)):		
				
		
		if stary[x]-top_left[1]<screen_width-1 and starx[x]<bottom_right[0] and stary[x]<bottom_right[1] and starx[x]>top_left[0] and stary[x]>top_left[1]:
						
			libtcod.console_put_char_ex(0, starx[x]-top_left[0],stary[x]-top_left[1], ".", libtcod.white,libtcod.black)
	
			
	
	
	
	for x in xrange(number_of_planets):
		
		if planet[x].y-top_left[1]<screen_width-1 and planet[x].x<bottom_right[0] and planet[x].y<bottom_right[1] and planet[x].x>top_left[0] and planet[x].y>top_left[1]:
			libtcod.console_set_default_foreground(0, planet[x].color)
			libtcod.console_put_char_ex(0, planet[x].x-top_left[0],planet[x].y-top_left[1], 21, planet[x].color,libtcod.black)
	libtcod.console_set_default_foreground(0, libtcod.white)
	#libtcod.console_put_char(0, spacex-top_left[0], spacey-top_left[1], "$", libtcod.BKGND_NONE)
	libtcod.console_put_char(0, 24, 24, 20, libtcod.BKGND_NONE)
	
			
	
	
	
	libtcod.console_flush()
#defines how the game plays in space
def spaceplay():
	global planet,mode, player, number_of_planets, spacexmax,spacexmin,spaceymax,spaceymin
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	print("REEEEEEEEEEEEE")
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
	handle_spacekey()
	for i in xrange(number_of_planets):
		if spacex==planet[i].x and spacey==planet[i].y :
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
	print("reeeeeeeee")			
#Randomly places the player down. PRE-ALPHA CODE        
def explode(stx,sty,vel):
	
	lent=0
	while vel>0:
		lent+=1
		vel-=1
		for x in range(lent):
			
			planet[current_planet].tiles[stx+x][sty+x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx+x,sty+x):
				libtcod.console_put_char_ex(0, stx+x, sty+x, 25, libtcod.white, libtcod.black)
			planet[current_planet].tiles[stx-x][sty+x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx-x,sty+x):
				libtcod.console_put_char_ex(0, stx-x, sty+x, 25, libtcod.white, libtcod.black)
			planet[current_planet].tiles[stx+x][sty-x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx+x,sty-x):
				libtcod.console_put_char_ex(0, stx+x, sty-x, 25, libtcod.white, libtcod.black)
			planet[current_planet].tiles[stx][sty+x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx,sty+x):
				libtcod.console_put_char_ex(0, stx, sty+x, 25, libtcod.white, libtcod.black)
			planet[current_planet].tiles[stx+x][sty][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx+x,sty):
				libtcod.console_put_char_ex(0, stx+x, sty, 25, libtcod.white, libtcod.black)
			planet[current_planet].tiles[stx-x][sty-x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx-x,sty-x):
				libtcod.console_put_char_ex(0, stx-x, sty-x, 25, libtcod.white, libtcod.black)
			planet[current_planet].tiles[stx][sty-x][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx,sty-x):
				libtcod.console_put_char_ex(0, stx, sty-x, 25, libtcod.white, libtcod.black)
			planet[current_planet].tiles[stx-x][sty][current_floor].blocked=False
			if libtcod.map_is_in_fov(fov_map,stx-x,sty):
				libtcod.console_put_char_ex(0, stx-x, sty, 25, libtcod.white, libtcod.black)
			libtcod.console_flush()
			

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
			libtcod.console_put_char_ex(0,currentx,currenty,19, libtcod.white,libtcod.black)
			libtcod.console_set_default_foreground(0, libtcod.white)
			libtcod.console_flush()
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
				planet[current_planet].tiles[creature[current_planet][current_floor][i].x][creature[current_planet][current_floor][i].y][current_floor].blood=True
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
			libtcod.console_flush()
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
			libtcod.console_flush()
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
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	while mode=="inventory":
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		for i in xrange(len(inventory)):
		
			if i==currentselection:
				libtcod.console_set_default_foreground(0, libtcod.white)
				
			else:
				libtcod.console_set_default_foreground(0, libtcod.grey)
			
			tlvt=inventory[i].strength
			
			
			libtcod.console_print(0,0,i,inventory[i].name+" with strength of "+str(tlvt))
		
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
					del inventory[currentselection]
				elif inventory[currentselection].name=="curinal":
					player.health=player.health*4
					del inventory[currentselection]
				elif inventory[currentselection].name=="iecurcide":
					player_status_effects.append(status_effect("poison",16,0.75))
					
					del inventory[currentselection]
					currentselection=0
				elif inventory[currentselection].name=="adolite acid":
					player_status_effects.append(status_effect("poison",12,0.5))
					
					del inventory[currentselection]
					currentselection=0
				elif inventory[currentselection].name=="forticide":
					player_status_effects.append(status_effect("poison",24,0.5))
					
					del inventory[currentselection]
					currentselection=0
				elif inventory[currentselection].name=="mort acid":
					player_status_effects.append(status_effect("poison",48,0.5))
					
					del inventory[currentselection]
					currentselection=0
				elif inventory[currentselection].name=="caecilem":
					player_status_effects.append(status_effect("blind",12,1))
					
					del inventory[currentselection]
					currentselection=0
				elif inventory[currentselection].name=="incendite":
					planet[current_planet].tiles[player.x][player.y][current_floor].status_effect=status_effect("fire",6,1)
					del inventory[currentselection]
				elif inventory[currentselection].name=="platzenyl":
					explode(player.x,player.y,5)
					del inventory[currentselection]
				elif inventory[currentselection].name=="godyl":
					planet[current_planet].tiles[player.x][player.y][current_floor].status_effect=status_effect("gas",6,1)
					del inventory[currentselection]
				elif inventory[currentselection].name=="dorminyl":
					player_status_effects.append(status_effect("sleep",12,1))
					del inventory[currentselection]
				elif inventory[currentselection].name=="ilvenam":
					for c in range(len(player_status_effects)):
						if c<=len(player_status_effects)-1 and player_status_effects[c].effect=="poison":
							del player_status_effects[c]
					del inventory[currentselection]
				elif inventory[currentselection].name=="mergin":
					if hasattr(planet[current_planet].tiles[player.x][player.y][current_floor], "status_effect") and planet[current_planet].tiles[player.x][player.y][current_floor].status_effect!=None and planet[current_planet].tiles[player.x][player.y][current_floor].status_effect.effect=="fire":
						del planet[current_planet].tiles[player.x][player.y][current_floor].status_effect
					
					del inventory[currentselection]
		elif key.c==ord("z"):
			mode="ground"
		
			
	
		libtcod.console_flush()
def medical_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player, weapons,armours
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	while mode=="medical":
		libtcod.console_flush()
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		for i in xrange(len(player.wounds)):
		
			if i==currentselection:
				libtcod.console_set_default_foreground(0, libtcod.white)
				
			else:
				libtcod.console_set_default_foreground(0, libtcod.grey)
			
			
			
			
			libtcod.console_print(0,0,i,player.wounds[i].name+" with loss of "+str(player.wounds[i].loss))
		
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
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	
		
	while mode=="message":
		libtcod.console_flush()
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
	
		for i in xrange(len(message_log)):
			
			
			libtcod.console_set_default_foreground(0, libtcod.grey)
			
			
			
			
			libtcod.console_print(0,0,i,message_log[i+currentselection])
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(player.wounds)!=0 and currentselection!=len(player.wounds)-1:
			currentselection+=1
			
		
		elif key.c==ord("z"):
			mode="ground"			
	
def mix_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player, selected
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	while mode=="mix":
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		for i in xrange(len(inventory)):
		
			if i==currentselection:
				libtcod.console_set_default_foreground(0, libtcod.white)
			elif i==selected:
				libtcod.console_set_default_foreground(0, libtcod.green)
			else:
				libtcod.console_set_default_foreground(0, libtcod.grey)
			
			tlvt=inventory[i].strength
			
			
			libtcod.console_print(0,0,i,inventory[i].name+" with strength of "+str(tlvt))
		
		key = libtcod.console_wait_for_keypress(False)
		
		if libtcod.console_is_key_pressed(libtcod.KEY_UP) and currentselection!=0:
			currentselection-=1
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and len(inventory)!=0 and currentselection!=len(inventory)-1:
			currentselection+=1
			
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER) and selected==None:
			
			selected=currentselection
		elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER) and selected!=currentselection:
			name=alchemy_convert(inventory[currentselection].name,inventory[selected].name)
			if name!=None:
				del inventory[currentselection]
				if currentselection<selected:
					del inventory[selected-1]
				else:
					del inventory[selected]
				inventory.append(Chemical(name,1,1,None,None))
			selected=None
		
		elif key.c==ord("z") and selected== None:
			selected=None
			mode="ground"
		
			
		if currentselection!=None and selected!=0 and selected!=currentselection and selected!=None:
			
			message(alchemy_convert(inventory[currentselection].name,inventory[selected].name))
			
	
		libtcod.console_flush()
def incinerate_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	while mode=="incinerate" and len(inventory)>0:
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		for i in xrange(len(inventory)):
		
			if i==currentselection:
				libtcod.console_set_default_foreground(0, libtcod.white)
				
			else:
				libtcod.console_set_default_foreground(0, libtcod.grey)
			
			tlvt=inventory[i].strength
			
			
			libtcod.console_print(0,0,i,inventory[i].name+" with strength of "+str(tlvt))
		
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
		
			
	
		libtcod.console_flush()
	if len(inventory)==0:
		mode="space"
def status_screen():
	global inventory, mode
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	while mode=="status":
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		
		
			
		libtcod.console_print(0,0,0,"You have a "+current_weapon.name+" equipped.")
		libtcod.console_print(0,0,1,"You have a "+current_armor.name+" equipped as armour.")
		libtcod.console_print(0,0,2,"You are on planet "+planet[current_planet].name)
		libtcod.console_print(0,0,3,"You have "+str(player.health)+" health.")
		
		key = libtcod.console_wait_for_keypress(False)
		
		
		if key.c==ord("z"):
			mode="ground"
		
			
	
		libtcod.console_flush()

def space_inventory_screen():
	global inventory, mode, current_weapon,current_armor, player
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			libtcod.console_put_char_ex(0, x, y, " ", libtcod.black, libtcod.black)
	currentselection=0
	while mode=="space_inventory1":
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		for i in xrange(len(inventory)):
		
			if i==currentselection:
				libtcod.console_set_default_foreground(0, libtcod.white)
				
			else:
				libtcod.console_set_default_foreground(0, libtcod.grey)
			
			tlvt=inventory[i].strength
			
			
			libtcod.console_print(0,0,i,inventory[i].name+" with strength of "+str(tlvt))
		
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
		
			
	
		libtcod.console_flush()
	while mode=="space_inventory2":
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		for i in xrange(len(space_inventory)):
		
			if i==currentselection:
				libtcod.console_set_default_foreground(0, libtcod.white)
				
			else:
				libtcod.console_set_default_foreground(0, libtcod.grey)
			
			tlvt=space_inventory[i].strength
			
			
			libtcod.console_print(0,0,i,space_inventory[i].name+" with strength of "+str(tlvt))
		
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
		
			
	
		libtcod.console_flush()
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
		
