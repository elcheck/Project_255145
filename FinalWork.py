import sqlite3
class PlayersDB:
    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.cur = self.conn.cursor()
    def drop_table(self):
        self.cur.execute('DROP TABLE players')
    def create_tables(self):
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, score INTEGER, level INTEGER)')
    def insert_player(self,username):
        self.cur.execute('INSERT INTO players (username,score ) VALUES (?, ?, ?)', (username, 0, 0))
        self.conn.commit()
    def update_result(self, id, score):
        self.cur.execute('UPDATE players SET score = (?) WHERE id = (?);', (score, id))
        self.conn.commit()
    def delete_player(self, name):
        self.cur.execute('DELETE FROM players WHERE username = (?);', (name,))
    def find_player(self, by_name=""):
        try:
            list_of_results = self.cur.execute('SELECT id, score FROM players WHERE username = (?);', (by_name,)).fetchall()
            id=list_of_results[-1]
        except:
            id=(0,)
        return id
    def close(self):
        self.conn.close()
class Player:

    pass
class GuessWord:
    pass

if __name__ == '__main__':
    username=input('Enter user name: ')
    session=PlayersDB('chinook.db')
    session.create_tables()
    player=session.find_player(username)
    if player[0]==0:
        session.insert_player(username)
        print(f"Hello {username}! Welcome to the game!")
    else:
        id=player[0]
        score=player[1]
        print (f"Hello {username}!")
        print(f"Nice to see you again! your score is: {score}")
# here should be a code of playing game
    the_name = input("Enter the text: ").upper()
    result = ""
    for word in the_name.split(" "):
        result += "*" * len(word) + " "
    print(result)
    while ("*" in result):
        guess = input("Guess a character: ").upper()

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
    score+=1
    session.update_result(id,score)
    session.close()
#    session.insert_data('test')



