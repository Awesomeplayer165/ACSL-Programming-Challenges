# .pop(index) = remove the index element from the list and returns the element
def popPlayerCard():
  return player.pop(0) if len(player) > 0 else -1

def addCardtoPlayer(card):
  player.append(card)

def popPileCard():
  return pile.pop(0) if len(pile) > 0 else -1

def calculateTotal(card):
  if card == 9:
    return total
  elif card == 4:
    return total - 10
  elif card == 0:
    if total + 11 <= 99:
      return total + 11
    else:
      return total + 1
  else:
    return total + card

def play(cards):
  global total, pile, player
  total = cards[0]
  player = cards[1:4]
  pile = cards[4:]
  while True:
    # Player takes the card from his hand
    playercard = popPlayerCard()
    if playercard != -1:
      # Player adds the card to the total
      total = calculateTotal(playercard)
      if total > 99:
        # If player's card makes the total > 99, dealer wins
        return total, "dealer"
    # Player takes a card from the pile
    pilecard = popPileCard()
    if pilecard != -1:
      # Players adds the card to his hand
      addCardtoPlayer(pilecard)
    # Dealer takes the card from the pile
    dealercard = popPileCard()
    if dealercard != -1:
      # Dealer adds card to the total
      total = calculateTotal(dealercard)
      if total > 99:
        # If dealer's card makes the total > 99, player wins
        return total, "player"

print(play([87, 5, 8, 9, 7, 4, 6, 3, 9, 0, 2]))
print(play([78, 2, 4, 8, 3, 8, 5, 0, 6, 9, 8]))
print(play([85, 7, 9, 7, 6, 5, 9, 4, 5, 0, 1]))
print(play([84, 8, 4, 2, 7, 9, 0, 1, 9, 8, 3]))
print(play([95, 9, 0, 9, 0, 1, 0, 1, 0, 2, 5]))