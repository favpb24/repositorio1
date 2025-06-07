diccionario={
"lol": "Respuesta a algo gracioso",
"cringe": "Pena ajena",
"rofl": "Una respuesta a una broma",
"sheesh": "Ligera desaprobación",
"creepy": "Aterrador o siniestro",
"spoiler": "revelar importante de una serie o película antes de que alguien vea",
"tryhard": "alguien que se esfuerza demasiado en cualquier juego",
"banear": "Botar a alguien permanentemente de un juego o servidor",
"parry" : "Hacer un bloqueo perfecto a un ataque",
"bot": "persona bien mala en un juego",
"wow": "Sorprenderse de algo"
}

pregunta = input("Que palabra quieres saber?")
if pregunta in diccionario.keys():
  print(diccionario[pregunta])
else:
  print("esa palabra no existe")
                 


      
