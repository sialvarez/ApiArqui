# Api Usuarios - Grupos - T1 ASS

## [GET] Methods

### [GET] /users

Descripción: Obtiene todos los usuarios que hayan sido creados. 

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "user_id": { contenido }, para todos los usuarios existentes.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

```python
{
    id: {
        id: int  # id de usuario.
        username: string # Nombre de cuenta
        name: string # Nombre del usuario.
        middleName: string # Apellido(s) del usuario.
        birthdate: date # Fecha de nacimiento del usuario.
        created_at: date
        updated_at: date
    }
    ...
}
```

### [GET] /users/{user_id}

Descripción: Obtiene el usuario con el user_id solicitado. 

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "user_id": { contenido } para ese usuario en particular.

Respuesta en caso de error: Se retornará ```HTTP Status Code 204 (No Content)``` si el user_id especificado no se encuentra en la base de datos, o ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

```python
{
    id: {
        id: int  # id de usuario.
        username: string # Nombre de cuenta
        name: string # Nombre del usuario.
        middleName: string # Apellido(s) del usuario.
        birthdate: date # Fecha de nacimiento del usuario.
        created_at: date
        updated_at: date
    }
}
```

### [GET] /users/{user_id}/groups

Descripción: Obtiene todos los grupos a los que pertenece el usuario con id user_id. 

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "group_id": { contenido }.

Respuesta en caso de error: Se retornará ```HTTP Status Code 204 (No Content)``` si el user_id no se encuentra en la base de datos, o ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

```python
{
    id: {
        id: int  # id de grupo.
        name: string # Nombre del grupo.
        membersCount: int # Cantidad de miembros en el grupo.
        created_at: date
        updated_at: date
    }
    ...
}
```

### [GET] /groups

Descripción: Obtiene todos los grupos que han sido creados. 

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "group_id": { contenido }, para todos los usuarios existentes.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la request No se retornará JSON.

```python
{
    id: {
        id: int  # id de grupo.
        name: string # Nombre del grupo.
        membersCount: int # Cantidad de miembros en el grupo.
        created_at: date
        updated_at: date
    }
    ...
}
```

### [GET] /groups/{group_id}

Descripción: Obtiene el grupo con el group_id solicitado. 

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "group_id": { contenido }.

Respuesta en caso de error: Se retornará ```HTTP Status Code 204 (No Content)``` si el group_id no se encuentra en la base de datos, o ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

```python
{
    id: {
        id: int  # id de grupo.
        name: string # Nombre del grupo.
        membersCount: int # Cantidad de miembros en el grupo.
        created_at: date
        updated_at: date
    }
}
```

### [GET] /groups/{group_id}/users

Descripción: Obtiene todos los usuarios que pertenecen al grupo con id group_id.
 
Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "user": { contenido }.

Respuesta en caso de error: Se retornará ```HTTP Status Code 204 (No Content)``` si el group_id no se encuentra en la base de datos, o ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

```python
{
    id: {
        id: int  # id de usuario.
        username: string # Nombre de cuenta
        name: string # Nombre del usuario.
        middleName: string # Apellido(s) del usuario.
        birthdate: date # Fecha de nacimiento del usuario.
        created_at: date
        updated_at: date
    }
    ...
}
```

## [POST] Methods

### [POST] /users

Descripción: Crea un usuario.

Parámetros a entregar:

```python
{
    id: {
        username: string # Nombre de cuenta
        passwordHash: string # la password ya pasada por una función hash.
        name: string # Nombre del usuario.
        middleName: string # Apellido(s) del usuario.
        birthdate: date # Fecha de nacimiento del usuario.
    }
    ...
}
```

Los parámetros que no se deben entregar es porque son manejados internamente.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)```, junto con un JSON de la forma "user":{contenido}:

```python
{
    id: {
        id: int  # id de usuario.
        username: string # Nombre de cuenta
        name: string # Nombre del usuario.
        middleName: string # Apellido(s) del usuario.
        birthdate: date # Fecha de nacimiento del usuario.
        created_at: date
        updated_at: date
    }
}
```
Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene permisos suficientes para crear un nuevo usuario. ```HTTP Status Code 409 (Conflict)``` si el usuario a crear ya existe en la base de datos. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /users/delete

Descripción: Elimina el usuario actual. No recibe parámetros. No retorna JSON.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```.

Respuesta en caso de error: Se retornará ```HTTP Status Code 304 (Not Modified)``` si no se pudo borrar al usuario, o ```HTTP Status Code 500 (Internal Server Error)``` si hubo un  problema del servidor al procesa la solicitud. No se retornará JSON.


### [POST] /groups

Descripción: Crea un grupo y luego relaciona el grupo al usuario que está conectado actualmente.

Parámetros a entregar:

```python
{
    id: {
        name: string # Nombre del grupo.
    }
    ...
}
```
membersCount será 1 dado que recién se está creando (es el usuario conectado).

Respuesta en caso de éxito: Se retornará  ```HTTP Status Code 201 (Created)``` junto con un JSON de la forma "group_id":{contenido}:

```python
{
    id: {
        id: int  # id de grupo.
        name: string # Nombre del grupo.
        membersCount: int # Cantidad de miembros en el grupo.
        created_at: date
        updated_at: date
    }
}
```

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene permisos suficientes para crear un nuevo grupo. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /groups/{group_id}

Descripción: Añade al grupo con group_id todos los usuarios con ids id1, id2, etc.

Parámetros a entregar:
```python
{
    users: {
        id1: int,
        id2: int,
        ...
    }
}
```
Respuesta en caso de éxito: Se retornará  ```HTTP Status Code 204 (No Content)```. No se retornará JSON.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene permisos suficientes para crear un editar un grupo. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /groups/{group_id}/remove

Descripción: Remueve del grupo con group_id todos los usuarios con ids id1, id2, etc.

Parámetros a entregar:
```python
{
    users: {
        id1: int,
        id2: int,
        ...
    }
}
```
Respuesta en caso de éxito: Se retornará  ```HTTP Status Code 204 (No Content)```. No se retornará JSON.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene permisos suficientes para crear un editar un grupo. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.


### [POST] /groups/{group_id}/delete

Descripción: Elimina el grupo con id group_id. No recibe parámetros.

Respuesta en caso de éxito: Se retornará  ```HTTP Status Code 204 (No Content)```. No se retornará JSON.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene permisos suficientes para crear un editar un grupo. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.
