
RESET   = "\033[0m" 
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
UNDER   = "\033[4m"
BLINK   = "\033[5m"
INVERT  = "\033[7m"

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

def get_info(prompt, type=str):
    while 777:
        try:
            return type(input(prompt))
            
        except ValueError:
            print(f"{RED}❌​ Invalid input. Try again. ​​❌​{RESET}\n")

check = None
while check != "stop":
    name = get_info(f"{YELLOW}🏷️​  Enter the name of the product:\n➤{RESET}  ")
    price = get_info(f"{GREEN}💵​ Enter the price of the product:\n➤{RESET}  ", float)
    quantity = get_info(f"{BLUE}🔢​ Enter the quantity of the product:\n➤{RESET}  ", int)
    total_cost = price * quantity

    check = "stop"