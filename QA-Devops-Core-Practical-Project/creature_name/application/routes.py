from flask import Flask, request, Response
from continent.application.routes import continent
from creature_type.application.routes import type

@app.route('/name',methods=['POST'])
def name():
    creature_name = request.data.decode('utf-8')
    if continent == 'Europe':
        if type == 'Mammal':
            creature_name = 'Red Squirrel'
        elif type == 'Reptile':
            creature_name = 'European Green Lizard'
        elif type == 'Amphibian':
            creature_name = 'Common Toad'
        elif type == 'Bird':
            creature_name = 'Robin'
        elif type == 'Fish':
            creature_name = 'Dover Sole'
    elif continent == 'Africa':
        if type == 'Mammal':
            creature_name = 'African Elephant'
        elif type == 'Reptile':
            creature_name = 'Dwarf Crocodile'
        elif type == 'Amphibian':
            creature_name = 'Mozambique Tree Frog'
        elif type == 'Bird':
            creature_name = 'Egyptian Goose'
        elif type == 'Fish':
            creature_name = 'Red Zebra Cichlid'
    elif continent == 'Asia':
        if type == 'Mammal':
            creature_name = 'Giant Panda'
        elif type == 'Reptile':
            creature_name = 'Gharial'
        elif type == 'Amphibian':
            creature_name = 'Asian Bullfrog'
        elif type == 'Bird':
            creature_name = 'Mandarin Duck'
        elif type == 'Fish':
            creature_name = 'Japanese Dragonet'
    elif continent == 'North America':
        if type == 'Mammal':
            creature_name = 'North American Beaver'
        elif type == 'Reptile':
            creature_name = 'Gopher Tortoise'
        elif type == 'Amphibian':
            creature_name = 'Spotted Salamander'
        elif type == 'Bird':
            creature_name = 'Bald Eagle'
        elif type == 'Fish':
            creature_name = 'Leopard Shark'
    elif continent == 'South America':
        if type == 'Mammal':
            creature_name = 'Big-eared Opossum'
        elif type == 'Reptile':
            creature_name = 'Boa Constrictor'
        elif type == 'Amphibian':
            creature_name = 'Oophaga'
        elif type == 'Bird':
            creature_name = 'Andean Flamingo'
        elif type == 'Fish':
            creature_name = 'Piranha'
    elif continent == 'Australasia':
        if type == 'Mammal':
            creature_name = 'Koala'
        elif type == 'Reptile':
            creature_name = 'Tuatara'
        elif type == 'Amphibian':
            creature_name = 'Leaf Green Tree Frog'
        elif type == 'Bird':
            creature_name = 'Kakapo'
        elif type == 'Fish':
            creature_name = 'Golden Perch'
        return Response(name, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
