

#Ejercicio 1

def sortVocal(toSort):
    words = toSort.split()
    vocals = ["a","e","i","o","u"]
    if words[1][0] in vocals: return True
    else: return False


#Ejercicio 10

def display_round(current):
      """
      Imprime en consola las estadisticas totales de los jugadores utilizando los valores enviados.

      :param current: Diccionario con los valores totales de cada jugador.
      """
      sortedCurrent = sorted(current,key=lambda x: current[x]['points'], reverse=True)
      print(f"Nombre   Kills   Asistencias   Muertes   MVP's   Puntos totales\n")
      print("-------------------------------------------------")
      for elem in sortedCurrent:
            print (f"{elem}   {current[elem]['kills']}   {current[elem]['assists']}   {current[elem]['deaths']}   {current[elem]['MVPS']}   {current[elem]['points']}")
      print("-------------------------------------------------")      
      return

def process_round(currentRound, total):
     """
      Procesa la ronda actual, determina el MVP, y luego envia los datos actualizados a "display_round" con el proposito de imprimir el ranking.

      :param currentRound: Diccionario con las estadisticas de los jugadores, teniendo en cuenta unicamente la ronda actual.
      :param total: Diccionario con las estadisticas de los jugadores, teniendo en cuenta todas las rondas previas.
     """
     currLeader = "dummyvalue"
     currLPoints = -99999
     for elem in currentRound:
           total[elem]['kills'] =+ currentRound[elem]['kills'] 
           total[elem]['assists'] =+ currentRound[elem]['assists']
           actualPoints = (currentRound[elem]['kills']*3 + currentRound[elem]['assists'])
           if (currentRound[elem]['deaths']): 
                total[elem]['deaths'] += 1
                actualPoints -= 1  
           total[elem]['points'] =+ actualPoints     
           if actualPoints>currLPoints:
                 currLeader=elem
                 currLPoints=actualPoints           
     total[currLeader]['MVPS'] += 1            
     display_round(total)     
