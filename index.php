<?php
   if(isset($_FILES['image'])){
      $errors= array();
      $file_name = $_FILES['image']['name'];
      $file_size =$_FILES['image']['size'];
      $file_tmp =$_FILES['image']['tmp_name'];
      $file_type=$_FILES['image']['type'];
      
      
      if($file_size > 2097152){
         $errors[]='File size must be excately 2 MB';
      }
      
      if(empty($errors)==true){
         move_uploaded_file($file_tmp,'data/'.$file_name);
         echo '<script>alert("File uploaded succesfully")</script>';
      }else{
         print_r($errors);
      }
   }
?>
<html>
<style> 
</style>
   <body>
<form enctype="multipart/form-data" method="POST" action="" style="text-align: -webkit-center; margin-top: 10%;">
<table border="1">
<tr >
<td colspan="2" align="center"><strong>Import Data</strong></td>
</tr>
<tr>
<td align="center">CSV File:</td><td><input type="file" name="image" ></td></tr>
<tr align="center">
<td></td>

<td align="center">
<a href="data/data.xlsx"><input type="button" value="File"></a>  
<input type="submit">
<a href="mail?value=f"><input type="button" value="Turncate"></a>
<a href="mail?value=t"><input type="button" value="Mail"></a> 
</td>

</tr>
</table>
</form>
   </body>
</html>