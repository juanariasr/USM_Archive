<center>
    <?php
        require 'conexion.php';
        require 'header.php';
        session_start();

        $busqueda = $_POST['busqueda'];
        $busqueda = strtolower($busqueda);


        $query1 = "SELECT * FROM series WHERE nombre like '%$busqueda%'";
        $query2 = "SELECT * FROM peliculas WHERE nombre like '%$busqueda%'";
        $query3 = "SELECT * FROM usuarios WHERE nombre like '%$busqueda%'";

    

        $consulta1 = pg_query($con, $query1);
        $cantidad1 = pg_num_rows($consulta1);
        $consulta2 = pg_query($con, $query2);
        $cantidad2 = pg_num_rows($consulta2);
        $consulta3 = pg_query($con, $query3);
        $cantidad3 = pg_num_rows($consulta3);
        echo "<br><br><br><br><br>";
        echo "Series: <br>";
        for ($i = 1; $i <= $cantidad1; $i++){
            $busqueda = pg_fetch_array($consulta1);
            $id = $busqueda['id'];
            $nombre = $busqueda["nombre"];
            echo "<a href='series.php?id=$id'>{$nombre}</a><br>";
        }
        echo "Peliculas:<br>";
        for ($i = 1; $i <= $cantidad2; $i++){
            $busqueda = pg_fetch_array($consulta2);
            $id = $busqueda['id'];
            $nombre = $busqueda["nombre"];
            echo "<a href='peliculas.php?id=$id'>{$nombre}</a><br>";
        }
        echo "Usuarios:<br>";
        for ($i = 1; $i <= $cantidad3; $i++){
            $busqueda = pg_fetch_array($consulta3);
            $id = $busqueda['id'];
            $nombre = $busqueda["nombre"];
            echo "<a href='usuarios.php?id=$id'>{$nombre}</a><br>";
        }
        if(isset($_SESSION['nombre_usuario'])){
            echo "<center><a href='ingreso.php' style= >volver</a></center>";
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
            echo "<center><a href='index.php'>volver</a></center>";
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
</center>             