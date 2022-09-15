# Definimos una fn que retorna hh:mm:ss.ss si se ingresa segundos
# y retorna seundos si se ingres hh:mm:ss

def reloj(*argumento):
    if len(argumento) == 1:
        segundos = argumento[0]
        horas = int(segundos / 3600)
        minutos = (segundos/3600-horas) * 60
        segundos = (minutos - int(minutos)) * 60
        return f"{horas}:{int(minutos)}:{round(segundos,0)}"

    else:
        segundos = argumento[0] * 3600 + argumento [1] * 60 + argumento [2]
    return segundos

print(reloj(1,23,20))
print(reloj(5000))