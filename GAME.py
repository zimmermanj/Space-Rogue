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
charrepair=0
charlore=0
charexplorer=0
def charactercreation():
  
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
def load_customfont():
	a = 256
 
	print("meh")
	libtcod.console_map_ascii_code_to_font(256, 0, 6)
	libtcod.console_map_ascii_code_to_font(257, 1, 6)
	
load_customfont()		
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
orc_tile = 259
troll_tile = 260
scroll_tile = 261
healingpotion_tile = 262
sword_tile = 263
shield_tile = 264
stairsdown_tile = 265
dagger_tile = 266
player_radioactivity=30 #0
fov_map=libtcod.map_new(screen_width-1, screen_width-1)
messages=[]
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

messages=[""]*4
#makes screen
libtcod.console_init_root(screen_width, screen_width*6/5, 'Game', False)
planet=[]
#makes inventory
inventory=[]
space_inventory=[]
current_weapon=0
current_armor=0
player_health=10000 #100
max_health=10000 #100
current_floor=0
top_left=[0,0]
bottom_right=[49,49]
longest=0
longest_name="none"
file=open("map.txt","w+")

#creates tile class
class Weapon:
	def __init__(self,name,strength,x,y):
		self.name=name
		self.strength=strength
		self.x=x
		self.y=y
		
class Armor:
	def __init__(self,name,strength,x,y):
		self.name=name
		self.strength=strength
		self.x=x
		self.y=y
class Chemical:
	def __init__(self,name,strength,power,x,y):
		self.name=name
		self.strength=strength
		self.power=power
		self.x=x
		self.y=y
weapons=[0]
weapons[0]=Weapon("Basic Weapon",1,None,None)
inventory.append(weapons[0])
armours=[0]
armours[0]=Armor("Basic Armour",1,None,None)
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
	def __init__(self,x,y,goal_x_coordinate,goal_y_coordinate, capital, name,health_points,floor,planet):
		self.x=x
		self.y=y
		self.goal_x_coordinate=goal_x_coordinate
		self.goal_y_coordinate=goal_y_coordinate
		self.capital=capital
		self.name=name
		self.health_points=health_points
		self.floor=floor
		self.planet=planet
		self.status_effects=[status_effect("health", 50,1)]
		
	def go(self):
		sleep=False
		for fect in self.status_effects:
			if fect.effect=="sleep":
				sleep=True
			
		if sleep==False and self.health_points>0 and current_planet==self.planet and current_floor==self.floor:
			return(path_finder(self.x,self.y,self.goal_x_coordinate,self.goal_y_coordinate))
	def draw(self):
		if self.health_points>0 and current_planet==self.planet and current_floor==self.floor:
			libtcod.console_put_char(0, self.x, self.y, self.capital, libtcod.BKGND_NONE)
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
player_status_effects=[]



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
		result='curinal'
	elif itemo=='branyl' and itemt=='flattle' or itemo=='flattle' and itemt=='branyl':
		result='il-forticide'
	elif itemo=='resdin' and itemt=='chestin' or itemo=='chestin' and itemt=='resdin':
		result='caecilem'
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
		print(str(itemo)+","+str(itemt))
		result=None
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
	global longest, longest_name
	end=0
	

	start=time.clock()
	

	for x in xrange(x2-x1+1):
		if end==1:
			break
		for y in xrange(y2-y1+1):
			
			if(planet[current_planet].tiles[x1+x][y1+y][current_floor].blocked==True):
				planet[current_planet].tiles[x1+x][y1+y][current_floor].blocked=False
                
			else:
                
				end=1
				break
	end=time.clock()
	if (end-start)>longest:
		longest_name="room make"
		longest=end-start			
