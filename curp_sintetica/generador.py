import random
import re

def _primera_vocal_interna(palabra):
    match = re.search(r'[AEIOU]', palabra[1:])
    return match.group(0) if match else 'X'

def _primera_consonante_interna(palabra):
    match = re.search(r'[BCDFGHJKLMNÑPQRSTVWXYZ]', palabra[1:])
    return match.group(0) if match else 'X'

def generar_curp_realista(nombres, paterno, materno, fecha_yyyy_mm_dd, sexo, clave_estado):
    nombres = nombres.strip().upper() if nombres else "X"
    paterno = paterno.strip().upper() if paterno else "X"
    materno = materno.strip().upper() if materno else "X"
    
    # 1. Letras iniciales (Primera del paterno, primera vocal interna del paterno, primera materno, primera nombre)
    l1 = paterno[0]
    l2 = _primera_vocal_interna(paterno)
    l3 = materno[0]
    l4 = nombres[0]
    
    # 2. Fecha YYMMDD
    if len(fecha_yyyy_mm_dd) == 10:
        fecha = fecha_yyyy_mm_dd[2:4] + fecha_yyyy_mm_dd[5:7] + fecha_yyyy_mm_dd[8:10]
    else:
        fecha = "000000"
        
    # 3. Sexo
    s = "M" if sexo.upper() == "MUJER" else "H"
    
    # 4. Estado (Acepta la clave de 2 letras, ej: GT)
    est = clave_estado.strip().upper()
    if len(est) != 2: 
        est = "NE" # Nacido en el extranjero
        
    # 5. Consonantes internas
    c1 = _primera_consonante_interna(paterno)
    c2 = _primera_consonante_interna(materno)
    c3 = _primera_consonante_interna(nombres)
    
    # 6. Homoclave y dígito verificador aleatorios (la firma de que sigue siendo falsa)
    homoclave = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    digito = str(random.randint(0, 9))
    
    return f"{l1}{l2}{l3}{l4}{fecha}{s}{est}{c1}{c2}{c3}{homoclave}{digito}"
