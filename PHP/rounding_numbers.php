<?php
$array = explode(" ", readline());

foreach ($array as $item)
{
    echo $item . " => " . round($item, 0, PHP_ROUND_HALF_UP) . PHP_EOL;
}

