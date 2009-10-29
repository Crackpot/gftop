<?php
class Page
{
    public $title="音乐唱片大全";
    public $content;//Page content.
    public $keywords="MP3,音乐,唱片,music";//Page keywords.
    
    //Page tabs navigation
    public $buttons= array(
    '主页'=>'#',
    '产品'=>'#',
    '服务'=>'#',
    '联系我们'=>'#',
    '网站地图'=>'#'
    );

    public function DisplayTitle()
    {
        echo "<title>";
        echo $this->title;
        echo "</title>\r\n";
    }

    public function DisplayContent()
    {
        echo $this->content;
    }

    public function DisplayKeywords()
    {
        echo "<meta name=\"keywords\" content=\"";
        echo $this->keywords;
        echo "\" />\r\n";
    }

    public function DisplayPage()
    {
        echo "<html>\r\n<header>";
        $this->DisplayTitle();
        $this->DisplayStyles();
        $this->DisplayKeywords();
        echo "</header>\r\n<body>";
        
        $this->DisplayHeader();
        $this->DisplayMenus($this->buttons);
        $this->DisplayContent();
        
        $this->DisplayFooter();
        echo "</body>\r\n</html>";
    }

    public function DisplayStyles()
    {
        echo "<style>";
        echo "h1{color:#000000; font-size:24pt; text-align:center;font-family:arial,sans-serif}";
        echo ".menu{color:#256114; font-size:12pt; text-align:center;font-family:arial,sans-serif; font-weight:bold}";
        echo "td{background:#EFEFEF}";
        echo "p{color:black; font-size:12pt; text-align:justify;font-family:arial,sans-serif}";
        echo "p.foot{color:#256114; font-size:9pt; text-align:center;font-family:arial,sans-serif; font-weight:bold}";
        echo "a:link,a:visited,a:active{color:#256114}";
        echo "</style>";
     }

    public function DisplayHeader()
    {
        echo "<table width=\"100%\" cellpadding =\"12\" cellspacing =\"0\" border =\"0\">";
        echo "<tr>";
        echo "<td align =\"left\"><img src = \"apache.gif\" /></td>";
        echo "<td bgcolor=\"#FFFFFF\">";
        echo "    <h1>音乐唱片大全</h1>";
        echo "</td>";
        echo "<td align =\"right\"></td>";
        echo "</tr>";
        echo "</table>";
    }

    public function DisplayMenus($buttons)
    {
        if(is_array($buttons) && count($buttons)==0) 
            return;
        echo "<table width=\"100%\" bgcolor=\"#FFFFFF\" cellpadding=\"4\"  cellspacing=\"4\"\n";
        echo "  <tr>\n";
    
        //calculate button size
        $width = 100/count($buttons);
    
        while (list($name, $url) = each($buttons))
        {
           $this -> DisplayButton($width, $name, $url, !$this->IsURLCurrentPage($url));
        }
        echo "  </tr>\n";
        echo "</table>\n";
    }

    public function IsURLCurrentPage($url)
    {
        if(strpos($_SERVER['PHP_SELF'], $url )==false)
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    public function DisplayButton($width, $name, $url, $active = true)
    {
        if ($active)
        {
            echo "<td width =\"$width%\" align=\"center\">";
            echo "<a href = \"$url\">";
            echo "<a href =\" $url \"><span class=\"menu\">$name</span></a></td>";
        }  
        else
        {
            echo "<td width =\"$width%\">";
            echo "<img src =\"side-logo.gif\">";
            echo "<span class=\"menu\">$name</span></td>";
        }  
    }

    public function DisplayFooter()
    {
        echo "<table width = \"100%\" bgcolor =\"black\" cellpadding =\"12\" border =\"0\">";
        echo "<tr>";
        echo "<td>";
        echo "<p class=\"foot\">版权所有 &copy; 2008 &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;Powerd by Apache + PHP + MySQL</p>";
        echo "</td>";
        echo "</tr>";
        echo "</table>";
    }
}
?>