#defines a passage        
def make_passage(c1, c2, c3, type):
	global longest, longest_name
	end=0
	start=time.clock()
	for x in xrange(max(c2,c1)-min(c2,c1)+1):
	
		if end==1:
			break
        if type== "y":
            
            planet[current_planet].tiles[c3][x+min(c2, c1)][current_floor].blocked=False
        if type== "x":
           
           planet[current_planet].tiles[x+min(c2, c1)][c3][current_floor].blocked=False
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
	global player_x_coordinate, player_y_coordinate, enemies_spawned, longest
	no_monster_there=True
	

	start=time.clock()


	for critter in creature[current_planet][current_floor]:
			
		if critter.x==player_x_coordinate+x and critter.y ==player_y_coordinate+y and critter.health_points>0:
			critter.health_points-=1
			no_monster_there=False
			message(critter.name+" has been hit")
		console_write (critter.capital)
		
	console_write (no_monster_there)			
	if no_monster_there==True:
		player_y_coordinate += y
		player_x_coordinate+=x
		
	end=time.clock()
	if (end-start)>longest:
		longest_name="check for able to move"
		longest=end-start	
		
#how the player moves on the ground	
def handle_keys():
	global mode,player_x_coordinate, player_y_coordinate, current_floor, longest
	
	libtcod.console_disable_keyboard_repeat()
	key = libtcod.console_wait_for_keypress(True)
	if player_health<=0:
		return(True)
	
	
	
	if libtcod.console_is_key_pressed(libtcod.KEY_UP) and planet[current_planet].tiles[player_x_coordinate][player_y_coordinate-1][current_floor].blocked==False and player_health>0:
		
		check_for_able_to_move(0,0-1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) and planet[current_planet].tiles[player_x_coordinate][player_y_coordinate+1][current_floor].blocked==False and player_health>0:
		check_for_able_to_move(0,1)
	
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT) and planet[current_planet].tiles[player_x_coordinate-1][player_y_coordinate][current_floor].blocked==False and player_health>0:
		
		check_for_able_to_move(0-1,0)
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT) and planet[current_planet].tiles[player_x_coordinate+1][player_y_coordinate][current_floor].blocked==False and player_health>0:
		check_for_able_to_move(1,0)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP7) and planet[current_planet].tiles[player_x_coordinate-1][player_y_coordinate-1][current_floor].blocked==False and player_health>0:
		check_for_able_to_move(0-1,0-1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP9) and planet[current_planet].tiles[player_x_coordinate+1][player_y_coordinate-1][current_floor].blocked==False and player_health>0:
		check_for_able_to_move(1,0-1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP1) and planet[current_planet].tiles[player_x_coordinate-1][player_y_coordinate+1][current_floor].blocked==False and player_health>0:
		check_for_able_to_move(0-1,1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_KP3) and planet[current_planet].tiles[player_x_coordinate+1][player_y_coordinate+1][current_floor].blocked==False and player_health>0:
		check_for_able_to_move(1,1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_SPACE):
		
		mode="space"
	elif key.c==ord("i"):
		mode="inventory"
	elif key.c==ord("u"):
		mode="mix"
	elif key.c==ord("s"):
		mode="status"
	elif key.c==ord("z"):
		ground_draw(True)
		done_shooting=False
		message("SHOOTING MODE IS ACTIVE")
		while(done_shooting==False):
			libtcod.console_wait_for_keypress(True)
			if libtcod.console_is_key_pressed(libtcod.KEY_UP):
				
				done_shooting=True
				shooting(player_x_coordinate, player_y_coordinate, 0,0-1)
			elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
				shooting(player_x_coordinate, player_y_coordinate, 0,1)
				done_shooting=True
			elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
				shooting(player_x_coordinate, player_y_coordinate, 1,0)
				done_shooting=True
			elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
				done_shooting=True
				shooting(player_x_coordinate, player_y_coordinate, 0-1,0)
	elif key.c==ord("t"):
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
					
		
		
			
	
		libtcod.console_flush()
		ground_draw(True)
		done_shooting=False
		message("THROWING MODE IS ACTIVE")
		while(done_shooting==False):
			libtcod.console_wait_for_keypress(True)
			if libtcod.console_is_key_pressed(libtcod.KEY_UP):
				
				done_shooting=True
				throwing(slection,player_x_coordinate, player_y_coordinate, 0,0-1)
			elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
				throwing(slection,player_x_coordinate, player_y_coordinate, 0,1)
				done_shooting=True
			elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
				throwing(slection,player_x_coordinate, player_y_coordinate, 1,0)
				done_shooting=True
			elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
				done_shooting=True
				throwing(slection,player_x_coordinate, player_y_coordinate, 0-1,0)
	elif key.c==ord("."):
		message("waited")
	
	
	elif player_x_coordinate==planet[current_planet].tiles[0][0][current_floor].stair[0] and player_y_coordinate==planet[current_planet].tiles[0][0][current_floor].stair[1]  or key.c==ord("d") :
		console_write("cf is "+str(current_floor))
		
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
		player_x_coordinate=planet[current_planet].tiles[0][0][current_floor].stairu[0]
		player_y_coordinate=planet[current_planet].tiles[0][0][current_floor].stairu[1]
		planet[current_planet].floor_visited[current_floor]=True
		
	elif player_x_coordinate==planet[current_planet].tiles[0][0][current_floor].stairu[0] and player_y_coordinate==planet[current_planet].tiles[0][0][current_floor].stairu[1]  or key.c==ord("d") :
		console_write("cf is "+str(current_floor))
		current_floor-=1
		if current_floor>0:
			
			if planet[current_planet].floor_visited[current_floor-1]==False:
				make_ground_map()
				make_all_enemies_on_floor(5)	
			player_x_coordinate=planet[current_planet].tiles[0][0][current_floor].stairu[0]
			player_y_coordinate=planet[current_planet].tiles[0][0][current_floor].stairu[1]
			planet[current_planet].floor_visited[current_floor]=True
		else:
			mode="space"
	else:
		handle_keys()
	

	if key.vk == libtcod.KEY_ENTER and key.lalt:
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
		
	elif key.vk == libtcod.KEY_ESCAPE:
		return True

