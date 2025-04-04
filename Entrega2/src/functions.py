

#Ejercicio 1

def sortVocal(toSort):
    words = toSort.split()
    vocals = ["a","e","i","o","u"]
    if words[1][0] in vocals: return True
    else: return False


#Ejercicio 10

def display_round(current):
      """
      Imprime en consola las estadisticas totales de los jugadores ordenado en manera de descendencia de puntos utilizando los valores enviados.

      :param current: Diccionario con los valores totales de cada jugador.
      """
      #Se ordena el diccionario 'current' (el diccionario de totales) por el valor de 'points' de cada jugador.
      sortedCurrent = sorted(current,key=lambda x: current[x]['points'], reverse=True)
      #Se imprime el encabezado de la tabla.
      print(f"Nombre   Kills   Asistencias   Muertes   MVP's   Puntos totales\n")
      print("-------------------------------------------------------------------")
      #Se imprime el nombre de cada jugador y sus estadisticas totales.
      for elem in sortedCurrent:
            print(f"{elem:<8}{current[elem]['kills']:>5}{current[elem]['assists']:>12}{current[elem]['deaths']:>10}{current[elem]['MVPS']:>8}{current[elem]['points']:>15}")
      print("-------------------------------------------------------------------")      
      return

def process_round(currentRound, total, actualround):
     """
      Procesa la ronda actual, actualiza los datos del diccionario total, determina el MVP, muestra la ronda y su MVP, 
      y luego envia los datos actualizados a "display_round" con el proposito de imprimir el ranking.

      :param currentRound: Diccionario con las estadisticas de los jugadores, teniendo en cuenta unicamente la ronda actual.
      :param total: Diccionario con las estadisticas de los jugadores, teniendo en cuenta todas las rondas previas.
      :param actualround: valor int de la ronda actual, utilizado para "display_round", como contador de ronda.
     """
     currLeader = "dummyvalue - Si se imprime esto se debe a un error."
     currLPoints = -99999
     for elem in currentRound:
           #Se actualizan las estadisticas totales de kills y assists.
           total[elem]['kills'] += currentRound[elem]['kills'] 
           total[elem]['assists'] += currentRound[elem]['assists']
           #Se cuentan los puntos de la ronda actual y se almacenan en 'actualPoints'.
           actualPoints = (currentRound[elem]['kills']*3 + currentRound[elem]['assists'])
           #Si el jugador ha muerto, se le resta un punto y se le suma uno al total de muertes.
           if (currentRound[elem]['deaths']): 
                total[elem]['deaths'] += 1
                actualPoints -= 1  
           #Se actualizan las estadisticas totales de puntos.     
           total[elem]['points'] += actualPoints     
           #Se determina si el jugador es el MVP de la ronda, comparando los puntos actuales con los puntos del MVP actual.
           if actualPoints>currLPoints:
                 currLeader=elem
                 currLPoints=actualPoints           
     #Se utiliza la variable 'currLeader' para actualizar el total de MVP's del jugador correspondiente.            
     total[currLeader]['MVPS'] += 1
     #Se imprime el numero de la ronda y el nombre del MVP de la ronda.
     print(f"Ronda {actualround}")
     print(f"MVP de la ronda: {currLeader}")            
     display_round(total)
     #Se suma uno al contador de ronda, para que la siguiente vez que se imprima el numero de ronda correcto.
     actualround+=1    
     return actualround  
