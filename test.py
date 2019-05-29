#define destinations in system
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'So Paulo, Brazil', 'Cairo, Egypt']
#define test_traveler[name, destination, [interest(s)]]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
#match dest w/in destinations and return destination index
def get_destination_index(dest):
  destination_index = destinations.index(dest)
  return destination_index
#find traveler destination (index[1]) and match with destinations return destinations index
def get_traveler_location(traveler):
  traveler_dest = traveler[1]
  traveler_dest_index = get_destination_index(traveler_dest)
  return traveler_dest_index
#test_dest_index = get_traveler_location(test_traveler)
#print(test_dest_index)

#attractions will be a list of empty lists, w/ 1 empty list/value in destinations
attractions = [[] for x in destinations]
#add_attraction matches dest w/ destinations w/ ValueError msg.
def add_attraction(dest, attrac):
  try:
    dest_index = get_destination_index(dest)
  except ValueError:
    return print('Error: destination list does not contain '+ str(dest))
  #w/ no value error then attrac is appended into the corresponding dest_index list in attractions
  attractions_for_dest = attractions[dest_index]
  attractions_for_dest.append(attrac)
  return
#attractions schema: [[attraction(s),[interest(s)]],[...]]
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#find_attractions will return[[attraction, [interest(s)]],[ect..]]
def find_attractions(dest, interests):
  matched_attractions = []
  dest_index = get_destination_index(dest)
  dest_attractions = attractions[dest_index]
  #dest_attractions is the destination attractions via corresponding index [[the destination attraction + [interest(s)]], [ect[ect]]] 
  for attns in dest_attractions:
    #attns is [the destination attraction + [interest(s)]]
    attraction_intrts = attns[1] #var for attraction's interests
    #check if each interest is in attraction interests
    for intrt in interests: 
      if intrt in attraction_intrts:
        #then append empty list w/ attns
        matched_attractions.append(attns[0])
  return matched_attractions
#la_test = find_attractions("Los Angeles, USA", ['art'])
#print(la_test)
#get_traveler_attractions
def gen_traveler_attractions_str(tvlr):
  tvlr_dest = tvlr[1]
  tvlr_intrts = tvlr[2]
  tvlr_attractions = find_attractions(tvlr_dest, tvlr_intrts) #returns list of attractions for tvlr_dest & intrts
  #concatenating welcome_string to include tvlr name, dest, and attractions w
  welcome_string = 'Hi '+tvlr[0]+" we think you'll like these places around "+tvlr_dest+":"
  for attn in tvlr_attractions:
    welcome_string += " The " + str(attn) + ","
  welcome_string += " enjoy!"
  return welcome_string
#smill_test = gen_traveler_attractions_str(['Dereck Smill', 'Paris, France', ['monument']])
#print(smill_test)
