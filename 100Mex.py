#Metodo anterior aplicado a funciones
global jugadores #Variable global para designar a los jugadores y sus puntuaciones
jugadores = {'Pedro':[10], 'Karla':[30], 'Luis':[25], 'Samantha':[50]}#En un diccionario se guarda a los jugadores y sus puntuaciones
Pregunta1 = {'Rusia':[50], 'Canada':[30], 'China':[10]}
Lista = [1,2,3]
dos = []
randoms = []
import time
from IPython.display import clear_output
import random

def buscar(nombre):
  respuesta = nombre in jugadores
  if respuesta == False:
    opc = int(input("El jugador {} no esta registrado.\n\n¿Desea registrarlo?\n\n1. Si\n2. No\n\nRespuesta: ".format(nombre)))
    if opc == 1:
      agregar(nombre)
    else:
      print("\nRegresando al menú principal...\n")
      time.sleep(1.5)
      clear_output()
      principal()
  return nombre

def puntuaciones(nombre):
  buscar(nombre)
  if jugadores[nombre]:
    print("\nJugador: {}\nPuntuaciones: {}\n".format(nombre, jugadores[nombre]))
    option = input("Ingrese cualquier tecla para regresar al menu principal.")
    option == 1
    principal()
  else:
    print("El jugador {} aún no tiene puntuaciones registradas.".format(nombre))
  time.sleep(1.5)
  clear_output()

def agregar(nombre):
  jugadores[nombre] = []
  print("\nEl jugador {}, fue agregado exitosamente.\n".format(nombre))
  time.sleep(1.5)
  clear_output()

def borrar(nombre):
  buscar(nombre)
  del jugadores[nombre]
  print("\n\nSe eliminó al jugador {}.".format(nombre))
  time.sleep(1.5)
  clear_output()

def jugar(jugadores):
  r = input("Ingrese el nombre del jugador 1: ")
  dos.append(r)
  if r not in jugadores:
    principal()
  if r in jugadores:
      s = input("Ingrese el nombre del jugador 2: ")
      print("Bienvenidos a 100 drogadictos dijieron, sortearemos quien ira primero")
      dos.append(s)
      rand = random.choice([r,s])
      randoms.append(rand)
      print("El primero en responder sera: ", rand)
      if r in randoms:
        randoms.append(s)
      else:
        randoms.append(r)      
      preguntas()

def preguntas():
  while Lista:
    leni = len(Lista) - 1
    print("Primera pregunta: \nPaís más grande:\n1.-Rusia\n2.-Canada\n3.-China")
    rop = input("\nTu respuesta es: ")
    if rop in Pregunta1:
      print("Le atinaste ")
      jugadores[randoms[0]].append(Pregunta1[rop][0])  # Accede al valor dentro de la lista y lo agrega
      print("¡Puntuación agregada con éxito!")
      print(f"Puntuaciones de {randoms[0]}: {jugadores[randoms[0]]}")
      print("Jugadoresrandom",randoms)

      print(dos)
      time.sleep(2)
    else:
      Lista.pop()
      print("Te equivocaste, te quedan ",leni)
      time.sleep(2)
  print("No le atinaste, te quedan 0 vidas\nLe toca a ",dos[1])
  rop = input("\nTu respuesta es: ")
  if rop in Pregunta1:
    print("le atinaste ")
    jugadores[randoms[1]].append(Pregunta1[rop][0])  # Accede al valor dentro de la lista y lo agrega
    print("¡Puntuación agregada con éxito!")
    print(f"Puntuaciones de {randoms[1]}: {jugadores[randoms[1]]}")
    print(dos)
    time.sleep(2)

def preguntabien():
  print("va")

def pedirNumero():
  correcto=False
  opc=0
  while(not correcto):
      try:
          print("\033[1;35m"+"     __   __   ____   ___   _   _   _ ")
          print("\033[1;35m"+"    |  \_/  | |  __| |   \ | | | | | |")
          print("\033[1;35m"+"    | |\_/| | |  __| | |\ \| | | |_| |")
          print("\033[1;35m"+"    |_|   |_| |____| |_| \___| |_____|")

          opc = int(input("\n¿Que desea hacer?\n\n1. Verificar puntuaciones\n2. Agregar un nuevo jugador\n3. Borrar un jugador\n4. Jugar\n5. Salir\n\nOpción: "))
          correcto=True
      except ValueError:
          print('Error, introduce un numero entero')
          time.sleep(1.5)
          clear_output()    
  return opc     
      
      
      

def principal():
  clear_output()
  opc = pedirNumero()
  time.sleep(1.5)
  clear_output()
  if opc == 1 or opc == 2 or opc == 3:
    nombre = input("\nIngrese el nombre del jugador: ").capitalize()

  if opc == 1:
    puntuaciones(nombre)
  elif opc == 2:
    agregar(nombre)
  elif opc == 3:
    borrar(nombre)
  elif opc == 4:
    jugar(jugadores)
  elif opc == 5:
    clear_output() 
  elif opc == 6:
    preguntas()
    print("\033[3;32m"+"¡Que tenga un buen día!\n¡Gracias por jugar! :)\nSaliendo...")
  else:
    print("\033[1;31m"+"Opción no válida, intentelo de nuevo.\nPor favor introduzca una opción valida.")
    time.sleep(3)
    clear_output()    
    principal()

  if opc == 1 or opc == 2 or opc == 3 or opc == 4:
    principal()
  

principal()
