
requisitos:

- docker
- docker-compose

1. Clonar proyecto
2. dentro de la carpeta del proyecto ejecutar el comando docker-compose up -d
3. para auto configurar la base de dato y el usuario root ejecute en el navegador o en postman la petición GET: http://localhost/setup/auto-setup
    esto creará un usuario root con el siguiente acceso: username: admin@root.com password: 123456
4. Todos las peticiones tienen una autenticación Bearer, por lo que para interactuar con el sistema se debe estar logueado, excepto para las peticiones de http://localhost/item/find y http://localhost/item/all
5. Las notificaciones sin ver por el administrador se contarán al momento de loguearse mostrando la cantidad.
6. la secuencia de configuración sería la siguiente
  -crear un nuevo usuario
  -loguearse con el nuevo usuario
  -copiar el token generado para utilizarse en las peticiones
  -crear los brand para los ítem
  -crear los ítem vinculado con los brand
 
 
 7. se crearon servicios para poder visualizar las notificaciones del administrador como también las estadísticas

 8. para ejecutar las pruebas unitarias en la raíz de la carpeta server ejecutar el comando: pytest