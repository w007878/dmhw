from sgmllib import SGMLParser

steam_store_url = 'https://store.steampowered.com'

class game_page(SGMLParser):

    # Initialize
    def reset(self):
        SGMLParset.reset(self)
        self.title = ''
        self.is_dlc = False
        self.is_bunble = False
        
        self.div_flag = False
        self.h1_flag = False
        self.h2_flag = False
        
    def __init__(self): self.reset()
    
    # Return the information
    def get_name(self): return self.title
    def dlc(self): return self.is_dlc
    def bunble(self): return self.is_bunble
        
    # Find the title of the name
    def start_div(self, attrs):
        check = [v for k, v in attrs and k == 'class']
        if 'apphub_AppName' in check:
            self.div_flag = True
    def end_div(self):
        self.div_flag = False
        
    # If 'DLC' is in the page
    def start_h1(self, attrs):
        self.h1_flag = True
    def end_h1(self):
        self.h1_flag = False    
    
    # If this is a bunble rather than a game
    def start_h2(self, attrs):
        check = [v for k, v in attrs and k == 'class']
        if 'no_margin' in check:
            self.h2_flag = True
    def end_h2(self):
        self.h2_flag = False
    
    # get the information we want
    def handle_data(self, data):
        if self.div_flag:
            self.title = data
            
        if self.h1_flag and data == 'DLC':
            self.is_dlc = True
            
