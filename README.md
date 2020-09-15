# lichess-path
<a href="https://www.lichess-path.online/">The Lichees-Path Site</a> <br>
The purpose of this project is to find for every user in lichess, his path of victory to magnus carlsen aka DrNykterstein.<br>
What is a path?<br>
a path is a chain of wins from you (the lichess user) to magnus carlsen.<br>
I.E: <br>
me, 'sheynan' (my lichess handle) won 'renkum79', who won 'arashtash1976', who won 'isitajoke', who won 'Zhalmakhanov_R', who won 'DrNykterstein'.<br>

<h1>Building the data base</h1>
<p>I parsed the lichess data base, and added about 550,000 users to my mongoDB.
  each user in the data base is in te form of:<br>
  <pre>
  {
    "_id": {
        "$oid": "5f49168b4269e503095c218c"
    },<br>
    "User_Name": "sheynan",
    "Users_Won": ["Gonzales2015", "parafaragaramus", "Isvelur", "Aurelius23", "renkum79", "Chase_Dickerson", "Demolidor_gyn", "Huthyfy", "RomanOrsag", "Woeke", "Sopiandri", "Paladin51", "stuntmancb", "JHSPaul", "TheColdVolcano", "vladanufr"],
    "Users_Won_Count": 16,
    "Distance": 5
}
</pre>
. and about 30 million games. each player has a 'Distance' property, that indicates how many degrees are from you to Magnus.
The distribution of the 'Distance' property is as followin</p>

