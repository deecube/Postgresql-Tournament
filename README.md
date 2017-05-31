# Tournament Planner
## A Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project requires Python 2.7 and the following Python libraries installed:

* [Psycopg2](http://initd.org/psycopg/)

#### Description of the project files:

* `tournament.sql` - this file is used to set up the database schema.
* `tournament.py` - this file is used to provide access to your database via a library of functions which can add, delete or query data in the database to another python program (a client program). 
* `tournament_test.py` - this is a client program which will use your functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py.

#### Installation Instructions
Please ensure that you have postgresql, psql, psycopg2 and python are installed.

Using the `tournament.sql` file

* The tournament.sql file should be used for setting up the schema and database prior to a client making use of the database for reporting and managing tournament players and matches. This file will only be run once by a client setting up a new tournament database. 
It will execute when you run
```
vagrant@vagrant:/Postgresql-Tournament$ psql
psql (9.5.6)
Type "help" for help.

user_name=> psql \i tournament.sql
DROP DATABASE
CREATE DATABASE
You are now connected to database "tournament" as user "user_name".
CREATE TABLE
CREATE TABLE
tournament-> 

```

#### Run
Once the database is set up, the test program can be run by using the following command:
`python tournament_test.py`

You should be able to see the following output once all the tests have passed:

```
vagrant@vagrant:/Postgresql-Tournament$ python tournament_test.py 
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
5 6 7 8
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```
#### Example of a 16 Player Swiss Tournament:

First round pairing is by random draw. For example, with 16 players they would be matched into 8 random pairs for the first round. For now, assume all games have a winner, and there are no draws.
After the first round, there will be a group of 8 players with a score of 1 (win), and a group of 8 players with a score of 0 (loss). For the 2nd round, players in each scoring group will be paired against each other – 1’s versus 1’s and 0’s versus 0’s.

After round 2, there will be three scoring groups:

4 players who have won both games and have 2 points

8 players who have won a game and lost a game and have 1 point

4 players who have lost both games and have no points.

Again, for round 3, players are paired with players in their scoring group. After the third round, the typical scoring groups will be:

2 players who have won 3 games (3 points)
6 players with 2 wins (2 points)
6 players with 1 win (1 point)
2 players with no wins (0 points)

For the fourth (and in this case final) round, the process repeats, and players are matched with others in their scoring group. Note that there are only 2 players who have won all of their games so far – they will be matched against each other for the "championship" game. After the final round, we’ll have something that looks like this:

1 player with 4 points – the winner!
4 players with 3 points – tied for second place
6 players with 2 points
4 players with 1 point
1 player with 0 points

The Swiss system produces a clear winner in just a few rounds, no-one is eliminated and almost everyone wins at least one game, but there are many ties to deal with.
