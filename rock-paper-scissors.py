import random

def rock_paper_scissors():
    options_list = ['r','p','s']
    input_answer = input('Please select the option: r-rock, p-paper, s-scissors ')
    win_statement = "Hurray! You Won!"
    lose_statement = "Ouch! You Lost"
    computer_reply = options_list[random.randint(0,2)]
    if input_answer in options_list and input_answer != computer_reply:
        print(computer_reply)
        if input_answer == 'r':
            if computer_reply == 'p':
                print(lose_statement)
            else:
                print(win_statement)
        
        if input_answer == 'p':
            if computer_reply == 'r':
                print(win_statement)
            else:
                print(lose_statement)
            
        if input_answer == 's':
            if computer_reply == 'r':
                print(win_statement)
            else:
                print(lose_statement)
    elif input_answer not in options_list:
        print('Selected option not in options list')
    else:
        print('Its a Draw!')


rock_paper_scissors()