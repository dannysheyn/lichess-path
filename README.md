# lichess-path
<a href="https://www.lichesspath.online/">The Lichees-Path Site</a> <br>
<h4>How to use the site? </h4>
<p>Just enter your lichess handle,(if you dont have one you can use my handle 'sheynan' or, go to the lichess site and find an active user name handle and enter it into the website)<br>
  <img src="https://github.com/dannysheyn/lichess-path/blob/master/Capture.PNG" width="400" height="200"><br>

  and you will get your chain of win to Magnus Carlsen!<br>
  
  <img src="https://github.com/dannysheyn/lichess-path/blob/master/Capture2.PNG" width="400" height="200">  </p>
  
 <p> 
The purpose of this project is to find for every user in lichess, his path of victory to magnus carlsen aka DrNykterstein.<br>
What is a path?<br>
a path is a chain of wins from you (the lichess user) to magnus carlsen.<br>
I.E: <br>
me, 'sheynan' (my lichess handle) won 'renkum79', who won 'arashtash1976', who won 'isitajoke', who won 'Zhalmakhanov_R', who won 'DrNykterstein'.</p>

<h1>Building the data base</h1>
<p>Building the data base was the hardest part of this project. the lichess database file was 114GB and most of that data was going to be parsed, doing so in an    efficient manner is not an easy task. For this task i used the MongoDB using the pymongo module <br>
  I parsed the lichess data base, and added about 550,000 users to my mongoDB. That took about 30 million to parse. <br>
  The the scripts that filled the data-base will be in a folder named : "LichessMongoDB" which you could view the source code over there.
  Each user in the data base is in te form of:<br>
  <pre>
  {
    "_id": {
        "$oid": "5f49168b4269e503095c218c"
    },
    "User_Name": "sheynan",
    "Users_Won": ["Gonzales2015", "parafaragaramus", "Isvelur", "Aurelius23", "renkum79", "Chase_Dickerson", "Demolidor_gyn", "Huthyfy", "RomanOrsag", "Woeke", "Sopiandri", "Paladin51", "stuntmancb", "JHSPaul", "TheColdVolcano", "vladanufr"],
    "Users_Won_Count": 16,
    "Distance": 5
}
</pre>

The 'Distance' property, indicates how many degrees the player is from Magnus Carlsen. (you can see the distribution at the site.
</p>


