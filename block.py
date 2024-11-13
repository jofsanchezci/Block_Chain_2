import hashlib
import time

# Clase Block para representar un bloque en la cadena
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __str__(self):
        return f"Block #{self.index} [Previous Hash: {self.previous_hash}, Hash: {self.hash}, Timestamp: {self.timestamp}, Data: {self.data}]"


# Clase Blockchain para gestionar la cadena
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Crea el primer bloque de la cadena (bloque génesis)"""
        genesis_block = Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))
        self.chain.append(genesis_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        """Calcula el hash de un bloque dado"""
        block_string = f"{index}{previous_hash}{timestamp}{data}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data):
        """Añade un nuevo bloque a la cadena"""
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        hash = self.calculate_hash(index, previous_block.hash, timestamp, data)
        new_block = Block(index, previous_block.hash, timestamp, data, hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Valida la cadena comprobando que no se hayan alterado los bloques"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Verificar que el hash de cada bloque sea válido
            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                print(f"Hash mismatch at block #{current_block.index}")
                return False

            # Verificar que el hash anterior en el bloque coincida con el hash del bloque anterior
            if current_block.previous_hash != previous_block.hash:
                print(f"Previous hash mismatch at block #{current_block.index}")
                return False

        return True


# Crear una nueva blockchain
blockchain = Blockchain()

# Añadir bloques a la cadena
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")
blockchain.add_block("Transaction 3")

# Imprimir los bloques de la cadena
for block in blockchain.chain:
    print(block)

# Verificar si la cadena es válida
print("\nIs blockchain valid?", blockchain.is_chain_valid())
