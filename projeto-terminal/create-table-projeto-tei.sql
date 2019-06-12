CREATE TABLE editora
(
  id SERIAL NOT NULL,
  nome character varying NOT NULL,
  CONSTRAINT editora_pkey PRIMARY KEY (id)
)

CREATE TABLE livro
(
  id SERIAL NOT NULL,
  nome character varying NOT NULL,
  autor character varying NOT NULL,
  id_editora integer,
  CONSTRAINT livro_pkey PRIMARY KEY (id),
  CONSTRAINT id_editora_fkey FOREIGN KEY (id_editora)
      REFERENCES editora (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)

CREATE TABLE usuario
(
  login character varying NOT NULL,
  senha character varying NOT NULL,
  nome character varying NOT NULL,
  CONSTRAINT usuario_pkey PRIMARY KEY (login)
)

INSERT INTO usuario VALUES ('aluno','aluno123','Aluno');
