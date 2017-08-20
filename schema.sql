drop table if exists date_suggestions;
drop table if exists registration;
create table registration (
  id serial primary key,
  name text not null,
  batch text not null,
  contact text not null,
  dates text not null
);
drop table if exists programs_suggestions;
create table programs_suggestions (
  id serial,
  name text primary key,
  batch text,
  programs text not null
);
