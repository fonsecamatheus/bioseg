import os
from typing import Any, Dict

from dotenv import load_dotenv

from source.http_requester import HttpRequester

load_dotenv()


class Trello:
    def __init__(self, requester: HttpRequester, resource: str) -> None:
        self.requester = requester
        self.url_base = 'https://api.trello.com/1'
        self.params = {
            'key': f'{os.getenv("API_KEY")}',
            'token': f'{os.getenv("API_TOKEN")}'
        }
        self.url = f"{self.url_base}/{resource}"


class TrelloBoards(Trello):
    def __init__(self, requester: HttpRequester, board_id: str) -> None:
        super().__init__(requester, f'boards/{board_id}')

    def fetch_cards(self) -> Dict[str, Any]:
        cards_url = self.url + '/cards'
        return self.requester.get(cards_url, self.params)

    def fetch_members(self) -> Dict[str, Any]:
        members_url = self.url + '/members'
        return self.requester.get(members_url, self.params)

    def fetch_labels(self) -> Dict[str, Any]:
        labels_url = self.url + '/labels'
        return self.requester.get(labels_url, self.params)

    def fetch_checklists(self) -> Dict[str, Any]:
        checklists_url = self.url + '/checklists'
        return self.requester.get(checklists_url, self.params)


class TrelloChecklists(Trello):
    def __init__(self, requester: HttpRequester, checklist_id: str) -> None:
        super().__init__(requester, f'checklists/{checklist_id}')

    def fetch_checkitems(self) -> Dict[str, Any]:
        checkitems_url = self.url + '/checkitems'
        return self.requester.get(checkitems_url, self.params)
