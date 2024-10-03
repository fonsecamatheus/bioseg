import pprint

from source.data_extractor import DataExtractor
from source.http_requester import HttpRequester
from source.trello import TrelloBoards, TrelloChecklists

requester = HttpRequester()
board = TrelloBoards(requester, 'LfvxueJy')

raw_data_cards = board.fetch_cards()
raw_data_checklists = board.fetch_checklists()
raw_data_labels = board.fetch_labels()
raw_data_members = board.fetch_members()

data_cards = DataExtractor(raw_data_cards)
extracted_data_cards = data_cards.extract_cards()

data_labels = DataExtractor(raw_data_labels)
extracted_data_labels = data_labels.extract_labels()

data_members = DataExtractor(raw_data_members)
extracted_data_members = data_members.extract_members()

data_checklists = DataExtractor(raw_data_checklists)
id_checks = data_checklists.extract_checklists_ids()

for id in id_checks:
    checkitems = TrelloChecklists(requester, id)
    raw_data_checkitems = checkitems.fetch_checkitems() 
    data_checkitems = DataExtractor(raw_data_checkitems)
    extracted_data_checkitems = data_checkitems.extract_checkitems()
