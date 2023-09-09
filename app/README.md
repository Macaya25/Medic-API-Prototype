# iaps Jobs API

## Variables de ambiente

Las variables de ambiente son las siguiente

```
DATABASE_URL=driver://user:pwd@host:port/db_name
TOKEN_SECRET_KEY="token"
```

## Setup inicial

Para iniciar el servicio es necesario correr las migraciones mediante el comando

```
docker exec {CONTAINER_ID} alembic upgrade head
```

## Para iniciar el servicio

```
docker compose up
```

# Configuración de nuevos jobs

## Registro

El registro de un nuevo job se realiza mediante la creación de una nueva seed en la bse de datos. Para esto se genera una nueva migración mediante el comando: `alembic revision -m "Añadir aqui descipcion de migracion"`

Un nuevo registro de job necesita:

- id: Un id unico para identificación dentro de la base de datos
- name: El nombre del tipo de job, ej: OPTMIZATION
- dag_name: El nombre del DAG de Airflow que se va a ejecutar con la configuración generada
- params_schema: El esquema de la estructura del json de los parametros que recibe inicialmente el job. Se usa para validar que los campos ingresados correpondan con los minimos para la ejecución. Como referencia se puede usar este recurso para la sintaxis https://json-schema.org/learn/miscellaneous-examples.html
