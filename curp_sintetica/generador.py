
import random

def generar_curp_apocrifa(nombre, fecha_yyyy_mm_dd, sexo):
    """
    Toma datos básicos y devuelve 18 caracteres de pura ficción burocrática.
    """
    nombre = nombre.strip().upper()
    sexo = sexo.strip().upper()
    
    if not nombre or nombre == "NOMBRE COMPLETO...":
        raise ValueError("Se requiere un nombre válido para procesar la identidad.")

    partes = nombre.split()
    paterno = partes[0] if len(partes) > 0 else "X"
    materno = partes[1] if len(partes) > 1 else "X"
    nombres = partes[2] if len(partes) > 2 else "X"
    
    letras = (paterno[:2] + materno[:1] + nombres[:1]).ljust(4, 'X').upper()
    fecha_curp = fecha_yyyy_mm_dd[2:4] + fecha_yyyy_mm_dd[5:7] + fecha_yyyy_mm_dd[8:10] if len(fecha_yyyy_mm_dd) == 10 else "000000"
    sexo_letra = "M" if sexo == "MUJER" else "H" if sexo == "HOMBRE" else "X"
    
    relleno = "GT" + "X" + "X" + "X" + str(random.randint(10, 99))
    
    return f"{letras}{fecha_curp}{sexo_letra}{relleno}"
