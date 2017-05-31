# Tournament Planner
## A Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project requires Python 2.7 and the following Python libraries installed:

* [Psycopg2](http://initd.org/psycopg/)

Description of the project files:

* `tournament.sql` - this file is used to set up the database schema.
* `tournament.py` - this file is used to provide access to your database via a library of functions which can add, delete or query data in the database to another python program (a client program). 
* `tournament_test.py` - this is a client program which will use your functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py.

