import random

class Deck():
    '''This class acts as a container for two objects that shuffle and deal the setup.'''
    
    def deck_shuffle():
        '''Function creates a deck of cards and shuffles it.'''
        deck = []
        
        faces = [' A ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ','10 ',' J ',' Q ',' K ']
        for face in faces:
            deck.append([face,'| Spade |'])
            deck.append([face,'| Heart |'])
            deck.append([face,'|Diamond|'])
            deck.append([face,'|Clover |'])
            
        random.shuffle(deck)
        return deck
    
   
    def setup_deal(deck):
        '''Function takes shuffled deck and deals first 2 cards to dealer and player.'''
        dealer = []
        player = []
        hidden_first = []
        cards_used = []
       
    
        for top_two_cards in range(2):
            cards_used.append(deck[0])
            dealer.insert(1,deck[0])
            deck.pop(0)
            cards_used.append(deck[0])
            player.insert(0,deck[0])
            deck.pop(0)
            
        hidden_first.append(player)
            

            
        return dealer,player,cards_used,deck 
    
    
class Card(Deck):
    '''Class contains objects that make up visual representation of cards.'''
    
    def dealer_second(second_card):

        """Takes in a face value being dealt and applies it to a blank card template for print"""
    
        card_distance = '   '
        upper_lower = '-'*9
        side = '|       |'
        face = '_'
        top_card = '|_    |'
        bottom_card = '|    _|'
          
        dealer_top = top_card.replace('_',second_card[0])
        dealer_side = face.replace('_',second_card[1])
        dealer_bottom = bottom_card.replace('_',second_card[0])
    
        return upper_lower,dealer_top,side,dealer_side,dealer_bottom
       
    
    
    def player_hand(first_card,second_card):

        """Takes in a face value being dealt and applies it to 2 blank card templates for print"""
    
        card_distance = '   '
        upper_lower = '-'*9
        side = '|       |'
        face = '_'
        
        plyr_ul_pair = upper_lower + card_distance + upper_lower
        side_pair = side + card_distance + side
        space = card_distance*2
         
        top_card = '|_    |'
        bottom_card = '|    _|'
          
        tf_plyr_card = top_card.replace('_',first_card[0])
        sf_plyr_card = face.replace('_',first_card[1])
        bf_plyr_card = bottom_card.replace('_',first_card[0])

        ts_plyr_card = top_card.replace('_',second_card[0])
        ss_plyr_card = face.replace('_',second_card[1])
        bs_plyr_card = bottom_card.replace('_',second_card[0])
        
        player_top = tf_plyr_card + card_distance + ts_plyr_card 
        player_side = sf_plyr_card + card_distance + ss_plyr_card
        player_bottom = bf_plyr_card + card_distance + bs_plyr_card
        

        return plyr_ul_pair,player_top,side_pair,player_side,player_bottom
    
    
    def hidden_card():
    
        """Takes in a face value being dealt and applies it to a blank 'hidden' card template for print"""
    
        hidden_ul = '-'*9
        fc_side = '|_|/////|'
        side_ = '|///////|' 
        bc_side = '|/////|_|'
        
        return hidden_ul,fc_side, side_,bc_side     
    
    
    
    
class Chip():
    """Class sets up bank object and betting object.""" 
    
    def bank():
        """Establishes a 'bank' with a value of 500."""

        bank = 500
        
        return bank

    def bet(bank):
        """Ask for bet amount from bank."""

        bet = input("How much do you want to bet?: \n   Bank: {}    Bet: ".format(bank))
        
        while len(bet) > 3 or len(bet) == 0:
            bet = input("Please choose a number between 1-500: ")

        while bet[0] not in '123456789':
                bet = input("Please choose a number between 1-500: ")

        if len(bet) > 1:
            while bet[1] not in '123456789':
                bet = input("Please choose a number between 1-500: ")

        if len(bet) > 2:
            while bet[2] not in '123456789':
                bet = input("Please choose a number between 1-500: ")

        bet_amount = int(bet)

        while bet_amount < 0 or bet_amount > 500:
            bet_amount = int(input("Please choose a number between 1-500: "))

        if bet_amount > 0 or bet_amount < 500:
                bank -= bet_amount
                print("Withdrawing from Bank..\n")
                print("remaining Bank: {}\n".format(bank))
        
        return bet_amount,bank 
    
    
