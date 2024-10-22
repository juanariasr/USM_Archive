<?php
require 'conexion.php';
session_start();


$usuario = $_SESSION['nombre_usuario'];
$comment = $_POST['comentario'];
$pelicula  = $_POST['id_pelicula'];

$query = "SELECT id FROM usuarios WHERE nombre = '$usuario'";
$consulta = pg_query($con, $query);
$busqueda = pg_fetch_array($consulta);
$id_usuario = $busqueda['id'];


$query = "INSERT INTO public.comentarios_peliculas(id_usuario, id_pelicula, comentario)
	VALUES ('$id_usuario', '$pelicula', '$comment');";
$consulta = pg_query($con, $query);

header("location:peliculas.php?id=$pelicula")

?> 