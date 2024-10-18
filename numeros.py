# Definimos la lista de valores romanos
valores_romanosen = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def detectar_numeros_romanos_en_frases(frases):
    numeros_romanosen_en_frases = []
    
    for frase in frases:
        # Convertimos la frase a mayúsculas
        frase = frase.upper()
        
        # Filtramos solo los caracteres que son numeros romanos
        romanos_en_frase = ''.join([char for char in frase if char in valores_romanosen])
        
        # Añadimos el número romano encontrado o None si no hay
        numeros_romanosen_en_frases.append(romanos_en_frase if romanos_en_frase else None)
    
    return numeros_romanosen_en_frases

def es_numero_romano_valido(numero_romano):
    contador = {key: 0 for key in valores_romanosen.keys()}
    
    for i in range(len(numero_romano)):
        char = numero_romano[i]
        
        # Verifica si el carácter es un número romano valido
        if char not in valores_romanosen:
            return False
        
        # Regla de no mas de 3 caracteres iguales
        if char in 'IXC':
            if contador[char] == 3:
                return False
        
        if char in 'VLD':
            if contador[char] > 0:
                return False
        
        # Incrementar el contador del carácter actual
        contador[char] += 1

        # Regla de sustraccion válida
        if i > 0 and valores_romanosen[char] > valores_romanosen[numero_romano[i - 1]]:
            if not ((numero_romano[i - 1] == 'I' and char in 'VX') or
                    (numero_romano[i - 1] == 'X' and char in 'LC') or
                    (numero_romano[i - 1] == 'C' and char in 'DM')):
                return False
            
            # Validacion adicional para evitar combinaciones no validas
            if char == 'L' and numero_romano[i - 1] == 'X':
                return False
            if char == 'C' and numero_romano[i - 1] in 'XL':
                return False
            if char == 'D' and numero_romano[i - 1] == 'C':
                return False
            if char == 'M' and numero_romano[i - 1] in 'CD':
                return False

    return True

def convertir_romano_a_decimal(numero_romano):
    total = 0
    longitud = len(numero_romano)
    
    for i in range(longitud):
        valor_actual = valores_romanosen[numero_romano[i]]
        
        # Si no es el último carácter y el siguiente es mayor, restamos el valor actual
        if i < longitud - 1 and valores_romanosen[numero_romano[i + 1]] > valor_actual:
            total -= valor_actual
        else:
            total += valor_actual

    return total

def ajustar_numero_romano(numero_romano):
    # Si el número romano no es válido, eliminamos caracteres de derecha a izquierda
    while not es_numero_romano_valido(numero_romano) and len(numero_romano) > 0:
        numero_romano = numero_romano[:-1]  # Eliminar el ultimo carácter

        # Validación adicional para evitar combinaciones no validas
        if "IVI" in numero_romano or "IXI" in numero_romano or "IIV" in numero_romano:
            numero_romano = numero_romano[:-1]  # Eliminar otro carácter si se encuentra un patron no válido
    
    return numero_romano

# Ejemplo de uso
palabras = ["Civil", "Pixel", "Paco", "Hijo", "Toxico", "Camion"]
numeros_romanos_en_frases = detectar_numeros_romanos_en_frases(palabras)

for frase, numero_romano in zip(palabras, numeros_romanos_en_frases):
    print(f"Palabra: '{frase}'")
    if numero_romano:
        valido = es_numero_romano_valido(numero_romano)
        print(f"  Número romano encontrado: {numero_romano}, válido: {valido}")
        
        # Ajustamos el número romano si no es válido
        if not valido:
            numero_romano = ajustar_numero_romano(numero_romano)
            valido = es_numero_romano_valido(numero_romano)
        
        print(f"  Número romano ajustado: {numero_romano}, válido: {valido}")
        
        if valido:
            decimal = convertir_romano_a_decimal(numero_romano)
            print(f"  Valor decimal: {decimal}")
    else:
        print("  No se encontró ningún número romano.")
