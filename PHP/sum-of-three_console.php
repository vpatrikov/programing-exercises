<?php
$elements = readline();
$arr = explode(" ", $elements);
for ($i = 0; $i < count($arr); $i++) {
    for ($j = $i + 1; $j < count($arr); $j++) {
        $sum = $arr[$i] + $arr[$j];

        if (in_array($sum, $arr)) {
            echo $arr[$i] . " + " . $arr[$j] . " == " . $sum . PHP_EOL;
        }
    }
}
