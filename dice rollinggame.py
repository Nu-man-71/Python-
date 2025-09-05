import random

def roll_dice(sides=6):
    """Roll a dice with specified number of sides"""
    return random.randint(1, sides)

def roll_multiple(num_dice, sides=6):
    """Roll multiple dice and return results"""
    rolls = [roll_dice(sides) for _ in range(num_dice)]
    return rolls

def main():
    print(" DICE ROLLER ")
    
    while True:
        try:
            num_dice = int(input("Number of dice (1-10): "))
            if num_dice < 1 or num_dice > 10:
                print("Please enter 1-10 dice")
                continue
            
            sides = int(input("Sides per dice (default 6): ") or 6)
            
            rolls = roll_multiple(num_dice, sides)
            
            print(f"\n Results: {rolls}")
            print(f" Total: {sum(rolls)}")
            
            if input("\nRoll again? (y/n): ").lower() != 'y':
                break
                
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()