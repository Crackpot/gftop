<?php
session_start();

if($_SESSION['user_id'] && $_SESSION['user_name'])
{
    unset($_SESSION['user_id']);
    unset($_SESSION['user_name']);
    header("Location: index.php");
}
?>
