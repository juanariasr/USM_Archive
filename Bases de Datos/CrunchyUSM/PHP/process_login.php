<?php
require 'conexion.php';
session_start();
$usuario = $_POST['username'];
$clave = $_POST['contrasena'];

$query = "SELECT * FROM usuarios WHERE nombre = '$usuario' AND contrasena = '$clave'";
$consulta = pg_query($con, $query);
$cantidad = pg_num_rows($consulta);
if ($cantidad > 0){
    $_SESSION['logeado'] = true;
    $_SESSION['nombre_usuario'] = $usuario;
    header("location:ingreso.php");
    echo "Sesion iniciada correctamente";
} else {
    echo "Datos incorrectos";
}
?>