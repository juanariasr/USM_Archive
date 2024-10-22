<?php 
    require "conexion.php";
    require "header.php";
    session_start();
    if(!isset($_SESSION['nombre_usuario'])){
        header("location:index.php");
    }
    $usuario=$_SESSION['nombre_usuario'];
    ?>
    <section class="site-container">
        <header class="site-header">
            <div class="brand-container">
            <?php
                echo "<a href = 'salir.php'>Salir</a>"
            ?>
            </div>
            <?php
            $usuario = $_SESSION['nombre_usuario'];
            echo "<a href='perfil.php'>$usuario</a>";
            ?>
        </header>
    </section>
 
<br><br><br><br><br><br>
<center>
<?php
    echo "<h1>Perfil de $usuario</h1><br>";
    $query = "SELECT id, cantidad_seguidores FROM usuarios WHERE nombre='$usuario'";
    $consulta = pg_query($con, $query);
    $busqueda = pg_fetch_array($consulta);
    $id_usuario = $busqueda['id'];
    $cant_seguidores = $busqueda['cantidad_seguidores'];
?>    

<h2>Historial:</h2>
<?php
$query = "SELECT id_serie, id_usuario FROM usuario_ha_visto_serie WHERE id_usuario = $id_usuario";
$consulta = pg_query($con, $query);
$cantidad_series_vistas = pg_num_rows($consulta);
for ($i = 0; $i < $cantidad_series_vistas; $i++){
    $busqueda = pg_fetch_array($consulta);
    $id_serie = $busqueda['id_serie'];

    $query2 = "SELECT nombre FROM series WHERE id = '$id_serie'";
    $consulta2 = pg_query($con, $query2);
    $busqueda2 = pg_fetch_array($consulta2);
    $n_serie = $busqueda2['nombre'];

    echo "<a href='series.php?id=$id_serie'>{$n_serie}</a><br>";
}

$query = "SELECT id_usuario, id_pelicula FROM usuario_ha_visto_pelicula WHERE id_usuario = $id_usuario";
$consulta = pg_query($con, $query);
$cantidad_peliculas_vistas = pg_num_rows($consulta);
for ($i = 0; $i < $cantidad_peliculas_vistas; $i++){
    $busqueda = pg_fetch_array($consulta);
    $id_pelicula = $busqueda['id_pelicula'];

    $query2 = "SELECT nombre FROM peliculas WHERE id = '$id_pelicula'";
    $consulta2 = pg_query($con, $query2);
    $busqueda2 = pg_fetch_array($consulta2);
    $n_pelicula = $busqueda2['nombre'];
    echo "<a href='peliculas.php?id=$id_pelicula'>{$n_pelicula}</a><br>";
}
?>
<br>
<h3>Cantidad de seguidores:</h3> <?php echo $cant_seguidores?> <br><br>
<h4>Cantidad de anime visto:</h4> <?php echo $cantidad_series_vistas + $cantidad_peliculas_vistas?>
</center>