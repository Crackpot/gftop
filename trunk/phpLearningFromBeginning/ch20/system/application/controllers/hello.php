<?php
class Hello extends Controller
{
    function index()
    {
        //echo 'Hello World!';
        $data['title'] = "New Title - Hello.php";
        $data['heading'] = "��Һã���ӭʹ��CodeIgniter��ܣ�";
        $this->load->view('helloview1',$data);
    }
    
    function saylucky()
    {
        echo 'It\'s time to say "Good Luck"!';
    }
    
    function sayhello($name)
    {
    	echo "Hello, $name !";
    }
}
?>