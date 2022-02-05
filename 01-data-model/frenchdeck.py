import collections
from random import choice

Card=collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades diamonds clubs hearts'.split()
    print(ranks)
    #['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    print(type(ranks)) #<class 'list'>

    print(suits)
    # ['spades', 'diamonds', 'clubs', 'hearts']
    print(type(suits)) #<class 'list'>

    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits
                                     for rank in self.ranks]
        
        # print('_cards:',self._cards)
        # print(type(self._cards))     #<class 'list'>
        # print(type(self._cards[0]))  #<class '__main__.Card'>

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]

deck=FrenchDeck()
# print(deck.__len__())
# print(deck[0])
# print(deck[-1])
# print(len(deck))
# print(deck)
# print(deck.__getitem__(10))
# print(type(deck))

# print(choice(deck))

# print(deck[:3])
# print(deck[12: :13])

# for card in deck:
#     print(card)

# for card in reversed(deck):
#     print(card)

#???????????  这里没有看懂,FrenchDeck.ranks.index(card.rank)是什么??????????///
# suit_values=dict(spades=3,hearts=2,diamonds=1,clubs=0)
# print(suit_values)
# def spades_high(card):
#     rank_value=FrenchDeck.ranks.index(card.rank)
#     return rank_value*len(suit_values)+suit_values[card.suit]
# print('\n---------------我是分割线--------------------')
# for card in sorted(deck,key=spades_high):
#     print(card)
