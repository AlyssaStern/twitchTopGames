# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('top_games_database.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE OBSERVATIONS
         (Date date PRIMARY KEY);''')

cursor.execute('''CREATE TABLE GAMES
         (GameID text PRIMARY KEY,
         GameName text NOT NULL,
         FirstDate date NOT NULL,
         MostRecentDate date NOT NULL,
         FOREIGN KEY(FirstDate) REFERENCES OBSERVATIONS(Date),
         FOREIGN KEY(MostRecentDate) REFERENCES OBSERVATIONS(Date));''')

cursor.execute('''CREATE TABLE RANKS
         (RankID INTEGER PRIMARY KEY AUTOINCREMENT,
         GameID text NOT NULL,
         Date date NOT NULL,
         Rank INT NOT NULL,
         FOREIGN KEY(GameID) REFERENCES GAMES(GameID),
         FOREIGN KEY (Date) REFERENCES OBSERVATIONS(Date));''')

cursor.close()

conn.commit()
conn.close()