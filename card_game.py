# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:05:06 2021

@author: PZ
"""
from random import choice, shuffle
from ranks import cardDeck
from ranks import card_kind_dict, suits_dict, hearts, spades, diamonds, clubs
from names import names
  
class Player:
    def __init__(self, hand =[], money=100):
        self.name = choice(names)
        self.hand = hand
        self.money = money
        self.score = self.setScore()
        self.chip = 3
        self.bet = 0
        
    def __str__(self): # print(player)
        currentHand = ""    
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + "Score: " + str(self.score)
        
        return finalStatus  
    
    def player_name(self):
        name = input("Enter your name: ")
        if not(name):
            name = self.name.upper()
            print("You are given the random name: ", name)
        else:
            self.name = name
        return name
        
            
    # Funtion to calculate the players score
    def setScore(self):     
        self.score = 0
        
        # Card variables
        card1 = self.hand[0]
        card2 = self.hand[1]
        card3 = self.hand[2]
        
        hand_cards = [card1, card2, card3]
        
        # Check if all three cards in players hand are of the same suit
        if all(item in hearts for item in hand_cards):
            # print("HEARTS")
            self.score += suits_dict[card1] + suits_dict[card2] + suits_dict[card3]
            
        elif all(item in spades for item in hand_cards):
            # print("SPADES")
            self.score += suits_dict[card1] + suits_dict[card2]+ suits_dict[card3]
            
        elif all(item in diamonds for item in hand_cards):
            # print("DIAMONDS")
            self.score += suits_dict[card1] + suits_dict[card2] + suits_dict[card3]
            
        elif all(item in clubs for item in hand_cards):
            # print("CLUBS")
            self.score += suits_dict[card1] + suits_dict[card2] + suits_dict[card3]
                
        # Check if two cards in hand are of the hearts suit
        elif card1 in hearts and card2 in hearts and card3 not in hearts:
            self.score += suits_dict[card1] + suits_dict[card2]
        elif card1 in hearts and card3 in hearts and card2 not in hearts:
            self.score += suits_dict[card1] + suits_dict[card3]
        elif card2 in hearts and card3 in hearts and card1 not in hearts:
            self.score += suits_dict[card2] + suits_dict[card3]   

          # Check if two cards in hand are of the spades suit
        elif card1 in spades and card2 in spades and card3 not in spades:
            self.score += suits_dict[card1] + suits_dict[card2]
        elif card1 in spades and card3 in spades and card2 not in spades:
            self.score += suits_dict[card1] + suits_dict[card3]
        elif card2 in spades and card3 in spades and card1 not in spades:
            self.score += suits_dict[card2] + suits_dict[card3]
            
        #Check if two cards in hand are of the diamonds suit
        elif card1 in diamonds and card2 in diamonds and card3 not in diamonds:
            self.score += suits_dict[card1] + suits_dict[card2]
        elif card1 in diamonds and card3 in diamonds and card2 not in diamonds:
            self.score += suits_dict[card1] + suits_dict[card3]
        elif card2 in diamonds and card3 in diamonds and  card1 not in diamonds:
            self.score += suits_dict[card2] + suits_dict[card3]
            
        #Check if two cards are of the clubs suit
        elif card1 in clubs and card2 in clubs and card3 not in clubs:
            self.score += suits_dict[card1] + suits_dict[card2]
        elif card1 in clubs and card3 in clubs and card2 not in clubs:
            self.score += suits_dict[card1] + suits_dict[card3]
        elif card2 in clubs and card3 in clubs and card1 not in clubs:
            self.score += suits_dict[card2] + suits_dict[card3]
        
        # check if all three cards in hand are of the same kind
        elif all(item in card_kind_dict['aces'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['twos'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['threes'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['fours'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict["fives"] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['six'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['sevens'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['eights'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['nines'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['tens'] for item in hand_cards):
            self.score += 30
        elif all (item in card_kind_dict['jacks'] for item in hand_cards):
            self.score += 30
        elif all(item in card_kind_dict['queens'] for item in hand_cards):
            self.score += 30
        elif all (item in card_kind_dict['kings'] for item in hand_cards):
            self.score += 30
            
        # check If all three cards in hand are of differents suits 
        else:
            # print("Different suits")
            #Variable to store the card with the largest rank
            largest_card = 0
            for card in self.hand:
                if suits_dict[card] > largest_card:
                    largest_card = suits_dict[card]
            # print(largest_card)
            self.score += largest_card           
        
        return self.score
    def tap(self):
        print(self.name, "has tapped", "make last draw")
        accept = input("OK").upper()
        if accept == "OK":
            pass
     
    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()
        
    def discard(self, card):
        self.hand.remove(card)
        self.score = self.setScore()
        
    def play(self, newHand):
        self.hand = newHand
        self.score =self.setScore()   
     
    def last_draw(self):
        self.hit()
        self.play()
        self.compareScores()
    
    def betMoney(self,amount):
        self.money -= amount
        self.bet += amount
        
    def win(self,result):
        if result == True:
            if self.score == 31 and len(self.hand) == 3:
                self.money += 2*self.bet
        else:
            self.bet = 0
            
    def compareScores(self):
        if self.name.self.score > self.name.self.score:
            pass
            
            
    def draw(self):
        self.money += self.bet
        self.bet = 0
    
    def lose_life(self):
        self.chip -= 1
        
    def lose_2_lives(self):
        self.chip -= 2
    
    def thirtyOne(self):
        if self.score == 31 and len(self.hand) == 3:
            return True
        else:
            return False

def printPile(discardPile):
    for card in range(len(discardPile.hand)):
        if card == 0:
            print(card, end =" ")
        elif card == len(discardPile.hand) - 1:
            print(discardPile.hand[card])
        else:
            print(discardPile.hand[card], end = " ")
            
        
class discards(Player):
     def __init__(self, discardPile =[],):
        super().__init__(hand=[], money=100)
        self.discardPile = discardPile
    
     def discard(self, card):
        self.hand.append(card)
        
     def collectCard(self, newHand):
        self.hand = newHand
       
deck = cardDeck()
shuffle(deck)
firstHand = [deck.pop(), deck.pop(), deck.pop()]
secondHand = [deck.pop(), deck.pop(), deck.pop()]
# discardHand = [deck.pop()]
player1 = Player(firstHand)
player2 = Player(secondHand)
# discardPile = discards()
deck = cardDeck()
shuffle(deck)

while(True):
    if len(deck) < 20:
        deck = cardDeck()
    # issue cards
    firstHand = [deck.pop(), deck.pop(), deck.pop()]
    secondHand = [deck.pop(), deck.pop(), deck.pop()]
    # discardHand = [deck.pop()]
    
    player1.play(firstHand)
    player2.play(secondHand)
    # discardPile.play(discardHand)
    
    player1.player_name()
    print(chr(27) + "[2J")
    player_name1 = player1.name.upper()
    print(player_name1)
    bet = int(input("Please place your bet: "))
    print(chr(27) + "[2J")
    
    player2.name    
    player_name2 = player2.name.upper()
    print(player_name2)
    bet = int(input("Please place your bet: "))
    print(chr(27) + "[2J")
    
    # print(deck)
    # Place bets
    player1.betMoney(bet)
    player2.betMoney(bet)
    # printPile(discardPile)
    
    # Check if players were dealt with cards that make thirty one
    if player1.thirtyOne():
        if player2.thirtyOne():
            player1.draw()
            player2.draw()
        else:
            player1.win(True) 
            player2.win(True)
    # Initialize player one    
    print(player_name1 + "'s turn.")
    if player1.score > 25 and player1.score <= 30:
        print(player1)
        action = input("Do you want to tap?(y/n): ").upper()
        if action == "N":
            player1.hit(deck.pop())
            print(player1)
            card = input("Choose a card to discard: ").upper()
            player1.discard(card)
            print(player1)
            # printPile(discardPile)
    else:
         print(player1)
         player1.hit(deck.pop())
         print(player1)
         card = input("Choose a card to discard: ").upper()
         player1.discard(card)
         print(player1)
         print(chr(27) + "[2J")
    
    # inititalize player 2
    print(player_name2 + "'s turn.")
    if player2.score > 25 and player2.score <= 30:
        print(player2)
        action = input("Do you want to tap?(y/n): ").upper()
        if action == "N":
            player2.hit(deck.pop())
            print(player2)
            card = input("Choose a card to discard: ").upper()
            player2.discard(card)
            print(player2)
        # printPile(discardPile)
    else:
        print(player2)
        player2.hit(deck.pop())
        print(player2)
        card = input("Choose a card to discard: ").upper()
        player2.discard(card)
        print(player2)
        print(chr(27) + "[2J")
      
    #Check winner  
    if player1.score > player2.score:
        player1.win(True)
    elif player2.score > player1.score:
        player2.win(True)
    
    elif player1.score == player2.score:
        player1.draw()
        player2.draw()
      
    print(player1.money)   
    print(player2.money)
    # print(discardPile)
        
        
        
    
        
            