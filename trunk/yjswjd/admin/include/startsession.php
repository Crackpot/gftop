<?php
session_start();
if (!isset($_SESSION['admin_id']) && !isset($_SESSION['admin_uuid'])) {// 未登录
  if (isset($_COOKIE['admin_id']) && isset($_COOKIE['admin_uuid']) && isset($_COOKIE['admin_name'])) {// 设置了cookie
    $_SESSION['admin_id'] = $_COOKIE['admin_id'];
    $_SESSION['admin_uuid'] = $_COOKIE['admin_uuid'];
    $_SESSION['admin_name'] = $_COOKIE['admin_name'];
  }// 设置了cookie
}// 未登录
?>
