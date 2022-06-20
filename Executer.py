name = input('Hello! I am waiter_bot. What is your name? ')
eat = input('Would you like to eat today,'+name + ' ' )
if (eat.lower() == 'of course')  or (eat.lower() == 'yes') or (eat.lower() == 'maybe') :
    print('Perfect! Heres a menu.')
    print('1) Fries\n2) Burger\n3) Wagyu Striploin with Potato Puree\n4) Caesar Salad\n5) Smoked Duck with Red wine reduction\n6) Lava Cake with Taitan Vanilla bean ice cream')
    choose = int(input('Choose the number of the dish you would like to order!!'))
    if choose == 1: 
        amount = input('How many servings would you like?')
        print('Here are your '+ amount +' Fries! They are fresh from the frier so they are quite hot.')
    elif choose == 2:
        amount = input('How many servings would you like?')
        print('Here are your '+ amount +' Kobe Beef burgers, cooked Medium to your request, served with fries fried in beef fat')
    elif choose == 3:
        amount = input('How many servings would you like?')
        print('Here is your '+ amount +' Wagyu Striploins, cooked to perfect medium rare, with a smooth potato puree and roasted carrots')
    elif choose == 4:
        amount = input('How many servings would you like?')
        print('Here are your '+ amount +' Caesar Salads with dressing. Enjoy!')
    elif choose == 5:
        amount = input('How many servings would you like?')
        print('Here is your '+ amount +' Smoked Duck, cooked rare, with a very esquisite red wine reduction. Enjoy your meal!')
    elif choose == 6:
        amount = input('How many servings would you like?')
        print('Here is your '+ amount +' desserts, which are lava cake and some very special vanilla bean ice cream. Enjoy!')
if (eat.lower() == 'no') or (eat.lower() == 'no thanks') or (eat.lower() == 'im good'):
    drinks = input('Would you like a drink?')
if (drinks.lower() == 'yes') or (drinks.lower() == 'yes please') or (drinks.lower() == 'sure'):
    print('Here are our options')
    print('1) Water\n2) Lemonade\n3) Red Wine\n4) Champagne')
    choice = int(input('Choose the drink that you would like to order using the number'))
    if choice == 1:
        print('Enjoy the water!')
    elif choice == 2:
        print('Enjoy the Lemonade!')
    elif choice == 3:
        print('Enjoy the Wine!')
    elif choice == 4:
        print('Enjoy the champagne!')
