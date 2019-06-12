create table usuario(
	login VARCHAR primary key,
	senha varchar not null
);


CREATE TABLE editora(
   id SERIAL PRIMARY KEY,
   nome VARCHAR NOT NULL
);

create table livro(
	id SERIAL primary key,
	nome VARCHAR not null,
	autor varchar not null,
	id_editora int,
	foreign key (id_editora) references editora(id)
);
