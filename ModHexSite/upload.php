<?php
   // Edit upload location here
   $number_rand =  rand(0,700);
   $destination_path = getcwd()."/media".DIRECTORY_SEPARATOR.$number_rand;

   $result = 0;
   
   $target_path = $destination_path . basename( $_FILES['myfile']['name']);

   if(@move_uploaded_file($_FILES['myfile']['tmp_name'], $target_path)) {
      $result = 1;
   }
    echo exec('python3 ModHex.py '.DIRECTORY_SEPARATOR.$number_rand.$_FILES['myfile']['name']);
   sleep(0.5);

?>


<script language="javascript" type="text/javascript">window.top.window.stopUpload(<?php echo $result; ?>);</script>

<script language="javascript" type="text/javascript">

    var destination = String('<?php echo DIRECTORY_SEPARATOR.$number_rand.$_FILES['myfile']['name']; ?>');

    window.top.window.viewResult(destination);

</script>

