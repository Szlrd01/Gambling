import random
import tools

def blackjack(penz):
    tools.torles()
    penz, tet = tools.tet(penz)
    tools.torles()

    while True:
        player_kartyak = [random.randint(1, 10), random.randint(1, 10)]
        dealer_kartyak = [random.randint(1, 10), random.randint(1, 10)]

        while True:
            player_osszeg = sum(player_kartyak)
            print(f'\nA kártyáid: {player_kartyak} (összeg: {player_osszeg})')

            if player_osszeg > 21:
                print('Túllépted a 21-et! Vesztettél.')
                break

            huz = input('Húzol? (igen/nem): ').lower().strip()
            if huz == 'igen':
                player_kartyak.append(random.randint(1, 10))
            else:
                break

        if sum(player_kartyak) > 21:
            input('Enter...')
            continue

        print(f'\nDealer lapjai: {dealer_kartyak}')
        while sum(dealer_kartyak) < 17:
            dealer_kartyak.append(random.randint(1, 10))

        dealer_osszeg = sum(dealer_kartyak)
        player_osszeg = sum(player_kartyak)

        print(f'Dealer végső lapjai: {dealer_kartyak} (osszeg: {dealer_osszeg})')

        if dealer_osszeg > 21 or player_osszeg > dealer_osszeg:
            print('Nyertél!')
            penz += tet * 20
        elif player_osszeg == dealer_osszeg:
            print('Döntetlen!')
            penz += tet
        else:
            print('Vesztettél!')

        input('Enter...')

    print(f'Kiléptél. Végső egyenleg: {penz}')
    with open('penz.txt', 'w+',encoding='utf-8') as f:
            f.write(str(penz))
    return penz
    