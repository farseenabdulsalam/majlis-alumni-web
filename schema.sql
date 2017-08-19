drop table if exists date_suggestions;
create table date_suggestions (
  id serial primary key,
  name text,
  batch text,
  dates text not null
);
drop table if exists programs_suggestions;
create table programs_suggestions (
  id serial,
  name text primary key,
  batch text,
  programs text not null
);
