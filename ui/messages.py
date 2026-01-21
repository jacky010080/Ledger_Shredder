"""
Provides simple helpers for colorized output in the CLI.
Used across the program to keep printed messages consistent and easy to read.
"""
RESET = "\033[0m"
# Mapping of color names to ANSI escape codes used for terminal styling.
COLORS = {
    "red": "\033[91m",       
    "green": "\033[92m",     
    "yellow": "\033[93m",    
    "blue": "\033[94m",      
    "info": "\033[96m",     # general informational text  
    "title": "\033[95;1m",  # section titles/headings
}

def format_message(msg, color="info"):
    """
    Return a string formatted with the chosen color.
    """
    code = COLORS.get(color, COLORS["info"])
    return f"{code}{msg}{RESET}"


def print_message(msg, color="info"):
    """
    Print a colorized message
    """
    print(format_message(msg, color))