#makes the map for the ground
def make_ground_map():
	global longest, longest_name, planet
	for x in range(screen_width-1):
		for y in range(screen_width-1):
			while len(planet[current_planet].tiles[x][y])<current_floor+1:
				planet[current_planet].tiles[x][y].append(Tile(True, "none","none","none"))
	general_variable=0
	new_x=player_x_coordinate
	new_x=player_y_coordinate
	new_x_two=player_x_coordinate
	new_x_two=player_y_coordinate
	
	start=time.clock()
	
	
	while general_variable<20:
		x=random.randint(1,screen_width-3)
		y=random.randint(1,screen_width-3)
		x_two=random.randint(x, screen_width-3)
		y_two=random.randint(y,screen_width-3)
		make_room(x, x_two, y, y_two)
        
        
        
		make_passage(new_x_two, x, new_x_two, "x")
		make_passage(new_x_two, y, x, "y")
        
        
		new_x=x
		new_x=y
		new_x_two=x_two
		new_x_two=y_two
		general_variable+=1
		
		
	end=time.clock()
	if (end-start)>longest:
		longest_name="make ground map"
		longest=end-start

	stx=random.randint(0,screen_width-2)
	sty=random.randint(0,screen_width-2)
	console_write(current_floor)
	while planet[current_planet].tiles[stx][sty][current_floor].blocked==True:
		console_write(stx)
		console_write(sty)
		stx=random.randint(0,screen_width-2)
		sty=random.randint(0,screen_width-2)
		console_write(stx)
		console_write(sty)
	planet[current_planet].tiles[0][0][current_floor].stair=[stx,sty]
	stx=random.randint(0,screen_width-2)
	sty=random.randint(0,screen_width-2)
	while planet[current_planet].tiles[stx][sty][current_floor].blocked==True:
		console_write(stx)
		console_write(sty)
		stx=random.randint(0,screen_width-2)
		sty=random.randint(0,screen_width-2)
		console_write(stx)
		console_write(sty)
	planet[current_planet].tiles[0][0][current_floor].stairu=[stx,sty]
