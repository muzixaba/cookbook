from bottle import run, get, post, delete, request

animals = [
    {'name': 'Ellie', 'type': 'Elephant'},
    {'name': 'Python', 'type': 'Snake'},
    {'name': 'Zed', 'type': 'Zebra'}
]

@get('/animal')
def get_all():
    return {'animals': animals}

@get('/animal/<name>')
def get_animal(name):
    the_animal = [x for x in animals if x['name'] == name]
    return {'animal': the_animal[0]}

@post('/animal')
def add_animal():
    new_animal = {
        "name": request.json.get("name"),
        "type": request.json.get("type")
        }
    animals.append(new_animal)
    return {'animals': animals}

@delete('/animal/<name>')
def delete_animal(name):
    the_animal = [x for x in animals if x['name']==name]
    animals.remove(the_animal[0])
    return {'animals': animals}

run(reloader=True, debug=True)