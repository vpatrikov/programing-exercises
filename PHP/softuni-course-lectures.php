<?php
$word = readline();
$occurences = [];

for($i  = 0; $i < strlen($word); $i++)
{
    $char = $word[$i];
    if(!key_exists($char, $occurences))
    {
        $occurences[$char] = 0;
    }
    $occurences[$char]++;
}

var_dump($occurences);


function repeatStr($n, $str)
{
  $array = array_fill(0, $n, $str);
  return implode($array);
}

function get_average($a) {
 $sum = 0;
 $array = explode(", ", $a);
 foreach ($array as $grade) {
    $sum += $grade;
 }
 return $sum / count($array);
}