#handles the space controls
def handle_spacekey():
	global longest, longest_name
	global spacex, spacey, mode
	global placex, placey
	console_write("(((((((("+str(longest)+"longest "+longest_name+"))))))))")
	key = libtcod.console_wait_for_keypress(True)
	libtcod.console_disable_keyboard_repeat()
	message("Your acceleration is at "+str(placex)+", "+str(placey))
	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		placey -= 1
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		placey += 1
		
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		placex -= 1
		print(placex)
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		placex += 1
	elif key.c==ord("d"):
		mode="incinerate"
	elif key.c==ord("i"):
		mode="space_inventory1"
	elif key.c==ord("z"):
		space_draw()
		done_shooting=False
		message("SHOOTING MODE IS ACTIVE")
		while(done_shooting==False):
			libtcod.console_wait_for_keypress(True)
			
			done_shooting=True
			space_shooting(spacex, spacex, placex,placey)
	top_left[0]+=placex
	bottom_right=[top_left[0]+49,top_left[1]+49]
	top_left[1]+=placey
	bottom_right=[top_left[0]+49,top_left[1]+49]
	print("foist"+str(spacex))
	spacex+=placex
	spacey+=placey
	print("sec"+str(spacex))
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
	
	elif key.vk == libtcod.KEY_ESCAPE:
		return True
def ground_draw(shooting_mode):
	global player_health, longest, longest_name
	libtcod.map_compute_fov(fov_map, player_x_coordinate,player_y_coordinate,0,light_walls=True,algo=libtcod.FOV_DIAMOND)
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
					
			if planet[current_planet].tiles[x][y][current_floor].blocked==True:
						
				libtcod.map_set_properties(fov_map,x,y,False,False)
			
			else:
						
				libtcod.map_set_properties(fov_map,x,y,True,True)
	
	start=time.clock()
	libtcod.console_print (0,0,screen_width,"You are at "+str(player_health)+"/"+str(max_health)+" health")
	if check_for_status_effect("blind")!=True:
		for x in xrange(screen_width-1):
			for y in xrange(screen_width-1):
			
				for weapon in weapons:
				
					if hasattr(weapon,"x") and libtcod.map_is_in_fov(fov_map,weapon.x,weapon.y):
						libtcod.console_put_char(0,weapon.x,weapon.y,"w", libtcod.BKGND_NONE)
				for larmour in armours:
					if hasattr(larmour,"x") and libtcod.map_is_in_fov(fov_map,larmour.x,larmour.y):
						libtcod.console_put_char(0,larmour.x,larmour.y,"a", libtcod.BKGND_NONE)
				if planet[current_planet].tiles[x][y][current_floor].blocked==True and player_health>0 and libtcod.map_is_in_fov(fov_map,x,y):
					libtcod.console_set_default_foreground(0, libtcod.white)
					
					libtcod.console_put_char_ex(0, x, y, "#",  libtcod.white, libtcod.black)
				elif planet[current_planet].tiles[x][y][current_floor].blocked==False and player_health>0 and libtcod.map_is_in_fov(fov_map,x,y) :
					#CHAR_CHECKBOX_UNSET
					
					
					libtcod.console_put_char_ex(0, x, y, 9, libtcod.white, libtcod.black)
					if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect!=None and planet[current_planet].tiles[x][y][current_floor].status_effect.effect=="fire":
						libtcod.console_put_char_ex(0, x, y, 224, libtcod.white, libtcod.black)
				
					
				else:
					libtcod.console_put_char(0,x,y," ", libtcod.BKGND_NONE)
				libtcod.console_set_default_foreground(0, libtcod.white)
			
				for critter in creature[current_planet][current_floor]:
				
					if libtcod.map_is_in_fov(fov_map,critter.x,critter.y):
						critter.draw()
			
				if shooting_mode==False:
					libtcod.console_put_char(0, player_x_coordinate, player_y_coordinate, "@", libtcod.BKGND_NONE)
				if shooting_mode==True:
				
					libtcod.console_put_char(0, player_x_coordinate, player_y_coordinate, "@", libtcod.BKGND_NONE)
				if x==planet[current_planet].tiles[0][0][current_floor].stair[0] and y==planet[current_planet].tiles[0][0][current_floor].stair[1] and libtcod.map_is_in_fov(fov_map,x,y):
					libtcod.console_put_char(0, x, y, ">", libtcod.BKGND_NONE)
				if x==planet[current_planet].tiles[0][0][current_floor].stairu[0] and y==planet[current_planet].tiles[0][0][current_floor].stairu[1] and libtcod.map_is_in_fov(fov_map,x,y):
					libtcod.console_put_char(0, x, y, "<", libtcod.BKGND_NONE)
	else:
		for x in xrange(screen_width-1):
			
			for y in xrange(screen_width-1):
				libtcod.console_put_char(0,x,y," ", libtcod.BKGND_NONE)
	if player_health<=0:
		for x in xrange(screen_width-1):
			for y in xrange(screen_width-1):
				
				libtcod.console_put_char(0, x, y, random.choice(["D","E","A","D"]), libtcod.BKGND_NONE)
				
	
	libtcod.console_flush()
	end=time.clock()
	if (end-start)>longest:
		longest_name="drawn"
		longest=end-start
	
