-- Table definitions for the tournament project.
--

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament


create table player_info (
	id serial primary key, 
	name text
	);


create table match_info (
	match_id serial primary key, 
	winner integer references player_info(id) ON DELETE CASCADE, 
	loser integer references player_info(id) ON DELETE CASCADE
	);


 CREATE VIEW winners AS 
 SELECT p.id,p.name, COUNT(m.winner) AS wins 
 FROM player_info p LEFT JOIN match_info m 
 ON p.id=m.winner GROUP BY p.id;

 CREATE VIEW noofmatches AS 
 SELECT p.id, p.name, COUNT(p.id) AS matches 
 FROM player_info p, match_info m 
 WHERE p.id=m.winner or p.id=m.loser 
 GROUP BY p.id; 

 CREATE VIEW standings AS 
 SELECT n.id, n.name, w.wins, n.matches 
 FROM noofmatches n JOIN winners w 
 ON w.id = n.id ORDER BY wins DESC;