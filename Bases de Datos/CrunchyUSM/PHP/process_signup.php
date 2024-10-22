<?php

require 'conexion.php';
$usuario = $_POST['username'];
$clave = $_POST['contrasena'];

$query = "SELECT * FROM usuarios WHERE nombre = '$usuario' AND contrasena = '$clave'";
$consulta = pg_query($con, $query);
$cantidad = pg_num_rows($consulta);
if ($cantidad > 0){
    echo "Este usuario ya existe";
} else {
    
    $query = "INSERT INTO public.usuarios(nombre, contrasena) VALUES ('$usuario', '$clave')";
    $consulta = pg_query($con, $query);
    header("location:login.php");
}
?>