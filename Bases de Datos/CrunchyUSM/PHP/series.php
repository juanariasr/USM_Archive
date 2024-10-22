<?php 
if(isset($_GET['id'])){
    session_start();
    require 'conexion.php';
    require 'header.php';

    $id = pg_escape_string($con, $_GET['id']);


    $query = "SELECT * FROM series WHERE id = '$id'";
    $consulta = pg_query($con, $query);
    $consulta = pg_fetch_array($consulta);

    $img = $consulta['img_link'];
    
}
else{
    header('location:index.php');
}
?>
<br><br>
<center><h1><?php echo $consulta['nombre']?></h1></center>
<br>
<p>numero de comentarios: <?php echo  $consulta['numero_comentarios']?></p>
<br>
<p>descripcion: <?php echo $consulta['descripcion']?></p>
<br>
<p>cantidad de episodios: <?php echo $consulta['cantidad_episodios']?></p>
<br>
<p>puntuacion media: <?php echo $consulta['puntuacion_media']?></p>
<br>

<?php
$query = "SELECT id_serie, id_genero FROM genero_serie WHERE id_serie = $id";
$consulta = pg_query($con, $query);
$cantidad = pg_num_rows($consulta);
echo "<p>generos:</p>";
for ($i = 0; $i < $cantidad; $i++){
    $busqueda = pg_fetch_array($consulta);
    $id_serie = $busqueda['id_serie'];
    $id_genero = $busqueda["id_genero"];
    $query = "SELECT genero FROM generos WHERE id = '$id_genero'";
    $consulta2 = pg_query($con, $query);
    $busqueda2 = pg_fetch_array($consulta2);
    $gen = $busqueda2['genero'];
    echo "$gen/";
}?>
<br>
Comentarios: <br>
<?php
    $query = "SELECT comentario, id_usuario FROM comentarios_series WHERE id_serie = $id_serie";
    $consulta = pg_query($con, $query);
    $cantidad = pg_num_rows($consulta);
    for ($i = 0; $i < $cantidad; $i++){
        $busqueda = pg_fetch_array($consulta);
        $comentario = $busqueda['comentario'];
        $id_usuario = $busqueda['id_usuario'];

        $query2 = "SELECT nombre FROM usuarios WHERE id = '$id_usuario'";
        $consulta2 = pg_query($con, $query2);
        $busqueda2 = pg_fetch_array($consulta2);
        $n_usuario = $busqueda2['nombre'];

        echo "<a href='usuarios.php?id=$id_usuario'>{$n_usuario}</a>: {$comentario}<br>";
    }
?>
<center><?php echo "<img src = '../$img' width=' 30%'> "?></center>
<?php
if(isset($_SESSION['nombre_usuario'])){
    ?>
    <center>
    <section class="simpleContainer">
        <div class="centerContainer">
            <form action="process_comment_series.php" method="POST">
                <div class="regFormContainer">
                <div class="stepHeader-body">
                <div class="group">
                    <input type="text" name="comentario" id='comentario' autocomplete="off" require>
                    <input type="hidden" name="id_serie" id="id_serie" value=<?=$id?>>
                </div>
            <div class="submitBtnContainer">
            <button type="submit" name="submitButton">Comentar</button>
            <form/>
            <a href="process_ver_series.php?id_pelicula={<?=$id?>}">VER</a>
    </center>
    <?php  
    echo "<center><a href='ingreso.php'>volver</a></center>";
}
else{
    echo "<center><a href='index.php'>volver</a></center>";
}

if(isset($_SESSION['nombre_usuario'])){
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
    <?php
    
}
else{
    ?>
    <section class="site-container">
        <header class="site-header">
            <div class="brand-container">
            <a href="login.php">Ingresar</a>
            </div>
            <a href="signup.php">Crea una cuenta</a>
        </header>
    </section>
    <?php
}
?>