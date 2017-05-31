-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

\c tournament
create table player_info (id serial primary key, name text, wins integer default 0, losses integer default 0, matches integer default 0);
create table match_info (match_id serial primary key, winner integer references player_info(id), loser integer references player_info(id));