#defines ground gameplay
def groundplay():
	global longest, longest_name,planet, player_radioactivity
		
		
	global player_health, player_x_coordinate, player_y_coordinate
	console_write("((s))"+str(longest)+longest_name+"((e))")
	
	ground_draw(False)
	start=time.clock()
	for leffect in range(len(player_status_effects)):
		
		print("asd"+str(player_status_effects[leffect]))
		
		thing=player_status_effects[leffect].effect
		if thing=="poison":
			player_health=int(player_health*player_status_effects[leffect].power)
		player_status_effects[leffect].decay-=1
		print("dec="+str(player_status_effects[leffect].decay))
		if player_status_effects[leffect].decay<1:
			print("EEHEHEHEJFDHSKLFHSK")
			
			del player_status_effects[leffect]
	
	if player_x_coordinate==0 and player_y_coordinate==0:
		player_y_coordinate=planet[current_planet].tiles[0][0][current_floor].stair[1]
		player_x_coordinate=planet[current_planet].tiles[0][0][current_floor].stair[0]
	for x in xrange (screen_width-1):
		for y in xrange(screen_width-1):
			
			if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect!=None and planet[current_planet].tiles[x][y][current_floor].status_effect !=0:
				
				planet[current_planet].tiles[x][y][current_floor].status_effect.decay-=1
				if planet[current_planet].tiles[x][y][current_floor].status_effect.decay <=0:
					del(planet[current_planet].tiles[x][y][current_floor].status_effect)
				if hasattr(planet[current_planet].tiles[x][y][current_floor],"status_effect") and planet[current_planet].tiles[x][y][current_floor].status_effect.effect=="fire":
					if x ==player_x_coordinate and y ==player_y_coordinate:
						player_health=int(player_health/2)
					
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
		if weapon.x==player_x_coordinate and weapon.y==player_y_coordinate:
			inventory.append(weapon)
			weapon.x=None
			weapon.y=None
	end=time.clock()
	if (end-start)>longest:
		longest_name="check if player is on weapon"
		longest=end-start		
	start=time.clock()
	if player_radioactivity>0:
		player_health=player_health-(player_radioactivity)
	player_radioactivity=int(player_radioactivity/2)
	for larmour in armours:
		if larmour.x==player_x_coordinate and larmour.y==player_y_coordinate:
			inventory.append(larmour)
			larmour.x=None
			larmour.y=None
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
	
	
	
	for critter in creature[current_planet][current_floor]:
		start=time.clock()
		if hasattr(planet[current_planet].tiles[critter.x][critter.y][current_floor],"status_effect") and planet[current_planet].tiles[critter.x][critter.y][current_floor].status_effect!=None and planet[current_planet].tiles[critter.x][critter.y][current_floor].status_effect.effect=="fire":
			critter.status_effects.append(status_effect("fire",3,1))
		console_write("weenus")
		while len(critter.status_effects)>5:
			del(critter.status_effects[0])
		for other_critter in creature[current_planet][current_floor]:
			if critter.x==other_critter.x and critter.y==other_critter.y and critter!=other_critter and other_critter.health_points>0 and critter.health_points>0  and current_planet==critter.planet and current_floor==critter.floor:
				other_critter.health_points=0
			for fect in critter.status_effects:
				
				if fect.effect=="fire":
					critter.health_points-=1
					if critter.x==other_critter.x:
						if critter.y-1>2 and critter.y-1==other_critter.y:
							other_critter.status_effects.append(status_effect("fire",3,1))
						if critter.y+1<screen_width-2 and critter.y+1==other_critter.y:
							other_critter.status_effects.append(status_effect("fire",3,1))
					if critter.y==other_critter.y:
						if critter.x-1>2 and critter.x-1==other_critter.x:
							other_critter.status_effects.append(status_effect("fire",3,1))
						if critter.x+1<screen_width-2 and critter.x+1==other_critter.x:
							other_critter.status_effects.append(status_effect("fire",3,1))
		end=time.clock()
		if (end-start)>longest:
			longest_name="movin enemies"
			longest=end-start
		for fect in critter.status_effects:
			for fectt in critter.status_effects:
				if fect.effect==fectt.effect:
					del fectt
		if critter.health_points>0  and current_planet==critter.planet and current_floor==critter.floor:
			if critter.x==player_x_coordinate and critter.y ==player_y_coordinate:
				critter.health_points-=weapons[current_weapon].strength
			
			critter.goal_x_coordinate=player_x_coordinate
			critter.goal_y_coordinate=player_y_coordinate
			dorg=0
			if player_health>0:
				dorg=critter.go()
			
			if dorg=="x":	
				critter.move(1,0)
			
			elif dorg=="-x":
					critter.move(-1,0)
			
			elif dorg=="y":
				critter.move(0,1)
			
			elif dorg=="-y":
					critter.move(0,-1)
			if critter.x==player_x_coordinate and critter.y==player_y_coordinate:
				message(critter.name+" did "+str(critter.health_points-armours[current_armor].strength)+" damage to the player")
				player_health-=critter.health_points-armours[current_armor].strength
			if dorg=="x" and critter.x==player_x_coordinate and critter.y==player_y_coordinate:	
				critter.move(-1,0)
			
			elif dorg=="-x" and critter.x==player_x_coordinate and critter.y==player_y_coordinate:
					critter.move(1,0)
			
			elif dorg=="y" and critter.x==player_x_coordinate and critter.y==player_y_coordinate:
				critter.move(0,-1)
			
			elif dorg=="-y" and critter.x==player_x_coordinate and critter.y==player_y_coordinate:
					critter.move(0,1)
			if player_y_coordinate+1<screen_width-2 and critter.x==player_x_coordinate and critter.y==player_y_coordinate+1 and player_radioactivity>50:
				critter.health_points-=(player_radioactivity-50)
			elif player_x_coordinate-1>2 and critter.x==player_x_coordinate-1 and critter.y==player_y_coordinate and player_radioactivity>50:
				critter.health_points-=(player_radioactivity-50)
			elif player_x_coordinate+1<screen_width-2 and critter.x==player_x_coordinate+1 and critter.y==player_y_coordinate and player_radioactivity>50:
				critter.health_points-=(player_radioactivity)
			elif player_y_coordinate-1>2 and critter.x==player_x_coordinate and critter.y==player_y_coordinate-1 and player_radioactivity>50:
				critter.health_points-=(player_radioactivity)
		if critter.health_points>0  and current_planet==critter.planet and current_floor==critter.floor:
			libtcod.map_set_properties(fov_map,critter.x,critter.y,False,False)
		
		if critter.health_points<0  and current_planet==critter.planet and current_floor==critter.floor:
			
			
			
			del critter
			
			
	if sleep!=True and exit==True:
		return True
	end=time.clock()
	if (end-start)>longest:
		longest_name="movin enemies"
		longest=end-start		
	ground_draw(False)

		
