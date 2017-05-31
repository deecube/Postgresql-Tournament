#!/usr/bin/env python
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
        dbconn = connect()
        cur = dbconn.cursor()
        cur.execute("delete from match_info")
        cur.execute("update player_info set wins=0,matches=0,losses=0;")
        dbconn.commit()
        dbconn.close()
    except:
        print "Could not delete matches from the match_info table"


def deletePlayers():
    """Remove all the player records from the database."""
    try:
        dbconn = connect()
        cur = dbconn.cursor()
        cur.execute("delete from player_info")
        dbconn.commit()
        dbconn.close()
    except:
        print ("Could not delete player information from",
               "the player_info table")


def countPlayers():
    """Returns the number of players currently registered."""
    try:
        dbconn = connect()
        cur = dbconn.cursor()
        cur.execute("select count(id) as num from player_info")
        count = cur.fetchall()
        dbconn.close()
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
        dbconn = connect()
        cur = dbconn.cursor()
        cur.execute("insert into player_info (name) values(%s)", (name,))
        dbconn.commit()
        dbconn.close()
    except:
        print ("Could not insert the player information into",
               "the player_info table")


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    try:
        dbconn = connect()
        cur = dbconn.cursor()
        cur.execute(
            "select id,name,wins,matches from player_info order by wins desc;")
        standings = cur.fetchall()
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
        conn = connect()
        c = conn.cursor()
        c.execute("INSERT INTO match_info (winner, loser) VALUES(%s, %s)",
                  (winner, loser))
        c.execute("UPDATE player_info SET matches=matches+1, wins=wins+1 \
                   WHERE id = %(id_place)s", {'id_place': winner})
        c.execute("UPDATE player_info SET matches=matches+1 \
                   WHERE id = %(place)s", {'place': loser})
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
        pairs = []
        standing = playerStandings()
        for i in range(0, len(standing), 2):
            l = (standing[i][0], standing[i][1],
                 standing[i+1][0], standing[i+1][1])
            pairs.append(tuple(l))
        return pairs
    except:
        print "Encountered an error"
