<?php
 session_start();
 require 'conexion.php';
 require 'header.php';
if(isset($_SESSION['nombre_usuario'])){
    $id_pelicula = pg_escape_string($con, $_GET['id_pelicula']);
    $usuario = $_SESSION['nombre_usuario'];

    $id_pelicula = substr($id_pelicula, 1, -1);

    $query = "SELECT id FROM usuarios WHERE nombre = '$usuario'";
    $consulta = pg_query($con, $query);
    $busqueda = pg_fetch_array($consulta);
    $id_usuario = $busqueda['id'];

    $query = "SELECT id FROM usuario_ha_visto_serie WHERE id_usuario = '$id_usuario' AND id_serie = $id_pelicula";
    $consulta = pg_query($con, $query);
    $cantidad = pg_num_rows($consulta);

    if(($cantidad==0)){
        $query = "INSERT INTO public.usuario_ha_visto_serie(id_serie, id_usuario)
        VALUES ('$id_pelicula', '$id_usuario');";
        $consulta = pg_query($con, $query);
        header("location:series.php?id=$id_pelicula");
    } else{
        echo "Ya viste este anime<br>";
        echo "<a href = series.php?id=$id_pelicula>Volver</a>";
    }
}
else{
    header('location:index.php');
}
?>