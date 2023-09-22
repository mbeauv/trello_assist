from trello import (
    create_trello_board,
    create_trello_list,
    create_trello_card,
    create_card_checklist,
    add_item_to_checklist 
)

class SprintBoardFactory:
    def __init__(self, api_key, api_token):
        self.api_key = api_key
        self.api_token = api_token

    def create_card_acceptance_criteria(self, card_id, card_info):
        checklist_id = create_card_checklist(
            self.api_key,
            self.api_token,
            card_id,
            "Acceptance Criteria")["id"]
        for criterion in card_info["acceptanceCriteria"]:
            add_item_to_checklist(
                self.api_key, 
                self.api_token,
                checklist_id,
                criterion)
            
        return checklist_id
    
    def create_sprint_board(self, board_info):
        return create_trello_board(
            self.api_key,
            self.api_token,
            board_info["sprintId"],
            board_info["sprintDescription"])
        
    def create_sprint_lanes(self, board_id):
        lanes = [ "Backlog", "In Progress", "Review", "Done" ]
        list_ids = {}
        for lane in reversed(lanes):
            list_id = create_trello_list(
                self.api_key,
                self.api_token,
                board_id,
                lane
            )
            list_ids[lane] = list_id
        return list_ids
    
    def create_sprint_stories(self, board_id, backlog_id, board_info):
        card_ids = []
        for card in board_info["userStories"]:
            card_id = create_trello_card(
                self.api_key,
                self.api_token,
                backlog_id,
                card["title"],
                self.create_card_description(card))
            self.create_card_acceptance_criteria(card_id, card)
            card_ids.append(card_id)
        return card_ids

    def create_card_description(self, card_info):
        short_description = card_info["userStory"]
        long_description = card_info["description"]
        return f"**{short_description}**\n\n{long_description}"
    
    def create(self, board_info):
        board_id = self.create_sprint_board(board_info)
        lane_ids = self.create_sprint_lanes(board_id)
        card_ids = self.create_sprint_stories(board_id, lane_ids["Backlog"], board_info)
        return None
