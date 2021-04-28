<?php
    $command = escapeshellcmd('python3 app.py');
    $output = shell_exec($command);
    echo $output;
?>