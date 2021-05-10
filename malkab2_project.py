import os
import sys
import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='localhost',
                                         database='players',
                                         user='root',
                                         password='Therock12')

def function_1(Query, playerName, info):
    cursor = connection.cursor()
    result = cursor.execute(Query)
    data= cursor.fetchall() 
    print("\n")
    print(playerName + "'s " + info + " is: ",data)
    print("\n")
i = 0
limit = 1
while i != 6:
    
    username = input("1. Display players names\n"
                     "2. Enter a player's name\n"
                     "3. number of results (1 by defult)\n"
                     "4. Exit\nyou choice: ")
    
    
    if username == '1':
        Query = """select short_name from playersdata limit %s"""%(limit)
        function_1(Query, "", "")
    
    elif username == '2':
        nameplayer = input ("player's name (for example: L. Messi): ")
        x = 0
        while x != 6:
            playerOptions = input ("1. display " + nameplayer + "'s sofifaID\n"
                                   "2. display " + nameplayer + "'s URL link\n"
                                   "3. dispaly " + nameplayer + "'s long name\n"
                                   "4. display " + nameplayer + "'s age\n"
                                   "5. display " + nameplayer + "'s DOB\n"
                                   "6. display " + nameplayer + "'s Hight in cm\n"
                                   "7. display " + nameplayer + "'s Weight in kg\n"
                                   "8. display " + nameplayer + "'s nationality\n"
                                   "9. display " + nameplayer + "'s club\n"
                                   "10. display " + nameplayer + "'s rating\n"
                                   "11. display " + nameplayer + "'s value in eur\n"
                                   "12. display " + nameplayer + "'s wage in eur\n"
                                   "13. display " + nameplayer + "'s positions\n"
                                   "14. display " + nameplayer + "'s preferred foot\n"
                                   "15. display " + nameplayer + "'s weak foot rating\n"
                                   "16. display " + nameplayer + "'s jersey number\n"
                                   "17. display " + nameplayer + "'s date of entery\n"
                                   "18. display all info\n"
                                   "19. change the player\n"
                                   "\nChoose your option: ")
                                   
            if playerOptions == '18':    
                Query = """select * from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "all info")             
            elif playerOptions == '1':
                Query = """select sofifa_id from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "sofifaID")                
            elif playerOptions == '2':
                Query = """select player_url from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "URL link")
            elif playerOptions == '3':
                Query = """select long_name from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "long name")                
            elif playerOptions == '4':
                Query = """select age from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "age")
            elif playerOptions == '5':
                Query = """select dob from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "date of birth")
            elif playerOptions == '6':
                Query = """select height_cm from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "Hight in cm")
            elif playerOptions == '7':
                Query = """select weight_kg from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "Weight in kg")
            elif playerOptions == '8':
                Query = """select nationality from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "nationality")
            elif playerOptions == '9':
                Query = """select club from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "club")
            elif playerOptions == '10':
                Query = """select overall from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "rating")
            elif playerOptions == '11':
                Query = """select value_eur from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "value in eur")
            elif playerOptions == '12':
                Query = """select wage_eur from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "wage in eur")
            elif playerOptions == '13':
                Query = """select player_positions from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "positions")
            elif playerOptions == '14':
                Query = """select preferred_foot from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "preferred foot")
            elif playerOptions == '15':
                Query = """select weak_foot from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "weak foot rating")
            elif playerOptions == '16':
                Query = """select team_jersey_number from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "jersey number")
            elif playerOptions == '17':
                Query = """select joined from playersdata where short_name='%s'"""%(nameplayer)
                function_1(Query, nameplayer, "date of entery")
            elif playerOptions == '19':
                break
            else:
                print("\n***please enter option number between 1 and 19***\n")
    elif username == "3":
        limit = input("Enter a limit: ")
        
    elif username == '4':
        i = 6
    
    


