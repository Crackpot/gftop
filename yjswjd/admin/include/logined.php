<?php
function is_logined() {// 检测是否已登录
  if (isset($_SESSION['admin_id']) && isset($_SESSION['admin_uuid'])) {// 已登录
    return true;
  }// 已登录
  else {// 未登录
    return false;
  }// 未登录
}// 检测是否已登录
?>
