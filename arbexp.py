import graphviz

def graficar_arbol(expresion):
    # Crear un nuevo gráfico
    dot = graphviz.Digraph(comment='Arbol de expresiones')

    # Función recursiva para crear el árbol
    def crear_arbol(subexpresion):
        # Obtener el operador principal de la subexpresión
        operadores = ['*', '/', '+', '-']
        for operador in operadores:
            if operador in subexpresion:
                indice = subexpresion.index(operador)
                break
        else:
            # La subexpresión es un número
            dot.node(subexpresion, subexpresion)
            return subexpresion

        # Crear un nuevo nodo para el operador
        operador_nodo = f'{operador}_{indice}'
        dot.node(operador_nodo, operador)

        # Dividir la subexpresión en operandos y llamar a la función recursivamente para cada operando
        operandos = [subexpresion[:indice], subexpresion[indice+1:]]
        for i, operando in enumerate(operandos):
            nodo_operando = crear_arbol(operando)
            dot.edge(operador_nodo, nodo_operando, f'{i}')

        # Devolver el nodo del operador
        return operador_nodo

    # Llamar a la función para crear el árbol
    crear_arbol(expresion)

    # Guardar el archivo DOT
    dot.render('arbol_expresion', view=True)

graficar_arbol('3 * (9 - 3 * 4)')

