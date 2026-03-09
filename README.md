---

# Next Technologies – Technical Test

Este repositorio contiene la solución a la prueba técnica, la cual está dividida en dos partes:

1. **Procesamiento y transferencia de datos (ETL)**
2. **Implementación de lógica de aplicación**

La idea principal es tomar el dataset proporcionado, procesarlo utilizando Python, transformarlo para que cumpla con un esquema definido y almacenarlo en una base de datos.
Además, se implementa una pequeña aplicación que permite identificar qué número fue eliminado de un conjunto de los primeros 100 números naturales.

---

# Tecnologías utilizadas

Para resolver la prueba se utilizaron las siguientes herramientas:

* **Python 3.12** para el procesamiento de datos y la lógica del programa
* **PostgreSQL** como base de datos relacional
* **Docker** para levantar fácilmente la base de datos
* **Pandas** para manipulación y limpieza de datos
* **SQLAlchemy** y **Psycopg2** para la conexión con PostgreSQL
* **PyArrow** para trabajar con archivos Parquet
* **Python-dotenv** para manejar variables de entorno

---

# Instalación y ejecución

## 1. Clonar el repositorio

Comando:
git clone https://github.com/JorgeJuarez07/python_desafio_proxima_tecnologia.git
cd python_desafio_proxima_tecnologia

## 2. Crear un entorno virtual

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto.

Comando:
python3 -m venv env
source env/bin/activate

En Windows el comando de activación sería:

Comando:
env\Scripts\activate

## 3. Configurar variables de entorno

Primero se debe crear un archivo `.env` en la raíz del proyecto con la configuración de la base de datos.

```env
DATABASE_NAME=db_Siguiente_Tecnologia
DATABASE_USER=postgres
DATABASE_PASSWORD=TuPasswordSegura
DATABASE_HOST=localhost
DATABASE_PORT=5438
```


Es importante verificar que el puerto configurado no esté siendo utilizado por otro contenedor.
Esto se puede revisar con:

Comando:
docker ps

Si el puerto está ocupado, se puede cambiar por otro disponible y actualizar también el archivo `docker-compose.yml`.

---

## 4. Levantar la base de datos

La base de datos se ejecuta utilizando Docker.

Comando:
docker compose up -d

Este comando levantará el contenedor de PostgreSQL en segundo plano.

---

## 5. Instalar dependencias

Después se deben instalar las dependencias necesarias del proyecto:

Comando:
pip install -r requirements.txt

---

# Sección 1 – Procesamiento y Transferencia de Datos

En esta sección se implementa un pequeño proceso **ETL (Extract, Transform, Load)** para trabajar con el dataset proporcionado.

---

# Flujo del proceso

El flujo general del procesamiento de datos es el siguiente:

```
Dataset CSV
   ↓
Extracción con Python (Pandas)
   ↓
Transformación de datos
   ↓
Almacenamiento intermedio en Parquet
   ↓
Carga final en PostgreSQL
```

---

# Carga de información

Para almacenar la información se utilizó **PostgreSQL**.

La razón principal es que el dataset tiene relaciones claras entre entidades, por ejemplo entre compañías y transacciones.
Una base de datos relacional facilita manejar este tipo de relaciones y permite mantener la integridad de los datos.

Además, PostgreSQL es una base de datos robusta y muy utilizada en entornos de producción.

---

# Extracción

La extracción de los datos se realizó utilizando **Python** junto con la librería **Pandas**, ya que ofrece herramientas muy prácticas para trabajar con datasets.

El formato elegido para almacenar temporalmente los datos fue **Parquet**.

Se eligió este formato porque:

* reduce el tamaño de los archivos
* permite lecturas más rápidas
* es muy utilizado en pipelines de datos

### Retos encontrados

*Durante el desarrollo surgieron algunos retos pequeños:
*Configurar correctamente el entorno para trabajar con archivos Parquet (pyarrow).
*Manejar correctamente el formato de fechas del dataset.
*Asegurar que los tipos de datos coincidieran con el esquema de PostgreSQL.
*Verificar que el puerto de Docker no estuviera ocupado.
---

# Transformación

Antes de cargar la información en la base de datos se realizaron algunas transformaciones para que los datos cumplieran con el esquema solicitado.

Entre los cambios realizados:

* eliminación de registros con campos críticos vacíos
* conversión de fechas a formato `datetime`
* normalización de algunos campos

Por ejemplo, las fechas originalmente venían en el siguiente formato:

```
2023-01-01T00:00:00
```

Estas se convirtieron a objetos `datetime` para poder manejarlas correctamente dentro de Python y PostgreSQL.

---

# Dispersión de la información

Para almacenar la información se crearon dos tablas principales:

* **companies**: contiene el catálogo de compañías
* **charges**: contiene las transacciones realizadas

Ambas tablas están relacionadas mediante una clave foránea.

### Diagrama simple de la base de datos

```
companies
---------
id (PK)
company_name

      │
      │
      ▼

charges
---------
id (PK)
company_id (FK)
amount
status
created_at
updated_at
```

Esta estructura permite evitar duplicación de información y mantener las relaciones entre compañías y transacciones.

---

# Ejecutar el proceso ETL

El proceso completo se puede ejecutar con:

Comando:
python section_1_etl/main_etl.py

Este script se encarga de:

1. leer el dataset
2. limpiar y transformar los datos
3. insertar la información en la base de datos

---

# Vista SQL para reportes

Se creó una vista que permite consultar el monto total transaccionado por día para cada compañía.

```sql
CREATE OR REPLACE VIEW vw_total_transactions_per_day AS
SELECT 
    created_at::DATE AS transaction_day,
    company_name,
    SUM(amount) AS total_amount,
    COUNT(id) AS total_transactions
FROM charges
GROUP BY transaction_day, company_name
ORDER BY transaction_day DESC, total_amount DESC;
```

Esta vista facilita consultar rápidamente los totales diarios por compañía.

---

# Sección 2 – Lógica de Aplicación

En esta parte se implementa una pequeña aplicación que permite identificar qué número fue eliminado de un conjunto de los primeros **100 números naturales**.

---

# Implementación

Se creó una clase llamada **`NumberSet`** que representa el conjunto de números del 1 al 100.

Esta clase incluye el método:

```
extract(number)
```

Este método permite eliminar un número del conjunto, validando previamente que:

* sea un número entero
* esté dentro del rango de 1 a 100

---

# Algoritmo utilizado

Para calcular el número faltante se utilizó la **fórmula de Gauss**, que permite obtener la suma de una secuencia de números consecutivos.

La fórmula es:

`S = n * (n + 1) / 2`

Para el caso de los números del 1 al 100:

1. se calcula la suma esperada de todos los números
2. se calcula la suma del conjunto actual
3. la diferencia entre ambos valores indica qué número falta

Este enfoque permite resolver el problema de forma sencilla y eficiente.

---

# Ejecutar la aplicación

El programa puede ejecutarse desde consola pasando el número que se desea extraer.

Comando:
python section_2_api/number_logic.py 45

---
