<?php
require 'conexion.php';
session_start();


$usuario = $_SESSION['nombre_usuario'];
$comment = $_POST['comentario'];
$serie  = $_POST['id_serie'];


$query = "SELECT id FROM usuarios WHERE nombre = '$usuario'";
$consulta = pg_query($con, $query);
$busqueda = pg_fetch_array($consulta);
$id_usuario = $busqueda['id'];


$query = "INSERT INTO public.comentarios_series(comentario, id_usuario, id_serie)
	VALUES ('$comment', '$id_usuario', '$serie');";
$consulta = pg_query($con, $query);

header("location:series.php?id=$serie")

?> 