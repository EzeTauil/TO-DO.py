tasks=[]
count=int(input("La cantidad de Eventos que quiero agendar : "))
file=open("tareas.txt","w",encoding="utf8")
for i in range(count):
    new_element=input("Que querés agendar? : ") #Se repite las count veces
    tasks.append(new_element)
    file.write(new_element+'\n')
print(tasks)
file.close()