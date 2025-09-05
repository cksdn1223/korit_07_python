def createDeck():
    deck = {}
    for i in range(8):
        deck[f'❤️{i + 2}'] = i + 2
        deck[f'♦️{i + 2}'] = i + 2
        deck[f'♠️{i + 2}'] = i + 2
        deck[f'🍀{i + 2}'] = i + 2

    deck[f'❤️J'] = 10
    deck[f'❤️Q'] = 10
    deck[f'❤️K'] = 10
    deck[f'♦️J'] = 10
    deck[f'♦️Q'] = 10
    deck[f'♦️K'] = 10
    deck[f'♠️J'] = 10
    deck[f'♠️Q'] = 10
    deck[f'♠️K'] = 10
    deck[f'🍀J'] = 10
    deck[f'🍀Q'] = 10
    deck[f'🍀K'] = 10

    deck[f'❤️A'] = 11
    deck[f'♦️A'] = 11
    deck[f'♠️A'] = 11
    deck[f'🍀A'] = 11
    return deck