# Api Mensajes - T1 ASS

## Estructura de los mensajes

Los mensajes de esta API poseen las siguientes caracteísticas, la lista a continuación es de la forma *Nombre: (Tipo) Descripción*.

* id: (int) Id del mensaje.

* creator: (string) Username del creador del mensaje.

* title: (string) Título del mensaje.

* content: (string) Contenido del mensaje.

* important: (bool) Indica si el mensaje es importante o no (se muestra primero entre los mensajes de la misma jerarquía si toma el valor True)

* private: (bool) Indica si el mensaje es privado, en cuyo caso solo podrá ser accedido por los usuarios cuyos usernames estén detallados en el atributo *recipients* del mensaje (ver más adelante ejemplo [POST] /inbox/sent). Si toma el valor True, se creará también una entrada en la tabla PersonalMessage, indicando a qué usuarios pertenece el mensaje.

* groupal: (bool) Indica si el mensaje es grupal, en cuyo caso solo podrá ser accedido por los miembros del grupo en el cual fue creado el mensaje. Si toma el valor True, se creará también una entrada en la tabla GroupMessage, indicando a qué grupo pertenece el mensaje.

* created_at: (date) Fecha de creación del mensaje.

* updated_at: (date) Última actualización del mensaje.

* votes: (int) Suma neta de votos positivos y negativos que han sido dados al mensaje. Cuando un usuario entrega un voto, se crea una entrada en la tabla Vote, indicando que el usuario ha votado en el mensaje en cuestión (y el valor del voto).

* parent_id: (int) En caso de que el mensaje sea una respuesta a un mensaje anterior, este campo apunta a ese mensaje.

## [GET] Methods

### [GET] /public/messages

Descripción: Obtiene todos los mensajes que hayan sido creados con el atributo private = false. Los mensajes serán entregados en formato JSON.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "message_id": { contenido }, para todos los mensajes publicos.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensajes entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    }
    ,
    "id2":{
    },
}
```

### [GET] /inbox/

Descripción: Obtiene todos los mensajes que han sido recibidos y escritos por el usuario actualmente conectado.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "message_id": { contenido }, para todos los mensajes que corresponde.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.


Ejemplo de mensajes entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    }
    ,
    "id2":{
    },
}
```

### [GET] /inbox/recieved

Descripción: Obtiene todos los mensajes que han sido recibidos por el usuario actualmente conectado.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "message_id": { contenido }, para todos los mensajes que corresponde.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.


Ejemplo de mensajes entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    }
    ,
    "id2":{
    },
}
```

### [GET] /inbox/sent

Descripón: Obtiene todos los mensajes escritos por el usuario actualmente conectado.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "message_id": { contenido }, para todos los mensajes que corresponde.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensajes entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    }
    ,
    "id2":{
    },
}
```

### [GET] /groups/{group_id}/messages

Descripción: Obtiene todos los mensajes que provengan del grupo con id {group_id} y que el usuario actualmente conectado tenga acceso (que no sean privados, o bien si lo son el usuario se encuentra en la lista de involucrados).

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma "message_id": { contenido }, para todos los mensajes que corresponde.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensajes entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    }
    ,
    "id2":{
    },
}
```

### [GET] /public/messages/{message_id}

Descripción: Obtiene el mensaje especificado por {message_id}, en conjunto con todas las respuestas que apliquen al mensaje en cuestión.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma {"message_id": { contenido }, "replies": { contenido }}, para el mensaje de dicho id.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensaje entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    },
    "replies":[
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "etc..."
        }
    ]
}
```

### [GET] /inbox/{message_id}

