class DialogueSetting:
    def __init__(self, is_dialogue: bool = True):
        self._is_dialogue = is_dialogue   
    
    def get_is_dialogue(self) -> bool:        
        return self._is_dialogue
    
    def set_is_dialogue(self, value: bool) -> None:       
        if not isinstance(value, bool):
            raise ValueError("is_dialogue must be of type Boolean.")
        self._is_dialogue = value