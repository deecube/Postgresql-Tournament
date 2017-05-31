#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:  
        return psycopg2.connect("dbname=tournament")
    except:
        print "Could not connect to the db"

def deleteMatches():
    """Remove all the match records from the database."""
    try:
        dbconn=connect()
        cur=dbconn.cursor()
        cur.execute("delete from match_info")
        cur.execute("update player_info set wins=0,matches=0,losses=0;")
        dbconn.commit()
        dbconn.close()
    except:
        print "Could not delete matches from the match_info table"        
def deletePlayers():
    """Remove all the player records from the database."""
    try:
        dbconn=connect()
        cur=dbconn.cursor()
        cur.execute("delete from player_info")
        dbconn.commit()
        dbconn.close()
    except:
        print "Could not delete the player information from the player_info table"

def countPlayers():
    """Returns the number of players currently registered."""
    try:
        dbconn=connect()
        cur=dbconn.cursor()
        cur.execute("select count(id) as num from player_info");
        count=cur.fetchall();
        dbconn.close()
        print "count: ", count[0][0]
        return count[0][0]
    except:
        print "Could not make changes to the match_info table"

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    try:
        dbconn=connect()
        cur=dbconn.cursor()
        cur.execute("insert into player_info (name) values(%s)" , (name,))
        #cur.execute("insert into match_info (winner, loser) values(1,2)")
        dbconn.commit()
        dbconn.close()
    except:
        print "Could not insert the player information into the player_info table"



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    try:
        dbconn=connect()
        cur=dbconn.cursor()
        #matches = cur.execute("select player_info.id, player_info.name, count(result.match_id) as no_of_matches from player_info,(select player_info.id,player_info.name, match_info.match_id from player_info,match_info where match_info.winner= player_info.id or match_info.loser=player_info.id) as result where player_info.id=result.id group by player_info.id order by no_of_matches desc;")
        #wins= cur.execute("select player_info.name, results.num_of_wins from player_info,(select winner, count(match_id) as num_of_wins from match_info group by winner) as results where player_info.id=results.winner order by num_of_wins desc; ")
        #ans = cur.execute("select matches.id, matches.name, win.wins, matches.no_of_matches  from (select player_info.id, player_info.name, count(result.match_id) as no_of_matches from player_info,(select player_info.id,player_info.name, match_info.match_id from player_info,match_info where match_info.winner= player_info.id or match_info.loser=player_info.id) as result where player_info.id=result.id group by player_info.id order by no_of_matches desc) as matches,(select player_info.id, player_info.name, results.wins from player_info,(select winner, count(match_id) as wins from match_info group by winner) as results where player_info.id=results.winner order by wins desc) as win where matches.id=win.id;")
        cur.execute("select id,name,wins,matches from player_info order by wins desc;")

        standings=cur.fetchall()
        #print standings
        dbconn.close()
        return standings
    except:
        print "Could not get standings"


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    try:
        add_match_query = 'INSERT INTO match_info (winner, loser) VALUES ({0}, {1});'.format(winner, loser)
        add_winner_query = 'UPDATE player_info SET matches=matches+1, wins=wins+1 WHERE id = {0};'.format(winner)
        add_loser_query = 'UPDATE player_info SET matches=matches+1 WHERE id = {0};'.format(loser)
        conn = connect()
        c = conn.cursor()
        c.execute(add_match_query)
        c.execute(add_winner_query)
        c.execute(add_loser_query)
        conn.commit()
        conn.close()
    except:
        print "Could not update the match winner/ loser"
 

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    try:
        pairs=[]
        standings=playerStandings()
        print standings
        print "Standings: ", standings[0][1]
        print "Len of standings: ", len(standings)
        for i in range(0,len(standings),2):
            print "Inside loop"
            print i
            
            l=standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1]
            print l
            pairs.append(tuple(l))
            print pairs
        return pairs
    except:
        print "Encountered an error"