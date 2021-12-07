<?php
$temp=$_GET['value'];

if($temp=='t')
{
    $command = escapeshellcmd('python certi.py');
    $output = shell_exec($command);
    echo $output;
}

if($temp=='f')
{
    $status=unlink('data/data.xlsx');    
if($status){  
echo '<script>alert("File deleted successfully")</script>';
echo '<script type="text/javascript">
           window.location = "index"
      </script>';   
}else{  
echo "Sorry!";    
} 
}
?>