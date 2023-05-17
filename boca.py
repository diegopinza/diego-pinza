historia_libertadores = [
    {
        'año': 2000,
        'eliminado': None,
        'resultado': 'Campeón'
    },
    {
        'año': 2001,
        'eliminado': 'Cuartos de final',
        'resultado': None
    },
    {
        'año': 2003,
        'eliminado': None,
        'resultado': 'Campeón'
    },
    {
        'año': 2004,
        'eliminado': 'Cuartos de final',
        'resultado': None
    },
    {
        'año': 2005,
        'eliminado': None,
        'resultado': 'Campeón'
    },
    {
        'año': 2007,
        'eliminado': 'Semifinales',
        'resultado': None
    },
    {
        'año': 2008,
        'eliminado': 'Octavos de final',
        'resultado': None
    },
    {
        'año': 2012,
        'eliminado': 'Final',
        'resultado': None
    },
    {
        'año': 2013,
        'eliminado': None,
        'resultado': 'Campeón'
    },
    {
        'año': 2018,
        'eliminado': 'Cuartos de final',
        'resultado': None
    }
]

# Imprimir la historia de Boca Juniors en la Copa Libertadores después de 2000
print("Historia de Boca Juniors en la Copa Libertadores después de 2000:\n")
for edicion in historia_libertadores:
    año = edicion['año']
    eliminado = edicion['eliminado']
    resultado = edicion['resultado']
    
    print(f"Año: {año}")
    if eliminado:
        print(f"Eliminado: {eliminado}")
    if resultado:
        print(f"Resultado: {resultado}")
    print("-----------------------------")
