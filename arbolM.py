import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.tree = self.build_tree(transactions)
        
    def build_tree(self, transactions):
        """Construye el árbol de Merkle a partir de las transacciones"""
        tree = []
        # Crear las hojas del árbol (hash de las transacciones)
        leaf_nodes = [self.hash_transaction(tx) for tx in transactions]
        tree.append(leaf_nodes)

        # Construir el árbol de Merkle de abajo hacia arriba
        while len(leaf_nodes) > 1:
            leaf_nodes = self.create_parent_nodes(leaf_nodes)
            tree.append(leaf_nodes)
        
        return tree

    def create_parent_nodes(self, nodes):
        """Crea los nodos padres combinando los hashes de los nodos hijos"""
        parent_nodes = []
        for i in range(0, len(nodes), 2):
            # Si hay un número impar de nodos, duplicamos el último nodo
            if i + 1 < len(nodes):
                parent_nodes.append(self.hash_pair(nodes[i], nodes[i + 1]))
            else:
                parent_nodes.append(nodes[i])
        return parent_nodes

    def hash_transaction(self, transaction):
        """Devuelve el hash de una transacción"""
        return hashlib.sha256(transaction.encode('utf-8')).hexdigest()

    def hash_pair(self, left, right):
        """Devuelve el hash combinado de dos nodos"""
        return hashlib.sha256((left + right).encode('utf-8')).hexdigest()

    def get_merkle_root(self):
        """Devuelve la raíz de Merkle"""
        return self.tree[-1][0]

    def display_tree(self):
        """Imprime la estructura del árbol de Merkle"""
        for level in self.tree:
            print(level)

# Ejemplo de uso
transactions = [
    "Tx1: Alice -> Bob",
    "Tx2: Bob -> Charlie",
    "Tx3: Charlie -> Alice",
    "Tx4: Alice -> Charlie"
]

# Crear el árbol de Merkle
merkle_tree = MerkleTree(transactions)

# Mostrar el árbol
print("Árbol de Merkle:")
merkle_tree.display_tree()

# Mostrar la raíz de Merkle
print("\nRaíz de Merkle:", merkle_tree.get_merkle_root())
