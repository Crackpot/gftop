<?php
$arr_ip = array(
"127.0.0.1",
"218.206.10.123",
"192.221.515.0",
"123.0.0.0.1",
"-12.255.0.10",
"10.9c.132.69",
"255.10.10.255"
);

foreach ($arr_ip as $ip)
{
    if(validateIp($ip))
    {
        echo "<b>$ip 是正确的IP地址</b>";
        echo "<br/><br/>";
    }
    else
    {
        echo "$ip 不是正确的IP地址";
        echo "<br/><br/>";
    }
}

function validateIp($ip)
{
    $iparray = explode(".",$ip);
    for($i=0;$i<count($iparray);$i++)
    {
        if($iparray[$i]>255)
            return (0);
    }
    return ereg("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$",$ip);
}
?>