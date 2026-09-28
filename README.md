Tarea 15 - Colecciones de datos
Programa en Python de consola para llevar un registro sencillo de clientes de un despacho jurídico, usando diccionarios para almacenar la información.
Descripción
Los clientes se guardan en un diccionario donde la llave es el nombre del cliente y el valor es otro diccionario con su teléfono y el tipo de trámite:
clientes = {
    "Juan Pérez": {
        "telefono": "0999999999",
        "tramite": "Divorcio"
    }
}
Funcionalidades
El programa muestra un menú interactivo que se repite hasta que el usuario decide salir:
Opción	Función	Qué hace
1	agregar_cliente()	Solicita nombre, teléfono y tipo de trámite, y los registra.
2	mostrar_clientes()	Muestra todos los clientes registrados (o avisa si no hay ninguno).
3	buscar_cliente()	Busca un cliente por nombre y muestra sus datos.
4	eliminar_cliente()	Elimina un cliente por nombre.
5	Salir	Finaliza el programa.
Requisitos
•	Python 3 (desarrollado con Python 3.13)
Cómo ejecutarlo
1.	Clona o descarga este repositorio.
2.	Abre una terminal en la carpeta del proyecto.
3.	Ejecuta:
4.	python "Tarea 15 - Colecciones de datos.py"
Ejemplo de uso
===== REGISTRO DE CLIENTES =====
1. Agregar cliente
2. Mostrar clientes
3. Buscar cliente
4. Eliminar cliente
5. Salir
Seleccione una opción: 1
Ingrese el nombre del cliente: Juan Pérez
Ingrese el número de teléfono: 0999999999
Ingrese el tipo de trámite: Divorcio
Cliente registrado correctamente.
Conceptos aplicados
•	Diccionarios y diccionarios anidados
•	Funciones con def
•	Entrada de datos con input()
•	Ciclo while True con menú y break
•	Recorrido de colecciones con for y .items()
•	Condicionales (if, elif, else) y operador in
•	Eliminación de elementos con del
•	Formato de texto con f-strings
Limitaciones
•	Los datos se guardan solo en memoria: al cerrar el programa se pierden.
•	Si se ingresa un cliente con un nombre ya existente, se sobrescriben sus datos.
Autor
FRANKLIN LEMA
