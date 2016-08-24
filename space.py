
def spaceplay():
	global planet,mode, player, number_of_planets, spacexmax,spacexmin,spaceymax,spaceymin
	DISPLAYSURF.fill((0,0,0))
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