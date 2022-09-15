f = open("03_archivo.txt", "r+")
f.write("Esto es un texto1\n")
f.write("Esto es un texto2\n")
f.write("Esto es un texto3\n")
f.write("Esto es un texto4\n")
f.write("Esto es un texto5\n")
f.write("Esto es un texto6\n")
f.write("Esto es un texto7\n")
f.write("Esto es un texto8\n")
f.write("Esto es un texto9\n")
f.write("Esto es un texto10\n")
f.write("Esto es un texto11\n")
f.write("Esto es un texto12\n")
f.write("Esto es un texto13\n\n")
f.close()

f = open("03_libreria.txt","w")
while True:
  nombre = input("Ingrese Nombre <S para Salir>: ")
  if nombre.lower() == "s":
    break
  apellido = input("Ingrese Apellido: ")
  dni = input("Ingrese DNI: ")
  f.write("Nombre :"+ nombre + ","+ "Apellido:" +apellido +","+"DNI: f" + dni + "\n")
f.close()

f = open("03_libreria.txt","r")
contenido = f.read()
print (contenido)