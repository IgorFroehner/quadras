
-- DROP DATABASE quadras;
-- CREATE DATABASE quadras;

DROP TABLE IF EXISTS public.bolsista;
DROP TABLE IF EXISTS public.usuario;
DROP TABLE IF EXISTS public.quadra_esporte;
DROP TABLE IF EXISTS public.quadra;
DROP TABLE IF EXISTS public.agendamento;
DROP TABLE IF EXISTS public.evento_bloco;
DROP TABLE IF EXISTS public.bloco;
DROP TABLE IF EXISTS public.esporte;
DROP TABLE IF EXISTS public.evento;
DROP TYPE IF EXISTS tipo_usuario;
DROP TYPE IF EXISTS turnos;


CREATE TYPE tipo_usuario AS ENUM ('usuario', 'adm', 'bolsista');

CREATE TABLE public.usuario(
    cpf char(11) primary key,
    email varchar(150) not null,
    senha varchar(50) not null,
    permissao tipo_usuario not null default 'usuario'
);

CREATE TYPE turnos AS ENUM ('manha', 'tarde', 'noite');

CREATE TABLE public.bolsista(
    cpf char(11),
    turno turnos,
    foreign key (cpf) references usuario(cpf)
);

CREATE TABLE bloco (
    id_bloco varchar(10) primary key
);

CREATE TABLE quadra (
    id_quadra serial primary key,
    largura numeric(4, 2) not null,
    comprimento numeric(4, 2) not null,
    id_bloco varchar(10) not null,
    foreign key (id_bloco) references bloco(id_bloco)
);

CREATE TABLE esporte (
    id_esporte serial primary key,
    nome varchar(40) unique not null
);

CREATE TABLE agendamento (
    id_agendamento serial primary key,
    data date,
    hora time,
    id_quadra integer,
    id_esporte integer,
    foreign key (id_quadra) references quadra(id_quadra),
    foreign key (id_esporte) references esporte(id_esporte)
);

CREATE TABLE quadra_esporte (
    id_quadra integer not null,
    id_esporte integer not null,
    foreign key (id_quadra) references quadra(id_quadra),
    foreign key (id_esporte) references esporte(id_esporte)
);

CREATE TABLE evento (
    id_evento serial not null primary key,
    titulo varchar(100) not null,
    data_inicio date not null,
    data_fim date not null,
    hora_inicio time,
    hora_fim time
);

CREATE TABLE evento_bloco (
    id_evento integer not null,
    id_bloco varchar(10) not null,
    foreign key (id_bloco) references bloco(id_bloco),
    foreign key (id_evento) references evento(id_evento)
);


INSERT INTO quadra(LARGURA, COMPRIMENTO, ID_BLOCO) VALUES (30, 40, 'Ginasio');
INSERT INTO quadra_esporte values (4, 1);
INSERT INTO quadra_esporte values (4, 2);
INSERT INTO quadra_esporte values (4, 3);




