-- Table: public.Books_data

DROP TABLE IF EXISTS public."Books_Data";

CREATE TABLE IF NOT EXISTS public."Books_Data"
(
	Nome_Livro VARCHAR(264) PRIMARY KEY,
	Valor VARCHAR(10),
	Nota int,
	Em_Estoque varchar(128),
	Classificacao varchar(128),
	Comentarios TEXT
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Books_data"
    OWNER to postgres;

COMMENT ON TABLE public."Books_data"
    IS 'Dados sobre livfros para sistemas de recomendação';
