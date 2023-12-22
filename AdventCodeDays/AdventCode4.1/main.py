def main():    
    cards = open("input.txt").read().splitlines()
    c = 1
    for card in cards:
        cards[cards.index(card)] = clean_up_card(card, c)
        c += 1
    card_nums = {"winners" : None, "numbers": None}
    total_points = 0
    for card in cards:
        
        split_list = card.split('|')
        card_nums["winners"] = clean_up_numbers(split_list[0].split(' '))
        card_nums["numbers"] = clean_up_numbers(split_list[1].split(' '))
        total = 0
        for winner in card_nums["winners"]:
            if winner in card_nums["numbers"]:
                total += 1
        if total != 0:
            total_points += (2**(total-1))
            
         
    print(total_points)

def clean_up_card(card, c):
    new_card = card.replace(f"Card {c}: ", "")
    return new_card

def clean_up_numbers(list):
    clean_list = []
    for i in list:
        if i != '':
            clean_list.append(i)
    return clean_list
    

main()