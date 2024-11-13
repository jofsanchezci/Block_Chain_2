
# Implementación del Árbol de Merkle en Python

Este proyecto presenta una implementación simple de un **Árbol de Merkle** en Python, que se utiliza comúnmente en Blockchain para organizar las transacciones de manera eficiente y verificar su integridad.

## Descripción del Código

### 1. **Clase `MerkleTree`**:
La clase `MerkleTree` representa un Árbol de Merkle. Esta clase tiene los siguientes métodos:
- **`__init__(self, transactions)`**: Inicializa el árbol tomando una lista de transacciones. Llama al método `build_tree` para construir el árbol de Merkle.
- **`build_tree(self, transactions)`**: Construye el árbol de Merkle a partir de las transacciones. Las transacciones se convierten en hashes (hojas), y luego se crean nodos padres al combinar pares de hashes hasta obtener la raíz de Merkle.
- **`create_parent_nodes(self, nodes)`**: Genera los nodos padres tomando los hashes de las transacciones y combinándolos en pares, para luego aplicarles el hash.
- **`hash_transaction(self, transaction)`**: Calcula el hash de una transacción utilizando la función SHA-256.
- **`hash_pair(self, left, right)`**: Combina dos hashes y genera el hash del nodo padre mediante SHA-256.
- **`get_merkle_root(self)`**: Devuelve la raíz de Merkle, que es el hash final del árbol, representando un resumen de todas las transacciones.
- **`display_tree(self)`**: Imprime el árbol de Merkle en la consola, mostrando los nodos de cada nivel.

### 2. **Flujo Principal del Código**:
1. Se definen algunas transacciones simples como una lista de cadenas de texto.
2. Se crea una instancia de `MerkleTree` con estas transacciones.
3. El árbol de Merkle se construye y se imprime.
4. La raíz de Merkle se muestra como el resumen de todas las transacciones.

### 3. **Funcionamiento**:
- El árbol comienza con las transacciones, que se convierten en hashes utilizando SHA-256.
- A medida que se construye el árbol, los nodos padres se generan combinando los hashes de las transacciones. Si hay un número impar de transacciones, se replica el último nodo para formar un par.
- Este proceso continúa hasta que todos los nodos se combinan en la raíz de Merkle, que representa todas las transacciones de forma eficiente.

### 4. **Ejemplo de Uso**:
```python
# Lista de transacciones
transactions = [
    "Tx1: Alice -> Bob",
    "Tx2: Bob -> Charlie",
    "Tx3: Charlie -> Alice",
    "Tx4: Alice -> Charlie"
]

# Crear el árbol de Merkle
merkle_tree = MerkleTree(transactions)

# Mostrar el árbol
merkle_tree.display_tree()

# Obtener la raíz de Merkle
print("
Raíz de Merkle:", merkle_tree.get_merkle_root())
```

### 5. **Salida Esperada**:
El código imprimirá la estructura del árbol de Merkle en niveles, y al final mostrará la raíz de Merkle que representa un resumen de todas las transacciones.

### 6. **Requisitos**:
- Python 3.x
- La librería `hashlib` está incluida en la biblioteca estándar de Python.

## Conclusión:
Este código ilustra cómo funciona un Árbol de Merkle y cómo se utiliza para crear una estructura de datos eficiente y segura para Blockchain. La raíz de Merkle sirve como un resumen de todas las transacciones de un bloque y garantiza que los datos no hayan sido alterados.

