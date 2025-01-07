# Gestión Segura de Recursos Educativos

Este es un proyecto de ciberseguridad para la gestión segura de recursos educativos dentro de la universidad CEU. El sistema gestiona recursos internos como aulas, equipos tecnológicos, horarios y material didáctico de manera segura, teniendo en cuenta las mejores prácticas de seguridad para aplicaciones web y móviles.

## Tecnologías utilizadas

- **Django**: Framework web para desarrollar la aplicación.
- **Docker**: Para contenedores y despliegue de la aplicación.
- **PostgreSQL**: Base de datos relacional.
- **GitHub**: Repositorio para el control de versiones.
- **OWASP Top 10**: Enfoque en la detección y mitigación de los riesgos más críticos en la seguridad de las aplicaciones web.

## Descripción del Proyecto

El proyecto tiene como objetivo desarrollar una plataforma web y móvil que permita gestionar recursos educativos de manera segura, siguiendo los principios de seguridad establecidos en el OWASP Top 10. Se implementarán soluciones para cada uno de los riesgos identificados en este listado, desde la exposición de datos sensibles hasta la inyección de código.

### Características principales

- **Gestión de Aulas**: Registro y visualización de aulas disponibles.
- **Gestión de Equipos Tecnológicos**: Administración de equipos como ordenadores, proyectores, etc.
- **Gestión de Material Didáctico**: Control de los recursos materiales disponibles para los docentes.
- **Seguridad**: Implementación de las mejores prácticas de seguridad para cada componente del sistema.

## Instalación

### Requisitos previos

- Python 3.8 o superior.
- Docker y Docker Compose.
- PostgreSQL.

### Pasos para configurar el entorno

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/usuario/gestion-segura-recursos-educativos.git
    cd gestion-segura-recursos-educativos
    ```

2. **Configurar el entorno virtual y dependencias:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows, usa 'venv\Scripts\activate'
    pip install -r requirements.txt
    ```

3. **Configurar Docker:**

    Asegúrate de tener Docker y Docker Compose instalados. Luego, configura y levanta los contenedores de la base de datos y la aplicación.

    ```bash
    docker-compose up
    ```

4. **Realizar las migraciones de la base de datos:**

    ```bash
    python manage.py migrate
    ```

5. **Ejecutar el servidor localmente:**

    ```bash
    python manage.py runserver
    ```

### Uso

Accede a la aplicación web desde `http://127.0.0.1:8000`. Puedes empezar a explorar las diferentes funcionalidades para gestionar los recursos educativos.

## OWASP Top 10

Cada uno de los siguientes riesgos de seguridad del OWASP Top 10 ha sido abordado en el proyecto. Se han creado commits que muestran tanto el riesgo como su solución:

1. **A1: Inyección** - Prevención de inyecciones SQL.
2. **A2: Autenticación rota** - Implementación de autenticación segura.
3. **A3: Exposición de datos sensibles** - Cifrado de datos sensibles.
4. **A4: Entidades externas XML (XXE)** - Protección contra ataques XXE.
5. **A5: Control de acceso deficiente** - Mejora de los controles de acceso.
6. **A6: Configuración de seguridad incorrecta** - Configuración de seguridad adecuada.
7. **A7: Cross-Site Scripting (XSS)** - Protección contra ataques XSS.
8. **A8: Deserialización insegura** - Implementación de medidas contra la deserialización insegura.
9. **A9: Uso de componentes con vulnerabilidades conocidas** - Uso de dependencias seguras.
10. **A10: Insuficiencia de registro y monitoreo** - Implementación de logs adecuados.

## Contribuciones

Este proyecto está abierto a contribuciones. Si deseas aportar al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu contribución (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.