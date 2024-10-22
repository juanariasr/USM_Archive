<?php
    $pageTitle = "CrunchyUSM || Iniciar Sesion";
?>

<?php require "header.php";?>
        <header class="site-header signUpBasicHeader">
            <a href="index.php" class="brand-container" title="CrunchyUSM">
                <h1>CrunchyUSM</h1>
            </a>
            <a href="signup.php" class="signInLink">Crear una cuenta</a>
        </header>
    


    <section class="simpleContainer">
        <div class="centerContainer">
            <form action="process_login.php" method="POST">
                <div class="regFormContainer">
                    <div class="stepHeader-container">
                        <h1 class="stepTitle">Inicia Sesion en CrunchyUSM</h1>
                    </div>
                    <div class="stepHeader-body">
                        <div class="group">
                            <label for="username">Nombre de usuario</label>
                            <input type="text" name="username" id="username" autocomplete="off" require>
                        </div>
                        <div class="group">
                            <label for="contrasena">Contraseña</label>
                            <input type="password" name="contrasena" id="contrasena" autocomplete="off" require>
                        </div>
                    </div>
                    <div class="submitBtnContainer">
                        <button type="submit" name="submitButton">Iniciar Sesion</button>
                    </div>
                </div>
            </form>
        </div>
    </section>
</body>
</html>