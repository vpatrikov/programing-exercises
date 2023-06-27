<?php
// NOT WORKING
function stray($arr)
{
    for ($i = 0; $i < count($arr); $i++) {
        for ($n = 0; $n < count($arr) - $i - 1; $n++) {
            if ($arr[$n] > $arr[$n + 1]) {
                $temp = $arr[$n];
                $arr[$n] = $arr[$n + 1];
                $arr[$i + 1] = $temp;
            }
        }
        return end($arr);
    }
}
