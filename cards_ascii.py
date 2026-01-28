
import shutil

card_values = {
	"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
	"8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

card_names = list(card_values.keys())
suits = ["spades", "diamonds", "hearts", "clubs"]

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def strength(self):
		return card_values[self.rank]

	def full(self):
		return f"{self.rank} of {self.suit}"
	
	def get_suit(self):
		return self.suit

deck = {}
deck_names = []

for s in suits:
	for r in card_names:
		name = f"{r}_of_{s}"
		deck[name] = Card(r, s)
		deck_names.append(name)

class colors:
	red = '\033[0;31;40m'
	yellow = '\033[0;33;40m'
	dark_blue = '\033[1;34;40m'
	green = '\033[0;32;40m'
	end = '\033[0m'

def return_ascii_card(rank: str, suit: str):

	spades = f"""
.------.
|{rank}.--. |
| :{colors.dark_blue}/\{colors.end}: |
| {colors.dark_blue}(__){colors.end} |
| '--'{rank}|
`------'
"""

	hearts = f"""
.------.
|{rank}.--. |
|{colors.red} (\/) {colors.end}|
| :{colors.red}\/{colors.end}: |
| '--'{rank}|
`------'
"""

	clubs = f"""
.------.
|{rank}.--. |
| :{colors.yellow}(){colors.end}: |
| {colors.yellow}()(){colors.end} |
| '--'{rank}|
`------'
"""

	diamonds = f"""
.------.
|{rank}.--. |
| :{colors.green}/\{colors.end}: |
| :{colors.green}\/{colors.end}: |
| '--'{rank}|
`------'
"""
	cards_dict = {
		"spades": spades,
		"hearts": hearts,
		"diamonds": diamonds,
		"clubs": clubs
	}

	return cards_dict[suit]

cards_ascii = []
cards_name_to_ascii = {}

for c in deck_names:
	cards_ascii.append(return_ascii_card(deck[c].rank, deck[c].suit) if deck[c].rank != "10" else return_ascii_card("T", deck[c].suit))
	
	cards_name_to_ascii[c] = return_ascii_card(deck[c].rank, deck[c].suit) if deck[c].rank != "10" else return_ascii_card("T", deck[c].suit)

def print_cards_side_by_side(cards):
	if not cards:
		return
	
	# Get terminal width
	terminal_width = shutil.get_terminal_size().columns
	
	card_width = 8
	spacing = 2
	cards_per_line = max(1, terminal_width // (card_width + spacing))
	
	# Split cards into rows
	rows = []
	for i in range(0, len(cards), cards_per_line):
		rows.append(cards[i:i + cards_per_line])
	
	# Print row
	for row in rows:
		# Split each card into lines
		split_cards = [card.splitlines() for card in row]
		
		# Zip lines together and print them
		for lines in zip(*split_cards):
			print("  ".join(lines))
		
		if row != rows[-1]:
			print()