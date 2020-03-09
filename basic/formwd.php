<?php

   $con = mysqli_connect('127.0.0.1','root','');
   
   if(!$con)
   {
	   echo 'not connnected to server';
	   
   }
   
   if(!mysqli_select_db($con,'it'))
   {
	   echo 'Database Not Selected';
   }
   
   $FirstName = $_POST['fn'];
   $LastName = $_POST['ln'];
   $Gender = $_POST['Gender'];
   $Email = $_POST['email'];
   $DOB = $_POST['DOB'];
   
   $sql = "INSERT INTO c (FirstName,LastName,Gender,email,DOB) VALUES('$FirstName','$LastName',$Gender,'$Email','$DOB')";
   if(!mysqli_query($con,$sql))
   {
	   echo 'Not Inserted';
   }
   else
   {
	   echo 'Inserted';
   }
   
   header("refresh:2; url = formwd.html");

?>
