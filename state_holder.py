from enum import Enum

class state(Enum):
    UPLOAD_AGAIN = 1
    LOADING = 2
    MELTING = 3
    BLENDER = 4

class store_states:
    def __init__(self):
        self.state = state.UPLOAD_AGAIN
    
    def update_state(self):
        if self.state == state.UPLOAD_AGAIN:
            self.state = state.LOADING
        elif self.state == state.LOADING:
            self.state = state.MELTING
        elif self.state == state.MELTING:
            self.state = state.BLENDER
        elif self.state == state.BLENDER:
            self.state = state.UPLOAD_AGAIN
