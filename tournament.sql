-- Table definitions for the tournament project.
--

\c tournament
create table player_info (id serial primary key, name text, wins integer default 0, losses integer default 0, matches integer default 0);
create table match_info (match_id serial primary key, winner integer references player_info(id), loser integer references player_info(id));
