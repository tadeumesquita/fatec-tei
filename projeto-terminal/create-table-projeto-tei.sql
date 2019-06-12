-- Table: public.editora

-- DROP TABLE public.editora;

CREATE TABLE public.editora
(
  id integer NOT NULL DEFAULT nextval('editora_id_seq'::regclass),
  nome character varying NOT NULL,
  CONSTRAINT editora_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.editora
  OWNER TO postgres;


-- Table: public.livro

-- DROP TABLE public.livro;

CREATE TABLE public.livro
(
  id integer NOT NULL DEFAULT nextval('livro_id_seq'::regclass),
  nome character varying NOT NULL,
  autor character varying NOT NULL,
  id_editora integer,
  CONSTRAINT livro_pkey PRIMARY KEY (id),
  CONSTRAINT id_editora_fkey FOREIGN KEY (id_editora)
      REFERENCES public.editora (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.livro
  OWNER TO postgres;


-- Table: public.usuario

-- DROP TABLE public.usuario;

CREATE TABLE public.usuario
(
  login character varying NOT NULL,
  senha character varying NOT NULL,
  nome character varying NOT NULL,
  CONSTRAINT usuario_pkey PRIMARY KEY (login)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.usuario
  OWNER TO postgres;
