<?php
session_start();
if (!isset($_SESSION['user_id'])) {
  if (isset($_COOKIE['user_id']) && isset($_COOKIE['identification_number'])) {
    $_SESSION['user_id'] = $_COOKIE['user_id'];
    $_SESSION['identification_number'] = $_COOKIE['identification_number'];
  }
}
?>
