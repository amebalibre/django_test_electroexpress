# Notas

De momento no hay una doc formalizada.

Es un cumulo de notas personales.

Todo el documento va sin acentos debido al mapeo de teclado (pereza mia de ponerme es-ES, sorry xD).


### Instalacion de base de datos mediante Contenedores (Docker)

*  En el dicrectorio *docker_compose.d* se encuentra el `*.yml` necesario para levantar la DDBB junto a un pgadmin.
*  Para ello, ejecutar: `docker-compose up -d` y seran levantados automaticamente dos contendores llamados *pg* y *pgadmin*.


# Preparacion del entorno

*  Generar con `virtualenv` un entorno virtual para python: `virtualenv .env`
*  Abrir el entorno virtual: `source .env/bin/activate`
*  Instalar dependencias desde fichero *requirements.txt*: `pip install -r requirements.txt`
*  Realizar migraciones: `./manage.py makemigrations` y `./manage.py migrate`
*  Ejecutar servidor: `./migrate.py runserver`


### [TSHARK]((https://www.wireshark.org/docs/dfref/p/pgsql.html))

Mediante el siguiente comando se puede realizar un sniffeo de las queries ejecutadas por el ORM sobre nuestra DDBB.

`tshark --color -f "tcp port 5432" -i br-c2bbe8a8d950  -Y "pgsql" -T fields -e pgsql.query -e pgsql.status`

Recuerda modificar el parametro -i, en mi caso docker me ha levantado el servidor en la red `br-c2bbe8a8d950`. Para localizar el conector de red puedes hacer uso de `ifconfig`.

Se obtiene una salida similar a:

```
SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date" FROM "django_session" WHERE ("django_session"."expire_date" > '2019-01-30T20:09:15.767531+00:00'::timestamptz AND "django_session"."session_key" = '5xcbr8viosdnbx4gvg3f9kzydlzydzwn')
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1
SELECT COUNT(*) AS "__count" FROM "ecommerce_invoice"
SELECT "ecommerce_invoice"."id", "ecommerce_invoice"."name", "ecommerce_invoice"."shipping_cost", "ecommerce_invoice"."payment_date" FROM "ecommerce_invoice" ORDER BY "ecommerce_invoice"."payment_date" ASC  LIMIT 4
SELECT "ecommerce_invoiceline"."id", "ecommerce_invoiceline"."invoice_id", "ecommerce_invoiceline"."product_id", "ecommerce_invoiceline"."quantity", "ecommerce_invoiceline"."price" FROM "ecommerce_invoiceline" WHERE "ecommerce_invoiceline"."invoice_id" = 1
```


### A destacar

*  Los nombres de facturas son gestionados mediante un modulo externo de django (`django-sequences`), el cual se encarga de bloquear DDBB y asignar un nombre unico al nombre de la factura mediante el uso de sequencias.



### TODO List (Con prioridad)

*  Documentar el API
*  Generacion de tests unitarios (no es posible implantar TDD).
*  Completar modelo: Comment
*  Intentar evitar `@property` para campos como total_promos (Invoice)
