import random
#Aleix Part

#Arnau Part
#bot donarà dos números has de triar un número que estigui dintre els perametres.
#bot dirà números random intenta no escriure el mateix sinó perds.

num = int(input("Escriu un número de 1 al 20 --> "))
bot1 = random.randint(1,20)
bot2 = random.randint(1,20)
if (bot1>bot2):
    aux = bot1
    bot1 = bot2
    bot2 = aux
elif(num < bot1 or num > bot2):
    print(f"El {num} no estava dins els parametres, has perdut!! :C")
else:
     print(f"El {num} estava dins els parametres, has guanyat!! :D")

print(f"El prametre és {bot1,bot2}")
#
#David Part
