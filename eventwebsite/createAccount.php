<?php
     require 'dbconfig/config.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->

    <title>Title goes here</title>

    <!-- Google font -->
    <link href="https://fonts.googleapis.com/css?family=Poppins:400,700,900" rel="stylesheet">

    <!-- Bootstrap -->
    <link type="text/css" rel="stylesheet" href="css/bootstrap.min.css" />

    <!-- Owl Carousel -->
    <link type="text/css" rel="stylesheet" href="css/owl.carousel.css" />
    <link type="text/css" rel="stylesheet" href="css/owl.theme.default.css" />

    <!-- Font Awesome Icon -->
    <link rel="stylesheet" href="css/font-awesome.min.css">

    <!-- Custom stlylesheet -->
    <link type="text/css" rel="stylesheet" href="css/style.css" />

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
              <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
              <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
            <![endif]-->
</head>

<body>
    

    <!-- Header -->
    <header id="header">
        <!-- container -->
        <div class="container">
            <!-- navbar header -->
            <div class="navbar-header">
                <!-- Logo -->
                <div class="navbar-brand">
                    <a class="logo" href="index.html">
                        <img class="logo-img" src="./img/logo.png" alt="logo">
                        <img class="logo-alt-img" src="./img/logo-alt.png" alt="logo">
                    </a>
                </div>
                <!-- /Logo -->

                <!-- Mobile toggle -->
                <button class="navbar-toggle">
                        <i class="fa fa-bars"></i>
                    </button>
                <!-- /Mobile toggle -->
            </div>
            <!-- /navbar header -->

            <!-- Navigation -->
            <nav id="nav">
                <ul class="main-nav nav navbar-nav navbar-right">
                    <li><a href="index.html#home">Home</a></li>
                </ul>
            </nav>
            <!-- /Navigation -->

        </div>
        <!-- /container -->
    </header>
    <!-- /Header -->

    <!-- /LOGIN -->
    <div class="createaccount">
        <img src="avatar.png" class="avatar">
        <h2 style="color:#dd0a37">SIGN UP</h2>
        <form method="POST" action="createAccount.php">
            <p>NAME</p>
            <input type="text" name="" placeholder="FIRST NAME" required>
            <p>USERNAME</p>
            <input type="text" name="username" placeholder="Username" required>
            <p>PASSWORD</p>
            <input type="password" name="password" placeholder="password">
            <p>RE-ENTER PASSWORD</p>
            <input type="password" name="rpassword" placeholder="password">
            <p>EMAIL-ID</p>
            <input type="email" name="" placeholder="abc@email.com" required>
            <p>CONTACT</p>
            <input type="text" name="" required>
            <input type="submit" name="submit" value="SUBMIT" class="button">

            
            
        </form>

        <?php 
            if(isset($_POST['submit'])){
                //echo '<script type="text/javascript"> alert("Sign up clicked") </script>';

                $username = $_POST['username'];
                $password = $_POST['password'];
                $rpassword = $_POST['rpassword'];

                //check if the passwords match
                if($password == $rpassword)
                {
                    $query = "select * from login WHERE username = '$username'";
                    $query_run = mysqli_query($con,$query);

                    if(mysqli_num_rows($query_run)>0)
                    {
                        //username already taken
                        echo '<script type="text/javascript"> alert("USERNAME ALREADY TAKEN") </script>';
                    }
                    else{
                        $query = "INSERT INTO login (username,password) VALUES ('$username','$password')";
                        $query_run = mysqli_query($con,$query);

                        if($query_run)
                        {
                           echo '<script language="javascript">';
                           echo 'alert("REGISTERED")';
                           echo '</script>';
                           header('location:login.php');
                        }
                        else
                        {
                            echo '<script type="text/javascript"> alert("ERROR") </script>';
                        }

                    }
                }
            }

        ?>

    </div>


   

    <div class="section">
        <div class="container">
            <div class="row">

            </div>
        </div>
    </div>

    

</body>

</html>
