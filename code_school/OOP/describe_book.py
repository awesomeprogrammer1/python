'''
Create a class that describes the book.
It should contain information about
the author, title, year and genre. 
Create several different books.
'''


class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre


book_one = Book("J.K. Rowling", "Harry Potter", 1997, "Action")


class HockeyPlayer:
    def __init__(self, name, team, yob, stanley_cups_won):
        self.name = name
        self.team = team
        self.yob = yob
        self.stanley_cups_won = stanley_cups_won
    
    def won_stanley_cup(self):
        self.stanley_cups_won += 1
        return f"Congratulations to {self.name} for winning the stanley cup!"
    
    def change_team(self, new_team):
        self.team = new_team
        return f"{self.name} has been traded to the {self.team}"
    

hockey_player_one = HockeyPlayer("Matthew Barzal", "New York Islanders", 1997, 0)
hockey_player_two = HockeyPlayer("Connor McDavid", "Edmonton Oilers", 1997, 0)
print(hockey_player_one.stanley_cups_won)
print(hockey_player_one.won_stanley_cup())
print(hockey_player_one.stanley_cups_won)
#
print(hockey_player_two.team)
print(hockey_player_two.change_team("Vegas Golden Knights"))
print(hockey_player_two.team)