for x in xrange(number_of_planets):
	planet.append(Planet(random.randint(-100,100),random.randint(-100,100),False,0,0,monster_name()[1] ))


def message(message):
	global messages, player_health
	messages[0]=messages[1]
	messages[1]=messages[2]
	messages[2]=messages[3]
	messages[3]=message
	first_blank=True
	
	for i in xrange(3):	
		libtcod.console_print(0,0,screen_width+i+1,"                                                                         ")
		libtcod.console_print (0,0,screen_width+i+1,messages[i])
			
			
			
		libtcod.console_flush()
	
def space_draw():
	
	for x in xrange(screen_width):
		for y in xrange(int(screen_width)):
			
				
			libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
	
	libtcod.console_flush()
	
	
	
	

	for x in range(len(starx)):		
				
		
		if starx[x]<bottom_right[0] and stary[x]<bottom_right[1] and starx[x]>top_left[0] and stary[x]>top_left[1]:
						
			libtcod.console_put_char(0, starx[x]-top_left[0],stary[x]-top_left[1], ".", libtcod.BKGND_NONE)
	
			
	
	
	
	for x in xrange(number_of_planets):
		
		if planet[x].x<bottom_right[0] and planet[x].y<bottom_right[1] and planet[x].x>top_left[0] and planet[x].y>top_left[1]:
			libtcod.console_set_default_foreground(0, planet[x].color)
			libtcod.console_put_char(0, planet[x].x-top_left[0],planet[x].y-top_left[1], "O", libtcod.BKGND_NONE)
	libtcod.console_set_default_foreground(0, libtcod.white)
	libtcod.console_put_char(0, spacex-top_left[0], spacey-top_left[1], "$", libtcod.BKGND_NONE)
	
	
			
	
	
	
	libtcod.console_flush()
