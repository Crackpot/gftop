<?php
$doc = new DOMDocument();
$doc->load("17-1.xml");

$books = $doc->getElementsByTagName("book");
foreach($books as $book)
{
    $authors = $book->getElementsByTagName("author");
    $author = $authors->item(0)->nodeValue;
    
    $publishers = $book->getElementsByTagName("publisher");
    $publisher = $publishers->item(0)->nodeValue;
    
    $titles = $book->getElementsByTagName("title");
    $title = $titles->item(0)->nodeValue;
    
    $prices = $book->getElementsByTagName("price");
    $price = $prices->item(0)->nodeValue;
    
    echo "$title - $author - $publisher - $price";
    echo "<br/>";
    echo "<br/>";
}
?>