class Hand():
    """Class objects handle flow of game as well as ace evaluator and score keeping."""
    
    def pocket():
        """Establishes a visual 'pocket' to add cards as they're dealt."""

        pocket_title = '|      Pocket:     |'
        floor = '--------'
    
        dealer_title = ' | Dealer |'
        player_title = '| Player | '
    
        pocket_spot = "|                  |"
    
        dealer_pocket = [pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot]
        player_pocket = [pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot]
    
        return pocket_title,floor,dealer_title,player_title,dealer_pocket,player_pocket,pocket_spot



    def pocket_adjuster(dealer_pocket,player_pocket,dealer,player):
        """Shifts a 3rd card to the pocket for both dealer and player.""" 

        player_pocket.pop(5) 
        string = str(player[2])
        player_pocket.insert(0,string)
        dealer_pocket.pop(5)
        string_two = str(dealer[2])
        dealer_pocket.insert(0,string_two)
        
        return dealer_pocket,player_pocket
        
    
    
    def hit_stay():
        """Asks if you want to hit or stay and returns response."""
    
        answer = input(" Do you want to Hit['h'] or Stay['s']? \n") 
        while not answer.lower().startswith('h') and  not answer.lower().startswith('s'):
            answer = input("Whoops try again..\n Hit['h'] or Stay['s']? ") 

        if answer.lower() in 'hit':
            print("\n")
            print("   Hit! \ndealing card..  \n")
            print("\n")
            print("Dealer Hits!  \ndealing card..  \n")
            answer = 'h'
            return answer
        
        elif answer.lower() in 'stay':
            print('\n')
            print("   Stay! \n")
            print("Dealer is staying..\n")
            answer = 's'
            return answer
    
    
    def draw_or_wincheck(deck,dealer,player,cards_used):
        """Draws from remaining deck if 'Hit' to both player and dealer."""
        
        cards_used.append(deck[0])
        player.insert(0,deck[0])
        deck.pop(0)
        cards_used.append(deck[0])
        dealer.insert(0,deck[0])
        deck.pop(0)
        
        return deck,dealer,player,cards_used 
    
    
    
    def face_isolator(dealer,player):
        """Isolates the faces from names in both dealer and player lists to use in a card_value function."""
    
        dealer_value = []
        player_value = []
    
        for card in dealer:
            dealer_value.append(card[0])
        
        for card in player:   
            player_value.append(card[0])
        
        return dealer_value,player_value
    


    def ace_eval_and_summarizer(d_value,p_value):
        """Evaluates the value of cards in current hand and keeps score."""
    
        values = [[' A ',[1,11]],[' 2 ',2],[' 3 ',3],[' 4 ',4],[' 5 ',5],[' 6 ',6],[' 7 ',7],[' 8 ',8],[' 9 ',9],['10 ',10],[' J ',10],[' Q ',10],[' K ',10]]
        d_sum = []
        p_sum = []

        for value in values:
            count = 0
            if value[0] in d_value[0] and value[0] == ' A ':
                amount = d_value.count(value[0])
                ace = 0 
                if sum(d_sum) > 10:
                    ace += 1
                    while count < amount:
                        d_sum.append(ace)
                        count+=1
                elif sum(d_sum) <= 10:
                    ace += 11
                    while count < amount:
                        d_sum.append(ace)
                        count+=1
                
            elif value[0] in d_value and value[0] != ' A ':
                amount = d_value.count(value[0])
                while count < amount:
                        d_sum.append(value[1])
                        count+=1
            
        for value in values:
            count = 0

            if value[0] in p_value and value[0] != ' A ':
                amount = p_value.count(value[0])
                while count < amount:
                    p_sum.append(value[1]) 
                    count+=1

            elif value[0] in p_value and value[0] == ' A ':
                amount = p_value.count(value[0])
                while count < amount:
                    one_eleven = input("Player you have an Ace, how much is its worth?\n             1 or 11: ")
        
                    while len(one_eleven) > 2 or len(one_eleven) == 0:
                        one_eleven = input("Please choose a value, 1 or 11: ")

                    if len(one_eleven) > 1:
                        while one_eleven[1] in ' abcdefghijklmnopqrstuvwxyz':
                            one_eleven = input("Please choose a value, 1 or 11: ")   

                    while one_eleven[0] in ' abcdefghijklmnopqrstuvwxyz':
                        one_eleven = input("Please choose a value, 1 or 11: ")

                    one_eleven_amount = int(one_eleven)

                    while one_eleven_amount != 1 and one_eleven_amount != 11:
                        one_eleven_amount = int(input("Please choose a value, 1 or 11: "))

                    if one_eleven_amount == 1:
                        p_sum.append(one_eleven_amount) 
                        count+=1
                    elif one_eleven_amount ==11:
                        p_sum.append(one_eleven_amount)
                        count+=1
            
        return sum(d_sum),sum(p_sum)
    
    
    
    
