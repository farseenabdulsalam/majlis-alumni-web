drop table if exists date_suggestions;
create table date_suggestions (
  id integer primary key autoincrement,
  name text,
  batch text,
  dates text not null
);
drop table if exists programs_suggestions;
create table programs_suggestions (
  id integer primary key autoincrement,
  name text,
  batch text,
  programs text not null
);
