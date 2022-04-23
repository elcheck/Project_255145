# Laura Mandele, Jeļena Čekušina
import sqlite3
import requests
import string
def get_quote():
    url="https://api.goprogram.ai/inspiration"
    response = requests.get(url)
    quote=''
    author=''
    if response.status_code==200:
        data_from_json=response.json()
        quote=data_from_json['quote']
        author=data_from_json['author']
    return (quote,author)

class PlayersDB:
    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.cur = self.conn.cursor()
    def drop_table(self):
        self.cur.execute('DROP TABLE players')
    def create_tables(self):
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, score INTEGER)')
    def insert_player(self,username):
        self.cur.execute('INSERT INTO players (username,score ) VALUES (?, ?)', (username, 0))
        self.conn.commit()
    def update_result(self, id, score):
        self.cur.execute('UPDATE players SET score = (?) WHERE id = (?);', (score, id))
        self.conn.commit()
    def delete_player(self, name):
        self.cur.execute('DELETE FROM players WHERE username = (?);', (name,))
        self.conn.commit()
    def find_player(self, by_name=""):
        try:
            list_of_results = self.cur.execute('SELECT id, score FROM players WHERE username = (?);', (by_name,)).fetchall()
            id=list_of_results[-1]
        except:
            id=(0,)
        return id
    def get_rating(self):
        list_of_results = self.cur.execute('SELECT username, score FROM players ORDER by score DESC LIMIT 3;').fetchall()
        print("Are you among our best players?:")
        i=1
        for pl in list_of_results:
            name,score=pl
            print(f"Place: {i}. Name: {name} Score: {score}")
            i+=1
    def close(self):
        self.conn.close()
class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def intro(self):
        print (f"{self.name}! Welcome to the game! Your score is {self.score}")
class GuessAuthor:
    def __init__(self,sentence="Test"):
        self.sentence=sentence
    def play(self):
        result = ""
        the_name=self.sentence.upper()
        for s in the_name:
            if s in string.punctuation or s == " ":
                result+=s
            else:
                result+="*"
        print(result)
        while ("*" in result):
            guess = input("Guess a character or press ENTER if you quit: ").upper()
            if guess=="": return 0
            if len(guess) != 1:
                print("Please enter only one char!")
            else:
                count = the_name.count(guess)  # cik tādu burtu ir vārdā?
                if count > 0:
                    process = ""
                    for c1, c2 in zip(the_name, result):
                        if c1 == guess:
                            process += c1
                        else:
                            process += c2  # create new string by adding char to old string
                    result = process
                else:
                    print(f"Sorry, no '{guess}' in the text")

                print(f"The result is {result}")
        print("Congratulations!!! You win!")
        return 1
if __name__ == '__main__':
    username=input('Enter user name: ')
    if username=='':
        print('See you later!')
        exit()
    session=PlayersDB('chinook.db')
#    session.drop_table()
    session.create_tables()
    player=session.find_player(username)
    id=player[0]
    if id==0:
        session.insert_player(username)
        player = session.find_player(username)
        id=player[0]
    score = player[1]
    player1=Player(username,score)
    player1.intro()
    game=GuessAuthor()
    repeat = 'y'
    while repeat != '':
        quote_and_author=get_quote()
        print ("The inspiration quote for you:")
        print(f"\"{quote_and_author[0]}\"")
        print ("Guess, who is an author of this quote?")
        game.sentence=quote_and_author[1]
        flag=game.play()
        if flag==1:
            score+=1
        repeat=input('Enter any symbol to continue the game or ENTER to exit: ')
    print(f"Your score is {score}")
    session.update_result(id,score)
    session.get_rating()
    session.close()