class Game():
    """Class holds all general game objects."""

        
    def main_screen(dealer,pocket_title,floor,hidden_card,dealer_second,player_set,dealer_title,player_title,bet,bank,dealer_pocket,player_pocket,pocket_spot):
        """Sets up and displays main screen to game."""

        space = '    '
        card_width = '|         |'
        set_space = '                        '
        large_space = '             '
        dbl_card_wdth = card_width + distance + card_width
        dbl_space = space + space
        bet_title = 'Bet:  00{}'.format(bet)
        bank_title = 'Bank: {}'.format(bank)

        
        if bet in range(10,100):
            bet_title = 'Bet:  0{}'.format(bet)
        
        elif bet in range(100,501):
            bet_title = 'Bet:  {}'.format(bet)
        
        if bank in range(10,100):
            bank_title = 'Bank: 0{}'.format(bank)
            
        elif bank < 10:
            bank_title = 'Bank: 00{}'.format(bank)
            
        
        
        print(pocket_title + dbl_space + dealer_title + set_space + player_title + dbl_space + pocket_title)
        print(pocket_spot + space + hidden_ul + distance + upper_lower + large_space + plyr_ul_pair + space + pocket_spot)
        print(dealer_pocket[0] + space + fc_side + distance + dealer_top + large_space + player_top + space + player_pocket[0])
        print(dealer_pocket[1] + space + side_ + distance + side + large_space + side_pair + space + player_pocket[1])
        print(dealer_pocket[2] + space + side_ + distance + dealer_side + distance + bet_title + distance + player_side + space + player_pocket[2])
        print(dealer_pocket[3] + space + side_ + distance + side + large_space + side_pair + space + player_pocket[3])
        print(dealer_pocket[4] + space + side_ + distance + side + distance + bank_title + distance + side_pair + space + player_pocket[4])
        print(dealer_pocket[5] + space + bc_side + distance + dealer_bottom + large_space + player_bottom + space + player_pocket[5])
        print(pocket_spot + space + hidden_ul + distance + upper_lower + large_space + plyr_ul_pair + space + pocket_spot)
        
        return dealer_second,player_set,bet,bank,dealer_pocket,player_pocket
    
    
    
    def want_to_play():
        """Asks if you want to play or not."""

        want_to_play = input(" Do you want to play?\n Yes['y'] or No['n'] ") 
        while want_to_play not in 'yes' and want_to_play not in 'no':
            want_to_play = input("Whoops try again..\n Yes['y'] or No['n'] ") 

        while len(want_to_play) == 0:
            want_to_play = input("Whoops try again..\n Yes['y'] or No['n'] ") 

        if want_to_play.lower() in 'yes':
            print("  Let's get started!")
            want_to_play = True
            return want_to_play
        
        elif want_to_play.lower() in 'no':
            want_to_play = False
            return want_to_play

        
    def start_up():
        """Asks to push Enter between screen sets."""

        continu = input("press ENTER to continue..")
        continu = True
            
    def start_message():
        """Welcome display for opener."""

        edge = '   ---------------'
        intro = "  |    Welcome    |\n  |      to       |\n  |   BlackJack   |"
        print(edge)
        print(intro)
        print(edge)   
        
    def game_reset(bet,dealer,player,cards_used,dealer_pocket,player_pocket):
        """If game is to be replayed, refreshes all sets back to normal."""

        dealer.clear()
        player.clear()
        cards_used.clear()
        deck.clear() 
        dealer_pocket = [pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot]
        player_pocket = [pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot,pocket_spot]
        bet -= bet
        return dealer,player,cards_used,deck,dealer_pocket,player_pocket,bet
        
    def replay():
        """Asks if want to replay."""

        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
        

