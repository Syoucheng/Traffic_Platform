<?php

$connect = new PDO('mysql:host=localhost;dbname=inspection','root','');

$data = array();
$query = "SELECT * FROM list ORDER BY title";
$statement = $connect->prepare($query);

$statement->execute();

$result = $statement->fetchAll();

foreach($result as $row)
{
    $data[] = array(
        'id'             =>  $row["id"],
        'title'          =>  $row["title"],
        'start'          =>  $row["start_event"],
        'end'            =>  $row["end_event"],
    );
}

echo json_encode($data);
?>