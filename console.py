from datetime import datetime

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Console:
    def info(text):
        return Color.BOLD + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Color.BLUE + " INFO     " + Color.END + text
    
    def error(text):
        return Color.BOLD + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Color.RED + " ERROR     " + Color.END + text
    
    def warning(text):
        return Color.BOLD + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Color.YELLOW + " ERROR     " + Color.END + text