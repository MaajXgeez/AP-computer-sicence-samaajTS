# quiz1.py

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.
A linear search checks each element in a list one by one until it finds the target, while a binary search repeatedly divides the sorted list in half to locate the target more efficiently.

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.

listA = [10, 24, 34, 35, 67, 98, 101]
It would take 6 steps to find the number 98 using a linear search, because the algorithm checks each number in order starting from the beginning.

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.

listB = [1, 40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]
It would take 4 steps to find the number 150 using binary search. The list is split in half repeatedly until the number is found.

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.
An algorithm is a set of clear and step-by-step instructions used to solve a problem or perform a specific task.

# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.
 The best Big-O time complexity for this situation would be O(1), or constant time, because they already know exactly which floor and room to go to and do not need to search.

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.
The best Big-O time complexity would be O(n), or linear time, because you might have to check each pair of pants one at a time until you find your phone.

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.

class GameConsole:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def turn_on(self):
        return f"{self.model} is now ON."

    def turn_off(self):
        return f"{self.model} is now OFF."

    def storage_info(self):
        return f"{self.model} has {self.storage} of storage."

# Creating two unique game console objects
console1 = GameConsole("Sony", "PlayStation 5", "1TB", "White")
console2 = GameConsole("Microsoft", "Xbox Series X", "1TB", "Black")

# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.

class VideoGame:
    def __init__(self, title, genre, platform, rating):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.rating = rating

    def start_game(self):
        return f"Starting {self.title} on {self.platform}."

    def stop_game(self):
        return f"Stopping {self.title}."

    def game_info(self):
        return f"{self.title} is a {self.genre} game rated {self.rating}."

# Creating two unique video game objects
game1 = VideoGame("Spider-Man 2", "Action-Adventure", "PlayStation 5", "T")
game2 = VideoGame("Halo Infinite", "Shooter", "Xbox Series X", "M")