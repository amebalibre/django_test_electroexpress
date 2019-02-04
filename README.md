# LEEME

Ejercicio práctico en el que se pretende levantar un API básica para la gestión de una tienda online.
En primera instancia se pretende entender el funcionamiento básico de django, realizar la integración con DRF (Django Rest Framework), generar tests unitarios y la documentación del API.



## Preparación del entorno de desarrollo

Para levantar el API será necesaria

1. La instalación de una base de datos postgres.
2. La instalación de todas las dependencias Python.
3. La ejecución de las migraciones pertinentes.
4. La posterior ejecución del servidor.
5. Y finalmente la generación de datos dummies.



### Instalación de la base de datos mediante Contenedores (Docker)

Para este propósito se ha dejado preparado un fichero `.yml` debajo del subdirectorio *docker_compose.d*, alojado dentro del directorio raíz del proyecto.

Asumiendo que estamos dentro del fichero raíz, ejecutar los siguientes comandos:

```bash
cd ./docker_compose.d
docker-compose up -d
```

Una vez realizado dicho comando, tendremos preparada nuestra DDBB y además habremos levantado el servicio de workbench para administrar la DDBB mediante el cliente web: http:--http://localhost/browser/

> Cuando se deseé eliminar los contenedores, será necesario ejecutar los comandos:
>
> ```bash
> docker stop pg pgadmin
> docker rm pg pgadmin
> docker volume rm dockercomposed_db-data
> ```



### Preparación de las dependencias del entorno

Partiré de la base de que como usuario, conoces `virtualenv` y como se usa.

Al tener definido un fichero `requirements.txt` tan sólo será necesaria la ejecución de los siguientes comandos (partiendo de que estamos hubicados en el raíz del proyecto):

```bash
virtualenv .ENV
source .ENV/bin/activate
pip install -r requirements.txt
```

Una vez ejecutados estos comandos, ya tendremos todas las dependencias Python, ahora sólo necesitaremos realizar la migración de la base de datos, para ello ejecutar desde el raíz:

```bash
cd ./django_test_electroexpress
./manage.py migrate
```

Generar los usuarios:

```bash
./manage.py createsuperuser # username:admin, password: 1234
./manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('user', password='1234').save()
>>> exit()
```



A continuación recomiendo ejecutar este paso, aunque no obligatorio:

* Al no disponer de datos en base de datos, es recomendable abrir el (workbench)[http://localhost/browser] instalado previamente cuando realizamos la puesta en marcha de nuestro entorno dockerizado. Para acceder al workbench usar Username: *fake@mail.io* y Password: *1234*
* A continuación, especificar la conexión a DDBB.  
  * **Host**:  la ip del contenedor docker
  * **Port**: 5432
  * **Username**: django
  * **Password**: django

* y ejecutar el fichero `./src/populate.sql` desde el workbench para poblar las tablas de productos y de promociones, ya que son las tablas "maestras" de DDBB.



Y ya sólo quedará correr el servidor para testar el API.

```bash
./migrate.py runserver
```


#### Adicional...

Si se desea saber qué está ejecutando por debajo nuestro ORM, podemos hacer uso de este comando de tshark (para lo cual será necesario tener el programa `tshark` previamente instalado).

`tshark --color -f "tcp port 5432" -i br-c2bbe8a8d950  -Y "pgsql" -T fields -e pgsql.query -e pgsql.status`

Recuerda modificar el parametro -i, en mi caso docker me ha levantado el servidor en la red `br-c2bbe8a8d950`. Para localizar el conector de red puedes hacer uso de `ifconfig`.

Se obtiene una salida similar a:

```sql
SELECT "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date" FROM "django_session" WHERE ("django_session"."expire_date" > '2019-01-30T20:09:15.767531+00:00'::timestamptz AND "django_session"."session_key" = '5xcbr8viosdnbx4gvg3f9kzydlzydzwn')
SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" = 1
SELECT COUNT(*) AS "__count" FROM "ecommerce_invoice"
SELECT "ecommerce_invoice"."id", "ecommerce_invoice"."name", "ecommerce_invoice"."shipping_cost", "ecommerce_invoice"."payment_date" FROM "ecommerce_invoice" ORDER BY "ecommerce_invoice"."payment_date" ASC  LIMIT 4
SELECT "ecommerce_invoiceline"."id", "ecommerce_invoiceline"."invoice_id", "ecommerce_invoiceline"."product_id", "ecommerce_invoiceline"."quantity", "ecommerce_invoiceline"."price" FROM "ecommerce_invoiceline" WHERE "ecommerce_invoiceline"."invoice_id" = 1
```

> Documentación de [tshark](https://www.wireshark.org/docs/dfref/p/pgsql.html).
