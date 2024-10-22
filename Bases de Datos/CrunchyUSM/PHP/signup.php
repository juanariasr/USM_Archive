<?php
    $pageTitle = "CrunchyUSM || Registro";
?>

<?php require "header.php";?>
        <header class="site-header signUpBasicHeader">
            <a href="index.php" class="brand-container" title="CrunchyUSM">
                <h1>CrunchyUSM</h1>
            </a>
            <a href="login.php" class="signInLink">Ingresar</a>
        </header>
    


    <section class="simpleContainer">
        <div class="centerContainer">
            <form action="process_signup.php" method="POST">
                <div class="regFormContainer">
                    <div class="stepHeader-container">
                        <h1 class="stepTitle">Crea una cuenta en CrunchyUSM</h1>
                    </div>
                    <div class="stepHeader-body">
                        <div class="group">
                            <label for="fname">Nombre de usuario</label>
                            <input type="text" name="username" id="username" autocomplete="off" require>
                        </div>
                        <div class="group">
                            <label for="clave">Contraseña</label>
                            <input type="password" name="contrasena" id="contrasena" autocomplete="off" require>
                        </div>
                    </div>
                    <div class="submitBtnContainer">
                        <button type="submit" name="submitButton">Registrarse</button>
                    </div>
                </div>
            </form>
        </div>
    </section>
</body>
</html>