
drop trigger if exists tg_verify_evento_or_agendamento_at_same_time on agendamento;
DROP function if exists verify_evento_or_agendamento_at_same_time;

drop trigger if exists tg_verify_agendamento_esporte on agendamento;
DROP function if exists verify_agendamento_esporte;

drop trigger if exists tg_verify_event_at_same_time on evento_bloco;
DROP function if exists verify_event_at_same_time;

drop function if exists delete_all_agendamentos_between_time;

-- verifica se não há um evento ou um agendamento no mesmo dia no mesmo bloco para cadastrar o
-- novo agendamento de quadra

drop trigger if exists tg_verify_evento_or_agendamento_at_same_time on agendamento;
DROP function if exists verify_evento_or_agendamento_at_same_time;
create or replace function verify_evento_or_agendamento_at_same_time() returns trigger as
$$
declare
    cont integer;
    id_bloco_agendamento varchar(10);
begin
--  verifica se tem outro evento no mesmo bloco no mesmo dia
    id_bloco_agendamento := (select id_bloco from quadra where id_quadra = new.id_quadra);
    raise notice '%', id_bloco_agendamento;
    cont := (select count(*) from
                (select * from evento where ((new.data between data_inicio and data_fim) and (new.hora > hora_inicio or hora_fim < hora_fim))) e
                inner join evento_bloco eb on e.id_evento = eb.id_evento
                inner join (select * from bloco where id_bloco=id_bloco_agendamento) b on b.id_bloco = eb.id_bloco);
    if (cont >= 1) then
        raise exception 'there is already a evento in this bloco at this data and hora';
    end if;
--  verifica se tem outro agendamento na mesma hora
    cont = (select count(*) from agendamento where new.data=data and new.hora=hora and new.id_quadra=id_quadra);
    if (cont >= 1) then
        raise exception 'there is already a agendamento in this quadra at this time and date';
    end if;
    return new;
end
$$
LANGUAGE 'plpgsql';

create trigger tg_verify_evento_or_agendamento_at_same_time
    before insert or update on agendamento
    for each row
    execute procedure verify_evento_or_agendamento_at_same_time();

-- teste:

-- da problema pois já há um evento no bloco dessa quadra
insert into agendamento (data, hora, id_quadra, id_esporte) values ('2021-08-11', '20:00:00', 4, 1);
-- da problema pois já há um agendamento para essa quadra nesse horário
insert into agendamento (data, hora, id_quadra, id_esporte) values ('2021-08-5', '12:30:00', 4, 1);


-- verifica se não há um evento no mesmo dia no mesmo bloco ou agendamento
-- na mesma hora e mesmo dia no mesmo bloco para agendar um evento

drop trigger if exists tg_verify_event_at_same_time on evento_bloco;
DROP function if exists verify_event_at_same_time;
create or replace function verify_event_at_same_time() returns trigger as
$$
declare
    cont integer;
    data_inicio_evento date;
    data_final_evento date;
begin
--  verifica se tem outro evento no mesmo bloco no mesmo dia
    data_inicio_evento := (select data_inicio from evento where id_evento=new.id_evento);
    data_final_evento := (select data_fim from evento where id_evento=new.id_evento);
    cont := (select count(*) from
                (select * from evento_bloco where id_evento=1) eb
                inner join
                    (select * from evento where (
                        ((data_inicio_evento between data_inicio and data_fim) or (data_inicio_evento between data_inicio and data_fim)))) e on e.id_evento=eb.id_evento
                inner join (select * from bloco where id_bloco=new.id_bloco) b on b.id_bloco = eb.id_bloco);
    if (cont >= 1) then
        raise exception 'there is already a evento in this bloco at this data and hora';
    end if;
    return new;
end
$$
LANGUAGE 'plpgsql';

create trigger tg_verify_event_at_same_time
    before insert or update on evento_bloco
    for each row
    execute procedure verify_event_at_same_time();

select * from bloco;
select * from evento;
select * from evento_bloco;
select * from quadra;
select * from quadra_esporte;
select * from agendamento;
select * from esporte;

-- teste
insert into evento (titulo, data_inicio, data_fim, hora_inicio, hora_fim) values ('SEI', '2021-08-10', '2021-08-11', '19:00:00', '12:00:00');

-- aqui vai dar problema ao tentar atribuir esse evento ao bloco binásio
insert into evento_bloco values (4, 'Ginasio');
delete from evento where id_evento=6;

-- garante que um agendamento de quadra só pode ser feito em uma quadra que tenha o esporte solicitado

create or replace function verify_agendamento_esporte() returns trigger as
$$
declare
    cont integer;
begin
    cont := (select count(*) from
                (select * from quadra where id_quadra=new.id_quadra) q
                    join
                (select * from quadra_esporte where id_esporte=new.id_esporte) qe
                on q.id_quadra = qe.id_quadra);
    if (cont = 0) then
        raise exception 'Essa quadra não tem o esporte desejado';
    end if;
    return new;
end
$$
LANGUAGE 'plpgsql';

create trigger tg_verify_agendamento_esporte
    before insert or update on agendamento
    for each row
    execute procedure verify_agendamento_esporte();


select * from bloco;
select * from evento;
select * from evento_bloco;
select * from quadra;
select * from quadra_esporte;
select * from agendamento;
select * from esporte;

-- teste
insert into agendamento (data, hora, id_quadra, id_esporte) values ('2021-08-5', '14:00:00', 5, 3);

-- deleta todos os agendamentos dado um range de tempo

create or replace function delete_all_agendamentos_between_time(data_inicio date, data_fim date, hora_inicio time, hora_fim time) returns void as
$$
begin
    delete from agendamento
        where (data between data_inicio and data_fim) and (hora between hora_inicio and hora_fim);
end
$$
LANGUAGE 'plpgsql';

