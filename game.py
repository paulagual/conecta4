

class Game():
    

    def start(self):
        #imprimo el nombre del juego
        #configuro la partida
        #arranco el game loop
        self.print_logo()

    def print_logo(self):
        logo = """


 ██████  ██████  ███    ██ ███████  ██████ ████████  █████  
██      ██    ██ ████   ██ ██      ██         ██    ██   ██ 
██      ██    ██ ██ ██  ██ █████   ██         ██    ███████ 
██      ██    ██ ██  ██ ██ ██      ██         ██    ██   ██ 
 ██████  ██████  ██   ████ ███████  ██████    ██    ██   ██ 
                                                            
                                                                                          
"""
        print(logo)