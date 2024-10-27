<?php

$old = ['1.jpg','2.jpg','3.jpg'];
$new = ['3.jpg','4.jpg'];

$rs = array_diff($old, $new);

print_r($rs);