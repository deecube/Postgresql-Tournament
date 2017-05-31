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
