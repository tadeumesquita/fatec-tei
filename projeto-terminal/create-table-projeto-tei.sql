create table usuario(
	login VARCHAR primary key,
	senha varchar not null,
	nome varchar not null
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

'DUMP DO BANCO

--
-- PostgreSQL database dump
--

-- Dumped from database version 10.8 (Ubuntu 10.8-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.8 (Ubuntu 10.8-0ubuntu0.18.04.1)

-- Started on 2019-06-12 04:49:29 -03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2939 (class 1262 OID 16384)
-- Name: projeto-final-tei; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "projeto-final-tei" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE "projeto-final-tei" OWNER TO postgres;

\connect -reuse-previous=on "dbname='projeto-final-tei'"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 13041)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2941 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 198 (class 1259 OID 16406)
-- Name: editora; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.editora (
    id integer NOT NULL,
    nome character varying NOT NULL
);


ALTER TABLE public.editora OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 16404)
-- Name: editora_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.editora_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.editora_id_seq OWNER TO postgres;

--
-- TOC entry 2942 (class 0 OID 0)
-- Dependencies: 197
-- Name: editora_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.editora_id_seq OWNED BY public.editora.id;


--
-- TOC entry 200 (class 1259 OID 16417)
-- Name: livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livro (
    id integer NOT NULL,
    nome character varying NOT NULL,
    autor character varying NOT NULL,
    id_editora integer
);


ALTER TABLE public.livro OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 16415)
-- Name: livro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livro_id_seq OWNER TO postgres;

--
-- TOC entry 2943 (class 0 OID 0)
-- Dependencies: 199
-- Name: livro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livro_id_seq OWNED BY public.livro.id;


--
-- TOC entry 196 (class 1259 OID 16396)
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    login character varying NOT NULL,
    senha character varying NOT NULL,
    nome character varying NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 2799 (class 2604 OID 16409)
-- Name: editora id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editora ALTER COLUMN id SET DEFAULT nextval('public.editora_id_seq'::regclass);


--
-- TOC entry 2800 (class 2604 OID 16420)
-- Name: livro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro ALTER COLUMN id SET DEFAULT nextval('public.livro_id_seq'::regclass);


--
-- TOC entry 2931 (class 0 OID 16406)
-- Dependencies: 198
-- Data for Name: editora; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.editora (id, nome) FROM stdin;
2	editora
3	editora 3
1	Editora
4	TESTESASD asd asdew 
5	asdasd 
\.


--
-- TOC entry 2933 (class 0 OID 16417)
-- Dependencies: 200
-- Data for Name: livro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.livro (id, nome, autor, id_editora) FROM stdin;
1	Livro	Autor	1
2	Livro Bacana	Autor Gente Boa	2
3	Livro Bacana	Autor Gente Boa	2
4	Teste	Teste	4
\.


--
-- TOC entry 2929 (class 0 OID 16396)
-- Dependencies: 196
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (login, senha, nome) FROM stdin;
tadeumesquita	teste123	Tadeu Campos Mesquita
jose	123	Jose da Silva
\.


--
-- TOC entry 2944 (class 0 OID 0)
-- Dependencies: 197
-- Name: editora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.editora_id_seq', 5, true);


--
-- TOC entry 2945 (class 0 OID 0)
-- Dependencies: 199
-- Name: livro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livro_id_seq', 4, true);


--
-- TOC entry 2804 (class 2606 OID 16414)
-- Name: editora editora_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editora
    ADD CONSTRAINT editora_pkey PRIMARY KEY (id);


--
-- TOC entry 2806 (class 2606 OID 16425)
-- Name: livro livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro
    ADD CONSTRAINT livro_pkey PRIMARY KEY (id);


--
-- TOC entry 2802 (class 2606 OID 16403)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (login);


--
-- TOC entry 2807 (class 2606 OID 16426)
-- Name: livro livro_id_editora_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro
    ADD CONSTRAINT livro_id_editora_fkey FOREIGN KEY (id_editora) REFERENCES public.editora(id);


-- Completed on 2019-06-12 04:49:29 -03

--
-- PostgreSQL database dump complete
--


