class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def is_leaf(self):
        return self.left is None and self.right is None

def assign_hero(mission):
    root = Node("¿La misión es intergaláctica?")
    root.left = Node("¿La misión es de recuperación y no se puede ser detectado?")
    root.right = Node("¿La misión es de destrucción?")
    
    root.left.left = Node("¿Se requiere infiltración con personas del lugar?")
    root.left.right = Node("¿Es Khan el solicitante?")
    
    root.left.right.left = Node("Khan")
    root.left.right.right = Node("Ant-Man")
    
    root.left.left.left = Node("The Winter Soldier")
    root.left.left.right = Node("Capitana Marvel")
    
    root.right.left = Node("¿Se requiere de un líder para planear la misión?")
    root.right.right = Node("¿Es Nick Fury el solicitante?")
    
    root.right.left.left = Node("Iron Man")
    root.right.left.right = Node("Capitán América")
    
    root.right.right.left = Node("Thor")
    root.right.right.right = Node("The Incredible Hulk")
    
    current_node = root
    while not current_node.is_leaf():
        answer = input(current_node.data + " (s/n) ")
        if answer.lower() == 's':
            current_node = current_node.left
        else:
            current_node = current_node.right
    
    return current_node.data

mission = input("Introduce la descripción de la misión: ")
hero = assign_hero(mission)
print(f"El superhéroe asignado para la misión es: {hero}")
