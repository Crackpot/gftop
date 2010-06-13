<?php
    //将文件移至服务器的根目录的upload目录下，upload事先得建立好，其目录为：/srv/www/htdocs/upload，为wwwrun www所属
    echo "\$_SERVER['DOCUMENT_ROOT']的位置：".$_SERVER['DOCUMENT_ROOT']."<br/>";
    $upload_path = $_SERVER['DOCUMENT_ROOT']."/upload/";
    $dest_file = $upload_path.basename($_FILES['myfile']['name']);

    if(move_uploaded_file($_FILES['myfile']['tmp_name'],$dest_file)){
    	echo "文件已上传至服务器根目录的upload目录下";
    }
    else{
    	echo "文件上传时发生了一个错误".$_FILES['myfile']['error']."<br/>";
        echo '<a href="./3-06.html">返回并重新上传</a>';
    }
?>
