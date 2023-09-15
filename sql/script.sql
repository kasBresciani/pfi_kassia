create database cro;
use cro;

create table usuarios (
    id int primary key auto_increment,
    nome varchar(255),
    email varchar(255),
    senha varchar(255)
);