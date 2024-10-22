<?php 
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
            echo "<a href='perfil.php'>$usuario</a>";
            ?>
        </header>
    </section>
    <section class="banner">
        <img src="../images/banner.png" alt="fondo del index" class= "our-story-card-background">
        <div class="our-story-card-text">
            <form action="process_buscar.php" class="global-search" method = "POST">
                <div class="f-group">
                    <input type="text" name="busqueda" placeholder="Buscar animes" autocomplete="off">
                    <button type="submit" name="submit">Buscar</button>
                </div>
                <br><br>
                <center>
                    <div class="contenido-index">
                        <a href="">Animes por genero</a>
                        <br><br>
                        <a href="">Animes por orden alfabetico</a>
                        <br><br>
                        <a href="">Animes mas populares</a>                        
                        <br><br>
                    </div>
                
                <div>
                    <?php
                        echo "<h1>Top 5 anime con mayor popularidad:</h1>";
                        require 'conexion.php';
                        require 'header.php';

                        $query = "SELECT id,nombre FROM top_popular";

                        $consulta = pg_query($con, $query);
                        $cantidad = pg_num_rows($consulta);
                        for($i = 0; $i < $cantidad; $i++){
                            $busqueda = pg_fetch_array($consulta);
                            $top = $busqueda["nombre"];
                            $id = $busqueda['id'];
                            echo "<a href='series.php?id=$id'>{$top}</a><br>";
                        }
                        echo "<br>";
                        
                        echo "<h2>Top 5 anime con menor popularidad:</h2>";
                        $query = "SELECT id,nombre FROM bottom_popular";

                        $consulta = pg_query($con, $query);
                        $cantidad = pg_num_rows($consulta);
                        for($i = 0; $i < $cantidad; $i++){
                            $busqueda = pg_fetch_array($consulta);
                            $top = $busqueda["nombre"];
                            $id = $busqueda['id'];
                            echo "<a href='series.php?id=$id'>{$top}</a><br>";
                        }
                        echo "<br>";
                    
                        echo "<h3>Top 5 anime con mayor cantidad de comentarios:</h3>";
                        $query = "SELECT id,nombre FROM top_comentarios";

                        $consulta = pg_query($con, $query);
                        $cantidad = pg_num_rows($consulta);
                        for($i = 0; $i < $cantidad; $i++){
                            $busqueda = pg_fetch_array($consulta);
                            $top = $busqueda["nombre"];
                            $id = $busqueda['id'];
                            echo "<a href='series.php?id=$id'>{$top}</a><br>";
                        }
                    ?>
                    </center>
                </div>
            </form>
            
        </div>
    </section>
</body>
</html>