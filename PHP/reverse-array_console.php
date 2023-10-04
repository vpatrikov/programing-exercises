<?php
echo "Enter the size of your array: ";
$size = readline();
$array = new SplFixedArray($size);
echo "Enter the elements of the array: ";
$array = explode(" ", readline());
echo implode(array_reverse($array));
?>