import dbconnect
import comparison

dbconnect = dbconnect.SqlCommunication()

def basic_Conversation():
    user_input = ''

    while True:
        print("나 : ",end='')
        user_input = input()
        print("AI : ",end='')
        response = comparison.response_select(user_input)
        for i in range(len(response)):
            print(response[i][0])

basic_Conversation()
