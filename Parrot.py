class Parrot:
    
    species = "Bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
blu = Parrot("Blue", 10)
woo = Parrot("Woo", 15)

print(f"Blu is a {blu.species}")
print(f"Woo is also a {blu.species}")

print(f"{blu.name} is {blu.age} Years Old")
print(f"{woo.name} is {woo.age} Years Old")