#defines how the game plays in space
def spaceplay():
	global planet,mode, player_x_coordinate,player_y_coordinate, number_of_planets, spacexmax,spacexmin,spaceymax,spaceymin
	print(str(spacex)+"z")
	space_draw()
	if spacex>spacexmax:
		spacexmax=spacex
	if spacex<spacexmin:
		spacexmin=spacex
	if spacey>spaceymax:
		spaceymax=spacey
	if spacey<spaceymin:
		spacexmax=spacex
	exit=handle_spacekey()
	for i in xrange(number_of_planets):
		if spacex==planet[i].x and spacey==planet[i].y :
			if planet[i].visited==False:
				current_planet=i
				player_x_coordinate=random.randint(0,screen_width-1)
				player_y_coordinate=random.randint(0,screen_width-1)
				planet[i].player_x_coordinate=player_x_coordinate
				planet[i].player_y_coordinate=player_y_coordinate
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
			
			player_x_coordinate=planet[current_planet].tiles[0][0][current_floor].stairu[0]
			player_y_coordinate=planet[current_planet].tiles[0][0][current_floor].stairu[1]
			
			
			
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


placex=0
placey=0


	
creature=[]
def monster_death(x,y):
	if random.randint(0,1)==0:
		weapons.append(Weapon("weapon"+str(random.randint(0,10000)),random.randint(1,9),x,y))
	else:
		armours.append(Armor("armor"+str(random.randint(0,10000)),random.randint(1,9),x,y))
def make_all_enemies_on_floor(enemies_spawned):
	global creature,current_floor,current_planet
	
	
	
	
	
	for l in range(enemies_spawned):
		
		
			
			
		enemyc=[random.randint(2, screen_width-2), random.randint(2, screen_width-2)]

		while planet[current_planet].tiles[enemyc[0]][enemyc[1]][current_floor].blocked==True:
			enemyc[0]=random.randint(2, screen_width-2)
			enemyc[1]=random.randint(2, screen_width-2)
		while len(creature[current_planet])<current_floor+1:
			creature[current_planet].append([0])
		
		creature[current_planet][current_floor].append(monster(enemyc[0],enemyc[1],player_x_coordinate,player_y_coordinate, monster_name()[0],monster_name()[1],random.randint(1,9),current_floor,current_planet ))
	
	del creature[current_planet][current_floor][0]
	
	
	
def shooting(currentx,currenty, x,y):
	loops=1
	monster_hit=False
	
	while  random.randint(1,loops)<5 and currentx+x<screen_width-1 and currentx+x>=0 and currenty+y>=0 and currenty+y<screen_width-1 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True and monster_hit==False:
		if currentx!=player_x_coordinate or currenty!=player_y_coordinate:
			libtcod.console_set_default_foreground(0, libtcod.red)	
			libtcod.console_put_char(0,currentx,currenty,"~", libtcod.BKGND_NONE)
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
				if planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True:
					creature[current_planet][current_floor][i].x+=x
					creature[current_planet][current_floor][i].y+=y
				
				creature[current_planet][current_floor][i].health_points-=random.randint(1,5)*(weapons[current_weapon].strength)
				
				i=enemies_spawned
	if random.randint(1,loops)<5 and random.randint(1,10)!=1 and currentx+x<screen_width-1 and currentx+x<screen_width-1 and currenty+y<screen_width-1 and currentx+x>=0 and currenty+y>=0 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked==True:
		planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
