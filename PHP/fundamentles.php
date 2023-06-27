<?php
function reversed_string($str)
{
    $reversed = strrev($str);
    return $reversed;
}

function makeNumNegative($num)
{
    if ($num > 0) {
        return $num * -1;
    } else {
        return $num;
    }
}

function getGrade($a, $b, $c)
{
    $average = ($a + $b + $c) / 3;

    if ($average >= 90) {
        return 'A';
    } elseif ($average >= 80) {
        return 'B';
    } elseif ($average >= 70) {
        return 'C';
    } elseif ($average >= 60) {
        return 'D';
    } else {
        return 'F';
    }
}

function simpleMultiplication($number)
{
    if ($number % 2 == 0) {
        return $number * 8;
    } else {
        return $number * 9;
    }
}
