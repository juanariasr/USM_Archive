<?php
session_start();
require 'conexion.php';
require 'header.php';
if(isset($_SESSION['nombre_usuario'])){
    if(isset($_GET['id_a_seguir']) && isset($_GET['seguidor'])){
        $id_a_seguir = pg_escape_string($con, $_GET['id_a_seguir']);
        $id_a_seguir = substr($id_a_seguir, 1, -1);
        $usuario = $_SESSION['nombre_usuario'];
        $query = "SELECT id FROM usuarios WHERE nombre = '$usuario'";
        $consulta = pg_query($con, $query);
        $consulta = pg_fetch_array($consulta);
        $id_usuario = $consulta['id'];

        $query = "SELECT id FROM usuario_seguidor WHERE id_seguidor= '$id_usuario' AND id_seguido = $id_a_seguir";
        $consulta = pg_query($con, $query);
        $consulta = pg_fetch_array($consulta);
        $cantidad = pg_num_rows($consulta);

        if($cantidad > 0){
            
        }

    }
    else{
        header('location:index.php');
    }
}
else{
    header('location:index.php');
}





?>