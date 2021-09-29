<?/*
	$host="localhost";
	$username="root";
	$password="";
	$dbname="stddb";
	$link=mysqli_connect($host,$username,$password)or die("ไม่สามารถติดต่อกับฐานข้อมูลได้ในขณะนี้");
	mysql_select_db($dbname,$link)or die("ไม่สามารถติดต่อกับฐานข้อมูลได้ในขณะนี้");
	echo("ติดต่อสำเร็จ");
?>
<?php

/*$servername = "localhost";

$username = "root";

$password = "14121999";

$db = "dbhospital_queue";



// Create connection

$conn = mysqli_connect($servername, $username, $password,$db);



// Check connection

if (!$conn) {

   die("การเชื่อมต่อล้มเหลว: " . mysqli_connect_error());

}

//echo "เชื่อมต่อสำเร็จแล้ว";*/

?>   


<?php

$conn= mysqli_connect("localhost","root","","kingiceman_db") or die("Error: " . mysqli_error($conn));
mysqli_query($conn, "SET NAMES 'utf8' ");
error_reporting( error_reporting() & ~E_NOTICE );
date_default_timezone_set('Asia/Bangkok');

if (!$conn) {

   die("การเชื่อมต่อล้มเหลว: " . mysqli_connect_error());

}
  echo "เชื่อมต่อสำเร็จแล้ว";
?>

