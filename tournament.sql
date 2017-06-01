-- Table definitions for the tournament project.
--

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament


create table player_info (
	id serial primary key, 
	name text, 
	wins integer default 0, 
	losses integer default 0, 
	matches integer default 0
	);


create table match_info (
	match_id serial primary key, 
	winner integer references player_info(id), 
	loser integer references player_info(id)
	);


 create view winners as select p.id,p.name, count(m.winner) as wins from player_info p left join match_info m on p.id=m.winner group by p.id;

 create view noofmatches as select p.id, p.name, count(p.id) as matches from player_info p, match_info m where p.id=m.winner or p.id=m.loser group by p.id; 