from deck_of_cards import *
from time import sleep

'''deal 2 cards to # of players
Give player their total
Ask player if they want to hit or stay
if hit:
	deal 1 card, check against 21 and give new total if less than 21
	if 21, end player's turn automatically
	if over 21, display 'bust' and state that player loses
else:
	move on to next player, repeat process
dealer logic:
	if less than 16, hit
	if 16 or greater, stay
results:
	player or dealer closest to 21 wins
	if tie, deal 1 card to each player, highest card wins
'''


def cards_value(hand):
	card_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '1':10, 'J':10, 'Q':10, 'K':10}
	card_total = 0
	if type(hand) == list:
		for arg in hand:
			arg = str(arg)
			card_total += card_value[arg[2]]
	else:
		print(hand)
		card_total = card_value[str(hand)[2]]
	return card_total

def hit(hand, deck):
	new_card = deck.deal_card()
	hand.append(new_card)
	return hand

def user_turn(hand, deck, total):
	stay = False
	while stay == False:
		print(f"You are looking at {hand}.")
		print(f"Your current total is {total}.")
		if total > 21:
			print("Sorry! You busted!")
			stay = True
		else:
			answer = input("Would you like to hit or stay? ")
			if answer.lower()[0] == "h":
				hand = hit(hand, deck)
				total = cards_value(hand)
			elif answer.lower()[0] == "s":
				print(f"You stay with {total}.")
				stay = True
			else:
				print("That's not a valid response. Please type hit or stay.")
	return total, hand

def dealer_turn(hand, deck, total):
	stay = False
	while stay == False:
		print(f"Dealer currently has a total of {total}.")
		sleep(2)
		if total < 16:
			hand = hit(hand, deck)
			total = cards_value(hand)
			print("Dealer hits.")
		elif total >= 16 and total <= 21:
			print(f"Dealer stays with a total of {total}.")
			stay = True
		else:
			stay = True
	return total, hand

def result(total_1, total_2, deck):
	while True:
		if total_1 >= 21 and total_2 >= 21:
			print("Both player and house bust! No winners this time.")
			break
		elif total_1 > 21 and total_2 <= 21:
			print("Player busts! House wins!")
			break
		elif total_1 <= 21 and total_2 > 21:
			print("House busts! Player wins!")
			break
		elif total_1 > total_2:
			print("Congratulations player! You win!")
			break
		elif total_2 > total_1:
			print("Too bad! House wins this round!")
			break
		else:
			print("Sudden Death! Each player will draw a card and high card wins.")
			sleep(1)
			total_1 = cards_value(deck.deal_card())
			print(f"Player's card is equal to {total_1}.")
			sleep(1)
			total_2 = cards_value(deck.deal_card())
			print(f"Dealer's card is equal to {total_2}.")

replay = 'y'
while replay == 'y':	
	d = Deck()
	d = d.shuffle()
	player_hand = d.deal_hand(2)
	player_total = cards_value(player_hand)
	dealer_hand = d.deal_hand(2)
	dealer_total = cards_value(dealer_hand)
	print(f"You see the dealer has {dealer_hand[0]} face-up.")
	player_total, player_hand = user_turn(player_hand, d, player_total)
	dealer_total, dealer_hand = dealer_turn(dealer_hand, d, dealer_total)
	result(player_total, dealer_total, d)
	replay = input("Would you like to play again? y/n ").lower()[0]