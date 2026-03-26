"""
──── Basic formatting (0-7) ────────────────────────────────────────────────────────────────── 
─ Used to change the style of the text in the terminal. 
─ Each style is represented by a specific escape code. 
─ I decided to add all of them but in the end i only used RESET, which is the most common one.
─ ANSI escape codes for text styling: \033 signals the terminal to read what follows as a
formatting instruction, [ opens it, the number sets the style, and m closes/applies it
"""
RESET   = "\033[0m" 
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
UNDER   = "\033[4m"
BLINK   = "\033[5m"
INVERT  = "\033[7m"

""" 
──── Text colors (30-37) ─────────────────────────────────────────────────────────────────────────────────────
─ Used to change the color of the text in the terminal. 
─ Each color is represented by a specific escape code. 
─ I decided to add all of them even if I only use a few, so I have them ready for future use (THIS IS NOT AI).
─ ANSI escape codes for text color: same structure as above, 3X where X is the color number (0-7)
"""

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# Reusable input function — asks for a value, converts it to the given type (default: str),
# and keeps asking until the user enters something valid
def get_info(prompt, type=str):
    im_not_true = None
    while im_not_true != "stop":                                                        # Infinite loop to keep asking until valid input is received.
        try:
            return type(input(prompt))
            
        except ValueError:
            print(f"{RED}❌ Invalid input. Try again. ❌{RESET}\n")

# Control variable — the loop runs until the user finishes registering a product
check = None

# Main loop — collects product data, calculates total cost, and displays the result. I know its use here is a bit redundant since we only register one product, but i will recycle this code so i have it ready for future use lol
while check != "stop":

    # Ask for the product name (string, no conversion needed)
    name = get_info(f"{YELLOW}🏷️  Enter the name of the product:\n➤{RESET}  ")

    # Ask for the price and convert to float
    price = get_info(f"{GREEN}💵 Enter the price of the product:\n➤{RESET}  ", float)

    # Ask for the quantity and convert to int
    quantity = get_info(f"{BLUE}🔢 Enter the quantity of the product:\n➤{RESET}  ", int)

    # Calculate total cost
    total_cost = price * quantity

    # Display the product summary with colors
    print(f"{YELLOW}Product: {name} {RESET}|{GREEN} Price: ${price} {RESET}|{BLUE} Quantity: {quantity} {RESET}|{MAGENTA} Total Cost: ${total_cost}{RESET}\n")

    # Set check to "stop" to exit the loop after one product is registered
    check = "stop"
"""
──── Summary ────────────────────────────────────────────────────────────────────────────────
This program registers a single product by asking the user for its name, price, and quantity.
It validates numeric inputs using a reusable function and displays a formatted summary with
ANSI color codes to make the terminal output easier to read.
"""
