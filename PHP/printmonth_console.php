<?php
echo "Enter months: " . PHP_EOL;
$input = readline();
$array = array_map("intval", explode(' ', $input));
$months = [
    1 => 'January', 2 => 'February', 3 => 'March', 4 => 'April', 5 => 'May', 6 => 'June', 7 => 'July',
    8 => 'August', 9 => 'September', 10 => 'October', 11 => 'November', 12 => 'December'
];

foreach ($array as $number) {
    if (!array_key_exists($number, $months)) {
        echo "Invalid Month!" . PHP_EOL;
    } else {
        echo $months[$number] . PHP_EOL;
    }
}
