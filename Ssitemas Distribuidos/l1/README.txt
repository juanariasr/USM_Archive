Sebastian Gutierrez 202073601-4
Juan Arias 202073590-5

Para ejecutar el programa se debe construir la imagen en docker y ejecutar la imagen con los siguientes comandos
docker build -t servidor .
docker run -d -p 8080:8080 app
Posteriormente se debe ejecutar el archivo clientes.go con el siguiente comando
go run clientes.go

Si se agregara una central que ejecute las mismas funciones que la actualmente implementada. ¿Esto beneficiaria o complicaria al proceso?
La implementacion de una central en el proyecto serviria para darle redundancia y hacerlo mas robusto, previniendo asi que, si por alguna razon el servidor central falle, no se pueda seguir ejecutando.
Por otro lado, tambien puede ser util a la hora de escalar el proyecto, manejando un mayor volumen de datos, ya que se puede usar para que trabaje en paralelo con el servidor central distribuyendo la carga

Supuestos
Asumimos que el servidor central queda perpetuamente activo escuchando a los capitanes
Nosotros entendimos que solo el servidor central se ejecuta en docker, por lo tanto ejecutamos los clientes de manera "local"
Cuando el servidor central le asigna el botin a un planeta, le suma la cantidad de botin que encuentra el capitan al planeta con menos botin