Descripción: Obtiene el mensaje especificado por {message_id}, en conjunto con todas las respuestas que apliquen al mensaje en cuestión.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma {"message_id": { contenido }, "replies": { contenido }}, para el mensaje de dicho id.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensaje entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    },
    "replies":[
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "etc..."
        }
    ]
}
```

### [GET] /inbox/sent/{message_id}

Descripción: Obtiene el mensaje especificado por {message_id}, en conjunto con todas las respuestas que apliquen al mensaje en cuestión.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma {"message_id": { contenido }, "replies": { contenido }}, para el mensaje de dicho id.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensaje entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    },
    "replies":[
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "etc..."
        }
    ]
}
```

### [GET] /inbox/recieved/{message_id}

Descripción: Obtiene el mensaje especificado por {message_id}, en conjunto con todas las respuestas que apliquen al mensaje en cuestión.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma {"message_id": { contenido }, "replies": { contenido }}, para el mensaje de dicho id.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensaje entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    },
    "replies":[
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "etc..."
        }
    ]
}
```

### [GET] /groups/{group_id}/messages/{message_id}

Descripcion: Obtiene el mensaje especificado por {message_id}, en conjunto con todas las respuestas que apliquen al mensaje en cuestión.

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200 (OK)```, junto con un JSON de la forma {"message_id": { contenido }, "replies": { contenido }}, para el mensaje de dicho id.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

Ejemplo de mensaje entregados:

```json
{
    "id": {
        "id": "int",
        "creator": "string",
        "title": "string",
        "content": "string",
        "important": "bool",
        "private": "bool",
        "groupal": "bool",
        "created_at": "date",
        "updated_at": "date",
        "votes": "int",
        "parent_id": "int"
    },
    "replies":[
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "id": "int",
            "creator": "string",
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": "bool",
            "groupal": "bool",
            "created_at": "date",
            "updated_at": "date",
            "votes": "int",
            "parent_id": "int"
        },
        {
            "etc..."
        }
    ]
}
```

## [POST] Methods

### [POST] /public/messages

Descripción: Crea un mensaje de forma pública, en cual todos los usuarios pueden ver.

Ejempo:

```json
{   "message":
    {
        "title": "string",
        "content": "string",
        "important": "bool"
    }
}
```

Cabe destacar que el resto de los parámetros se manejan de forma interna, ya que son valores que no se ocupan (como private, groupal) o bien que el mismo backend se va a encargar de entregar (como created_at).

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)```, junto con un JSON de la forma "message":{contenido}.

Respuesta en caso de error: Se retornará ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/sent

Descripción: Crea un mensaje privado, el cual **debe** incluir a todos los usuarios que serán receptores del mensaje.

Ejemplo:

```json
    "message":{
        "recipients": ["username1", "username2", "username3"],
        "content": {
            "title": "string",
            "content": "string",
            "important": "bool"
        }
    }
```

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)```, junto con un JSON de la forma "message":{contenido}.

Respuesta en caso de error: Se retornará ```HTTP Status Code 404 (not found)``` si el usuario de destino no existe.```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.


### [POST] /groups/{group_id}/messages

Descripción: Crea un mensaje grupal, privado o no, el cual solo podrá ser visto por los miembros del grupo (y por los usuarios en la lista de receptores, si el atributo *private* está setteado a True). Cabe destacar que el parametro recipients siempre debe estar en el JSON que se entrega, estando vacío si el atributo *private* está setteado a False.

Ejemplo de parámetros, mensaje grupal público:

```json
    "message":{
        "recipients": [],
        "content": {
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": false
        }
    }
```

Ejemplo de parámetros, mensaje grupal privado:

```json
    "message":{
        "recipients": ["groupuser1", "groupuser2"],
        "content": {
            "title": "string",
            "content": "string",
            "important": "bool",
            "private": true
        }
    }
```
Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)```, junto con un JSON de la forma "message":{contenido}.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no pertenece al grupo. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /public/messages/{message_id}

Descripción: Crea una respuesta a un mensaje de categoría publica. Sigue el mismo formato que un mensaje cualquiera, solamente que en este caso el atributo *parent_id* apuntará al mensaje original que se está respondiendo, y será setteado automáticamente por el backend.