deck = Deck.deck_shuffle()  
dealer,player,cards_used,deck = Deck.setup_deal(deck)
distance = '  '


hidden_ul,fc_side,side_,bc_side = Card.hidden_card()   
upper_lower,dealer_top,side,dealer_side,dealer_bottom = Card.dealer_second(dealer[1])
plyr_ul_pair,player_top,side_pair,player_side,player_bottom = Card.player_hand(player[1],player[0])

hidden_card = [hidden_ul,fc_side,side_,bc_side]       
dealer_second = [upper_lower,dealer_top,side,dealer_side,dealer_bottom]
player_set = [plyr_ul_pair,player_top,side_pair,player_side]

pocket_title,floor,dealer_title,player_title,dealer_pocket,player_pocket,pocket_spot = Hand.pocket()


print("\n")
Game.start_message()
print("\n")
yes_no = Game.want_to_play()
if yes_no == True:
    print('\n')
    print("Dealer is shuffling cards.")
    print('\n')
    print("Dealer is dealing cards.")
    print('\n')
    bank = Chip.bank()
    bet, bank = Chip.bet(bank)
    print('\n')

    while True:
    
        if bet == 0:
            deck = Deck.deck_shuffle()  
            dealer,player,cards_used,deck = Deck.setup_deal(deck)
            print("Dealer is shuffling cards.")
            print('\n')
            print("Dealer is dealing cards.")
            print('\n')
            bet, bank = Chip.bet(bank)
            print('\n')
            

    
        print("\n")

        upper_lower,dealer_top,side,dealer_side,dealer_bottom = Card.dealer_second(dealer[1])
        plyr_ul_pair,player_top,side_pair,player_side,player_bottom = Card.player_hand(player[0],player[1])
        dealer_second,player_set,bet,bank,dealer_pocket,player_pocket = Game.main_screen(dealer,pocket_title,floor,hidden_card,dealer_second,player_set,dealer_title,player_title,bet,bank,dealer_pocket,player_pocket,pocket_spot)
        d_value,p_value = Hand.face_isolator(dealer,player)
        dsum,psum = Hand.ace_eval_and_summarizer(d_value,p_value)


        print('\n')
    
        if dsum == 21 or psum == 21:
            print("\n")
            print("\n")
        
            if dsum == 21:
                print("Dealer Won!! {}".format(dsum))
                print(dealer)
                print("\n")
                print("You lost with..{}".format(psum))
                print(player)
                print("\n")
                if not Game.replay():
                    print(" Thank You for playing!!")
                    break
                else:
                    dealer,player,cards_used,deck,dealer_pocket,player_pocket,bet = Game.game_reset(bet,dealer,player,cards_used,dealer_pocket,player_pocket)                  
                    deck = Deck.deck_shuffle() 
                    dealer,player,cards_used,deck = Deck.setup_deal(deck) 
                    clear = '\n' * 50
                    print(clear) 
                    continue
                
                
                  
            elif psum == 21: 
                print("You Won!! {}".format(psum))       
                print(player)
                print("\n")
                print("Dealer lost with..{}".format(dsum))
                print(dealer)
                print("\n")
                if not Game.replay():
                    print(" Thank You for playing!!")
                    break
                else:
                    dealer,player,cards_used,deck,dealer_pocket,player_pocket,bet = Game.game_reset(bet,dealer,player,cards_used,dealer_pocket,player_pocket)                  
                    deck = Deck.deck_shuffle()  
                    dealer,player,cards_used,deck = Deck.setup_deal(deck)
                    clear = '\n' * 50
                    print(clear) 
                    continue
            
    
        elif dsum > 21 or psum > 21:
            print("\n")
            print("\n")
        
            if psum > 21:
                print("Bust!! {}".format(psum))
                print(player)
                print("\n")
                print("Dealer finished with..{}".format(dsum))
                print(dealer)
                print("\n")
                if not Game.replay():
                    print(" Thank You for playing!!")
                    break
                else:
                    dealer,player,cards_used,deck,dealer_pocket,player_pocket,bet = Game.game_reset(bet,dealer,player,cards_used,dealer_pocket,player_pocket)                  
                    deck = Deck.deck_shuffle()  
                    dealer,player,cards_used,deck = Deck.setup_deal(deck)
                    clear = '\n' * 50
                    print(clear) 
                    continue
        
            elif dsum > 21:
                print("Dealer Bust!! {}".format(dsum))
                print(dealer)
                print("\n")
                print("You won with {}".format(psum))
                print(player)
                print("\n")
                if not Game.replay():
                    print(" Thank You for playing!!")
                    break
                else:
                    dealer,player,cards_used,deck,dealer_pocket,player_pocket,bet = Game.game_reset(bet,dealer,player,cards_used,dealer_pocket,player_pocket)                  
                    deck = Deck.deck_shuffle()  
                    dealer,player,cards_used,deck = Deck.setup_deal(deck)
                    clear = '\n' * 50
                    print(clear) 
                    continue

    
        hit_or_stay = Hand.hit_stay()
    
        if hit_or_stay in 's':
    
            if dsum > psum:
                print("Dealer has won with {}".format(dsum))
                print(dealer)
                print("\n")
                print("You lost with..{}".format(psum))
                print(player)
                print("\n")
                print("Better Luck Next Time!")
                print("\n")
                if not Game.replay():
                    print(" Thank You for playing!!")
                    break
                else:
                    dealer,player,cards_used,deck,dealer_pocket,player_pocket,bet = Game.game_reset(bet,dealer,player,cards_used,dealer_pocket,player_pocket)                  
                    deck = Deck.deck_shuffle()  
                    dealer,player,cards_used,deck = Deck.setup_deal(deck)
                    clear = '\n' * 50
                    print(clear) 
                    continue
            
            
        
            elif psum > dsum:
                print("Congratulations!\nYou won with {}".format(psum))
                print(player)
                print("\n")
                print("Dealer finished with..{}".format(dsum))
                print(dealer)
                print("\n")
                if not Game.replay():
                    print(" Thank You for playing!!")
                    break
                else:
                    dealer,player,cards_used,deck,dealer_pocket,player_pocket,bet = Game.game_reset(bet,dealer,player,cards_used,dealer_pocket,player_pocket)                  
                    deck = Deck.deck_shuffle()  
                    dealer,player,cards_used,deck = Deck.setup_deal(deck)
                    clear = '\n' * 50
                    print(clear) 
        else:
            deck,dealer,player,cards_used = Hand.draw_or_wincheck(deck,dealer,player,cards_used)
            dealer_pocket,player_pocket = Hand.pocket_adjuster(dealer_pocket,player_pocket,dealer,player)
            Game.start_up()
            
else:
    print(" Okay, maybe next time..")


"""Still in need of function to count Aces that have been given value and function to update bank up until 999 or 000."""