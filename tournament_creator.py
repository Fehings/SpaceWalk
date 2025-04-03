# Code to take a list of names and randomise the order of them to create match ups for a knock out tournament. 

import random
import sys

def create_tournament(names):
    '''
    Create a tournament by shuffling the list of names, creating matchups for the first round, and returning the matchups.
    Args:
        names (list): A list of participant names.
    Returns:
        list: A list of tuples representing the matchups for the first round. 
    '''
    # Step 1: Shuffle the list of names
    random.shuffle(names)
    
    # Step 2: Print the randomized list
    print("Randomized Order of Participants:")
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")
    
    # Step 3: Create matchups for the first round
    print("\nFirst Round Matchups:")
    if len(names) % 2 != 0:
        print("Odd number of participants. One participant gets a bye.")
    
    matchups = []
    while len(names) > 1:
        player1 = names.pop(0)
        player2 = names.pop(0) if names else "Bye"
        matchups.append((player1, player2))
        print(f"{player1} vs {player2}")
    
    # Step 4: Return the matchups for further processing if needed
    return matchups

# Example usage
if __name__ == "__main__":

 # Check for command-line arguments
    if len(sys.argv) > 1:
        participants = sys.argv[1:]  # Take all arguments after the script name
    else:
        # Default list of participants
        participants = [
            "Milk Chocolate Digestives",
            "Dark Chocolate Digestives",
            "Milk Chocolate Hobnobs",
            "Dark Chocolate Hobnobs",
            "Chocolate Leibniz",
            "M&S Outrageously Chocolatey Milk Chocolate Rounds",
            "Nutella Biscuits",
            "Chocolate Fingers",
            "Maryland Cookies",
            "Viennese Fingers",
            "Border's Dark Chocolate Gingers",
            "Chocolate Chip Shortbread",
            "Marquisettes",
            "Chocolate Biscoff",
            "Milka Choco Moos",
            "Carol's Lidl Chocolate Surprise"
        ]

    create_tournament(participants)