Ejemplo:

```json
{   "message":
    {
        "title": "string",
        "content": "string",
        "important": "bool",
    }
}
```

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)```, junto con un JSON de la forma "message":{contenido}.

Respuesta en caso de error: Se retornará ```HTTP Status Code 404 (not found)``` si el mensaje al que se responde no existe. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/recieved/{message_id}

Descripción: Crea una respuesta a un mensaje privado. Sigue el mismo formato que un mensaje cualquiera, solamente que en este caso el atributo *parent_id* apuntará al mensaje original que se está respondiendo.

Ejemplo:

```json
{   "message":
    {
        "title": "string",
        "content": "string",
        "important": "bool"
    }
}
```
Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)```, junto con un JSON de la forma "message":{contenido}.

Respuesta en caso de error: Se retornará ```HTTP Status Code 404 (not found)``` si el mensaje al que se responde no existe. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] groups/{group_id}/messages/{message_id}

Crea una respuesta a un mensaje grupal. Sigue el mismo formato que un mensaje cualquiera, solamente que en este caso el atributo *parent_id* apuntará al mensaje original que se está respondiendo.

Ejemplo:

```json
{   "message":
    {
        "title": "string",
        "content": "string",
        "important": "bool"
    }
}
```

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)```, junto con un JSON de la forma "message":{contenido}.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no pertenece al grupo. ```HTTP Status Code 404 (not found)``` si el mensaje al que se responde no existe. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /public/messages/{message_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/recieved/{message_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/sent/{message_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] groups/{group_id}/messages/{message_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /public/messages/{message_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/recieved/{message_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/sent/{message_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] groups/{group_id}/messages/{message_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {message_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /public/messages/{message_id}/replies/{reply_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/recieved/{message_id}/replies/{reply_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/sent/{message_id}/replies/{reply_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] groups/{group_id}/messages/{message_id}/replies/{reply_id}/upvote

Descripción: Solicita al servidor entregar un upvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace upvote, entonces la entrada de la tabla se reemplaza por un upvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /public/messages/{message_id}/replies/{reply_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/recieved/{message_id}/replies/{reply_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] /inbox/sent/{message_id}/replies/{reply_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [POST] groups/{group_id}/messages/{message_id}/replies/{reply_id}/downvote

Descripción: Solicita al servidor entregar un downvote al mensaje especificado en {reply_id}. Cabe destacar que para realizar el upvote el usuario tiene que poder tener acceso al mensaje.

Si un usuario había realizado un **downvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se elimina (se anula el voto).

Si un usuario había realizado un **upvote** en el mensaje especificado, y luego hace downvote, entonces la entrada de la tabla se reemplaza por un downvote.

El cuerpo de la solicitiud HTTP es vacío (no recibe parámetros)

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 200```, junto con un mensaje que explique si hubo modificación, fue el primer voto o fue nulo.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no tiene acceso. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

## [PUT] Methods

Respuesta en caso de éxito: Se retornará ```HTTP Status Code 201 (Created)``` si se crea un mesaje. ```HTTP Status Code 200``` si se actualiza un mensaje.

Respuesta en caso de error: Se retornará ```HTTP Status Code 401 (Unauthorized)``` si el usuario creador no pertenece al grupo. ```HTTP Status Code 500 (Internal Server Error)``` si hubo un problema del servidor al procesar la solicitud. No se retornará JSON.

### [PUT] /public/messages/{message_id}

### [PUT] /inbox/recieved/{message_id}

### [PUT] /inbox/sent/{message_id}

### [PUT] /groups/{group_id}/messages/{message_id}

### [PUT] /public/messages/{message_id}/replies/{reply_id}

### [PUT] /inbox/recieved/{message_id}/replies/{reply_id}

### [PUT] /inbox/sent/{message_id}/replies/{reply_id}

### [PUT] /groups/{group_id}/messages/{message_id}/replies/{reply_id}