create table lots_goszakup
(
    id                   integer                             not null
        constraint lots_goszakup_pk
            primary key,
    lot_number           text,
    ref_lot_status_id    integer,
    last_update_date     timestamp,
    union_lots           boolean,
    count                double precision,
    amount               double precision,
    name_ru              text,
    name_kz              text,
    description_ru       text,
    description_kz       text,
    customer_id          integer,
    customer_bin         bigint,
    trd_buy_number_anno  text,
    trd_buy_id           integer,
    dumping              boolean,
    dumping_lot_price    integer,
    psd_sign             smallint,
    consulting_services  boolean,
    is_light_industry    boolean,
    is_construction_work boolean,
    disable_person_id    boolean,
    customer_name_kz     text,
    customer_name_ru     text,
    ref_trade_methods_id integer,
    index_date           timestamp,
    system_id            integer,
    single_org_sign      smallint,
    relevance            timestamp default CURRENT_TIMESTAMP not null
);