<?php

$f_json = "text.json";
$json = file_get_contents("$f_json");
$obj = json_decode($json, true);

$title_one = $obj["cards"];

$sets = [];
for ($i = 0; $i < count($title_one); $i++) {
    $d = $title_one[$i];
    array_push($sets, array($d['count'], $d['color'], $d['shape'], $d['fill']));
}

print_r($sets);
echo '123';

$count = count($sets);
$cards = array();

    // for ($i = 0; $i < $count - 2; $i++) {
    //     for ($j = $i + 1; $j < $count - 1; $j++) {
    //         for ($k = $j + 1; $k < $count; $k++) {
    //             $num = 0;
    //             $lst = array('123', '132', '213', '231', '321', '312', '111', '222', '333');

    //             for ($n = 0; $n < 4; $n++) {
    //                 $a = $sets[$i][$n] . $sets[$j][$n] . $sets[$k][$n];
    //                 if (in_array($a, $lst)) {
    //                     $num += 1;
    //                 }
    //                 if ($num == 4) {
    //                     array_push($cards, array($sets[$i], $sets[$j], $sets[$k]));
    //                 }
    //             }
    //         }
    //     }
    // };

    // for ($i = 0; $i < count($cards); $i++) {
    //     for ($j = 0; $j < count($cards[$i]); $j++) {
    //         $f = $cards[$i][$j];
    //         echo $f[0], $f[1], $f[2], $f[3], '<br>';
    //     }
    //     echo '<br>';
    // };
