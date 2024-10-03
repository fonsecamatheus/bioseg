from typing import Any, Dict, List


class DataExtractor:
    def __init__(self, raw_data: Dict[str, Any]) -> None:
        self.raw_data = raw_data

    def extract_cards(self) -> List[Dict[str, Any]]:
        cards_list = []
        try:
            for card in self.raw_data:
                dic = {
                    'id': card.get('id'),
                    'name': card.get('name'),
                    'start': card.get('start'),
                    'due': card.get('due'),
                    'idMembers': card.get('idMembers'),
                    'checkItemStates': card.get('checkItemStates'),
                    'idLabels': card.get('idLabels')
                }
                cards_list.append(dic)
            return cards_list
        except Exception as e:
            print(f'Erro: {e}')
            return []

    def extract_members(self) -> List[Dict[str, Any]]: 
        return self.raw_data

    def extract_labels(self) -> List[Dict[str, Any]]: 
        return self.raw_data
    
    def extract_checklists_ids(self) -> List[Dict[str, Any]]:
        id_checklists_list = []
        try:
            for checklist in self.raw_data:
                id_checklists_list.append(checklist.get('id'))
            return id_checklists_list
        except Exception as e:
            print(f'Erro: {e}')
            return []

    def extract_checkitems(self) -> List[Dict[str, Any]]:
        checkitems_list = []
        try:
            for checkitem in self.raw_data:                
                dic = {
                    'id': checkitem['id'],
                    'name': checkitem['name'],
                    'state': checkitem['state']
                }
                checkitems_list.append(dic)
        except Exception as e:
            print(f'Erro: {e}')
            return []



