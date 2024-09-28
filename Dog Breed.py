

class Dog:
    
    animal_class = "Dog"
    
    
    def __init__(self, breed, color, favourite_toy, barking_level, training_status):
        
        self.breed = breed
        self.color = color
        self.favourite_toy = favourite_toy
        self.barking_level = barking_level
        self.training_status = training_status
    
    
    def display_details(self):
        print(f"Animal: {Dog.animal_class}")  
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
        print(f"Favorite Toy: {self.favourite_toy}")  
        print(f"Barking Level: {self.barking_level}/10")
        if self.training_status == True:
           print("Trained: Yes")
        else:
          print("Trained: No")

        
dog1 = Dog("Golden Retriever", "Golden", "Ball", 6, False)
dog2 = Dog("German Shepherd", "Black and Brown", "Frisbee", 9.5, True)


print("Details of Dog 1:")
dog1.display_details()

print("\nDetails of Dog 2:")
dog2.display_details()

# Thanks for Viewing My Project!


    
  
