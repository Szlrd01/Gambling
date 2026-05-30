import random
import tools


def blackjack(penz, normal):
    while True:
        tools.torles()
        penz, tet = tools.tet(penz)
        if tet == 0:
            break
        tools.torles()


        player_kartyak = [
            random.randint(1, 10),
            random.randint(1, 10)
        ]

        dealer_kartyak = [
            random.randint(1, 10),
            random.randint(1, 10)
        ]

        while True:
            tools.torles()
            print('=== BLACKJACK ===')
            player_osszeg = sum(player_kartyak)

            print(
                f'\nA kártyáid: '
                f'{player_kartyak} '
                f'(összeg: {player_osszeg})'
            )

            if player_osszeg > 21:
                print('Túllépted a 21-et! Vesztettél.')
                break

            while True:

                try:
                    huz = input(f'Kérsz még lapot?\n(igen/nem): ').lower().strip()

                except KeyboardInterrupt:
                    print('\nKilépés...')
                    return penz

                except EOFError:
                    print('\nHibás input!')
                    continue

                if huz in ['igen', 'nem']:
                    break

                print('Csak igen vagy nem lehet!')

            if huz == 'igen':
                player_kartyak.append(random.randint(1, 10))
            if huz == 'nem':
                break

        if sum(player_kartyak) > 21:

            try:
                input('Enter...')

            except KeyboardInterrupt:
                print('\nKilépés...')
                return penz

            continue

        print(f'\nDealer lapjai: {dealer_kartyak}')

        while sum(dealer_kartyak) < 17:
            dealer_kartyak.append(random.randint(1, 10))

        dealer_osszeg = sum(dealer_kartyak)
        player_osszeg = sum(player_kartyak)

        print(
            f'Dealer végső lapjai: '
            f'{dealer_kartyak} '
            f'(összeg: {dealer_osszeg})'
        )

        if dealer_osszeg > 21 or player_osszeg > dealer_osszeg:
            print('Nyertél!')
            if normal:
                penz = tools.nyeres2(penz,tet)
            elif not normal:
                penz = tools.nyeres4(penz,tet)

        elif player_osszeg == dealer_osszeg:
            print('Döntetlen!')
            penz += tet

        else:
            print('Vesztettél!')
            penz -= tet
        input('Folytatás...')
    print(f'Kiléptél. Végső egyenleg: {penz}')
    input('Kilépés...')
    try:
        tools.mentes(penz)

    except Exception as e:
        print(f'Hiba mentés közben: {e}')

    return penz