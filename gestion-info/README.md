# Sistema de Gestión de Usuarios

Este sistema CRUD permite gestionar el ciclo de vida de usuarios mediante consola, garantizando la persistencia de datos en archivos JSON.

## Descripción

El sistema permite registrar, consultar, actualizar y eliminar usuarios de una organización.
Los datos se almacenan automáticamente en el archivo `data/records.json`.

Además, incluye la generación de usuarios de prueba mediante la librería Faker, lo que permite simular datos reales y facilitar pruebas del sistema.

---

## Estructura del proyecto

```
gestion-info/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── records.json          # Base de datos local (JSON)
└── src/
    ├── main.py               # Punto de entrada
    ├── menu.py               # Interfaz de consola
    ├── service.py            # Lógica CRUD
    ├── file.py               # Persistencia JSON
    ├── validate.py           # Validaciones y utilidades
    └── integration.py        # Integración con Faker
```

---

## Requisitos

* Python 3.10 o superior
* pip

---

## Cómo ejecutar el programa

### 1. Clonar el repositorio

```
git clone https://github.com/tu-usuario/gestion-info.git
cd gestion-info
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate
```

### 3. Instalar dependencias

```
pip install -r requirements.txt
```

### 4. Ejecutar el programa

```
cd src
python main.py
```

---

## Funcionalidades

| Opción | Descripción        |
| ------ | ------------------ |
| 1      | Crear usuario      |
| 2      | Listar usuarios    |
| 3      | Buscar usuario     |
| 4      | Actualizar usuario |
| 5      | Eliminar usuario   |
| 0      | Salir              |

---

## Tecnologías y conceptos utilizados

* Python
* Estructuras de datos (listas, diccionarios, sets)
* Programación modular
* Manejo de archivos JSON
* Manejo de excepciones (`try-except`)
* List comprehensions
* Funciones lambda
* Librerías externas (Faker)

---

## Librerías externas

* Faker: generación de datos de prueba realistas

---

## Etiquetas de desarrollo

| Tag      | Descripción                      |
| -------- | -------------------------------- |
| m0-setup | Estructura base del proyecto     |
| m1-data  | Manejo de datos en memoria       |
| m2-files | Persistencia en archivos         |
| m3-crud  | Implementación completa del CRUD |

---

## Pruebas

Este proyecto usa `pytest` para las pruebas unitarias.

### Cómo ejecutar las pruebas

#### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 2. Correr las pruebas
```bash
cd gestion-info
pytest tests/
```

#### 3. Ver resultado detallado
```bash
pytest tests/ -v
```

### Pruebas incluidas

| Prueba | Descripción |
|---|---|
| `test_validate_user_valid` | Verifica que un usuario válido no genera errores |
| `test_validate_user_invalid_email` | Verifica que un email inválido es rechazado |
| `test_validate_user_invalid_age` | Verifica que una edad inválida es rechazada |
| `test_create_user` | Verifica que un usuario se crea correctamente |
