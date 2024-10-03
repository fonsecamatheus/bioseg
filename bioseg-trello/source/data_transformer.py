from typing import Any, Dict, List


class DataTransformer:
    def __init__(self, cards: List[Dict[str, Any]], members: List[Dict[str, Any]], 
                 labels: List[Dict[str, Any]], checkitems: List[Dict[str, Any]]) -> None:
        self.cards = cards
        self.members = members
        self.labels = labels
        self.checkitems = checkitems


    '''
    Implementar métodos de transformação
    
    '''