def space_shooting(currentx,currenty, x,y):
	loops=1
	monster_hit=False
	
	while  random.randint(1,loops)<5 and currentx+x<screen_width-1 and currentx+x>=0 and currenty+y>=0 and currenty+y<screen_width-1 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True and monster_hit==False:
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
			
			if planet[i].x==currentx and planet[i].y==currenty:
				message(planet[i].name+" has been hit")
				monster_hit=True
				del planet[i]
				
				
				
				
				
				i=number_of_planets
	
def throwing(chemical,currentx,currenty, x,y):
	loops=1
	monster_hit=False
	
	while  random.randint(1,loops)<5 and currentx+x<screen_width-1 and currentx+x>=0 and currenty+y>=0 and currenty+y<screen_width-1 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked!=True and monster_hit==False:
		if currentx!=player_x_coordinate or currenty!=player_y_coordinate:
			libtcod.console_set_default_foreground(0, libtcod.blue)	
			libtcod.console_put_char(0,currentx,currenty,"~", libtcod.BKGND_NONE)
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
					creature[current_planet][current_floor][i].health_points=player_health*2
					
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
	if random.randint(1,loops)<5 and random.randint(1,10)!=1 and currentx+x<screen_width-1 and currentx+x<screen_width-1 and currenty+y<screen_width-1 and currentx+x>=0 and currenty+y>=0 and planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked==True:
		planet[current_planet].tiles[currentx+x][currenty+y][current_floor].blocked=False
def inventory_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player_health
	
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
				current_weapon=currentselection
			elif isinstance(inventory[currentselection],Armor):
				current_armor=currentselection
			elif isinstance(inventory[currentselection],Chemical):
				if inventory[currentselection].name=="mundinal":
					player_health=player_health*2
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
				elif inventory[currentselection].name=="caecilem":
					player_status_effects.append(status_effect("blind",12,1))
					
					del inventory[currentselection]
					currentselection=0
				elif inventory[currentselection].name=="incendite":
					planet[current_planet].tiles[player_x_coordinate][player_y_coordinate][current_floor].status_effect=status_effect("fire",6,1)
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
					if hasattr(planet[current_planet].tiles[player_x_coordinate][player_y_coordinate][current_floor], "status_effect") and planet[current_planet].tiles[player_x_coordinate][player_y_coordinate][current_floor].status_effect!=None and planet[current_planet].tiles[player_x_coordinate][player_y_coordinate][current_floor].status_effect.effect=="fire":
						del planet[current_planet].tiles[player_x_coordinate][player_y_coordinate][current_floor].status_effect
					
					del inventory[currentselection]
		elif key.c==ord("z"):
			mode="ground"
		
			
	
		libtcod.console_flush()
def mix_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player_health, selected
	
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
		elif key.c==ord("z"):
			mode="ground"
		
			
	
		libtcod.console_flush()
def incinerate_screen(currentselection):
	global inventory, mode, current_weapon,current_armor, player_health
	
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
	
	while mode=="status":
		for x in xrange(screen_width):
			for y in xrange(screen_width):
				libtcod.console_put_char(0, x, y, " ", libtcod.BKGND_NONE)
		
		
			
		libtcod.console_print(0,0,0,"You have a "+inventory[current_weapon].name+" equipped.")
		libtcod.console_print(0,0,1,"You have a "+inventory[current_armor].name+" equipped as armour.")
		libtcod.console_print(0,0,2,"You are on planet "+planet[current_planet].name)
		libtcod.console_print(0,0,3,"You have "+str(player_health)+" health.")
		charactercreation()
		key = libtcod.console_wait_for_keypress(False)
		
		
		if key.c==ord("z"):
			mode="ground"
		
			
	
		libtcod.console_flush()
def space_inventory_screen():
	global inventory, mode, current_weapon,current_armor, player_health
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
			mode="ground"
		
			
	
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
			mode="ground"
		
			
	
		libtcod.console_flush()
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
	elif mode=="mix":
		mix_screen(0)
	elif mode=="incinerate":
		incinerate_screen(0)
	elif mode=="space_inventory1":
		space_inventory_screen()
sys.stderr.close()
sys.stderr = sys.__stderr__	
		
