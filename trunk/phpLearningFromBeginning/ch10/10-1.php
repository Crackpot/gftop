<?php
$root = getenv('DOCUMENT_ROOT');
$port = getenv('SERVER_PORT');
$file = getenv('SCRIPT_NAME');
$ua = getenv('HTTP_USER_AGENT');
$method = getenv('REQUEST_METHOD');
$protocol = getenv('SERVER_PROTOCOL');

echo "<b>ͨ������getenv()��ȡ��������</b><hr>";
echo "<b>�������ĵ���Ŀ¼��</b>".$root;
echo "<br/>";
echo "<br/>";

echo "<b>�������˿ڣ�</b>".$port;
echo "<br/>";
echo "<br/>";

echo "<b>��ǰִ���ļ���</b>".$file;
echo "<br/>";
echo "<br/>";

echo "<b>�û�UA��</b>".$ua;
echo "<br/>";
echo "<br/>";

echo "<b>���󷽷���</b>".$method;
echo "<br/>";
echo "<br/>";

echo "<b>����Э�飺</b>".$protocol;
?>