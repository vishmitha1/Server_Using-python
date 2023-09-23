<!-- <html>
<style>
body
{
  overflow: hidden;
  margin: 0px;
  padding: 0px;
  font-family: Arial, sans-serif;
  background: #c5bde1;
}
div
{
  color: #FF0000;  
}
#form
{
  color: #000;
  border: 0px solid #afafaf;
font-weight: bold;
  width: 30%;
  margin-left: 35%;
  margin-top: 120px;
  text-align: center;
  padding: 40px;
  padding-top: 20px;
  border-radius: 3px;
  box-shadow: 0px 0px 8px #777;
  background: rgba(255, 255, 255, 255);
}

input
{
  color: #777;
  font-weight: bold;
  width: 70%;
  padding: 10px;
  margin: 10px;
  border: 1px solid #afafaf;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.5);
  outline: none;
}

button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

</style>
<body>
<div id="form">
  <h3>Adding Two Numbers</h3>
  <div class= "text-success" style="text-align: center" id="error">
                    
                   </div>
  <form action="form2.php">
  <label for="numb1">Number 1:</label>
  <input type="text" name="numb1" id="numb1"  placeholder="First Number"/>
  <br>
  <label for="numb2">Number 2:</label>
  <input type="text" name="numb2" id="numb2"  placeholder="Second Number" />
  <br>
  <button name="submit" class="btn btn-primary" type="submit">Submit</button>
  <button type="reset" name="clear" class="btn btn-primary">Clear</button>
  </form>
  
</div>
    <script type="text/javascript" src="jquery-3.2.1.min.js"></script>
    <script>
     $(document).ready(function(){
         $("form").submit(function(){
         var numb1=$("#numb1").val();
         var numb2=$("#numb2").val();
         
         var pat=/^[0-9]+$/;//old nic
         
         
         if(numb1==""){
             $("#error").text("Enter a value");
             $("#numb1").focus();
             return false;
         }
          
          if(!numb1.match(pat)){
             $("#error").text("Enter a number");
             $("#numb1").focus();
             return false;
         }
          
         if(numb2==""){
             $("#error").text("Enter a value");
             $("#numb2").focus();
             return false;
         }
          if(!numb2.match(pat)){
             $("#error").text("Enter a number");
             $("#numb1").focus();
             return false;
         }
          
         });
     });
      </script>
      <script>
     function displayMsg(m){
         var r=confirm("Do You want to "+m);
         if(r){
             return true;
         }else{
             return false;
         }
     }
    </script> 
      
</body>
</html> -->

<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            overflow: hidden;
            margin: 0px;
            padding: 0px;
            font-family: Arial, sans-serif;
            background: #c5bde1;
        }

        div {
            color: #FF0000;
        }

        #form {
            color: #000;
            border: 0px solid #afafaf;
            font-weight: bold;
            width: 30%;
            margin-left: 35%;
            margin-top: 120px;
            text-align: center;
            padding: 40px;
            padding-top: 20px;
            border-radius: 3px;
            box-shadow: 0px 0px 8px #777;
            background: rgba(255, 255, 255, 255);
        }

        input {
            color: #777;
            font-weight: bold;
            width: 70%;
            padding: 10px;
            margin: 10px;
            border: 1px solid #afafaf;
            border-radius: 3px;
            background: rgba(255, 255, 255, 0.5);
            outline: none;
        }

        button {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <div id="form">
        <h3>Adding Two Numbers</h3>
        <div class="text-success" style="text-align: center" id="error">
            <!-- PHP code here -->
            <?php
            if (isset($_REQUEST['msg'])) {
                echo $_REQUEST['msg'];
            }
            ?>
        </div>
        <form action="form2.php" method="post">
            <label for="numb1">Number 1:</label>
            <input type="text" name="numb1" id="numb1" placeholder="First Number" />
            <br>
            <label for="numb2">Number 2:</label>
            <input type="text" name="numb2" id="numb2" placeholder="Second Number" />
            <br>
            <button name="submit" class="btn btn-primary" type="submit">Submit</button>
            <button type="reset" name="clear" class="btn btn-primary">Clear</button>
        </form>
    </div>

    <script type="text/javascript" src="jquery-3.2.1.min.js"></script>
    <script>
        $(document).ready(function () {
            $("form").submit(function () {
                var numb1 = $("#numb1").val();
                var numb2 = $("#numb2").val();

                var pat = /^[0-9]+$/; // Regular expression to match numbers

                if (numb1 == "") {
                    $("#error").text("Enter a value");
                    $("#numb1").focus();
                    return false;
                }

                if (!numb1.match(pat)) {
                    $("#error").text("Enter a number");
                    $("#numb1").focus();
                    return false;
                }

                if (numb2 == "") {
                    $("#error").text("Enter a value");
                    $("#numb2").focus();
                    return false;
                }

                if (!numb2.match(pat)) {
                    $("#error").text("Enter a number");
                    $("#numb2").focus();
                    return false;
                }
            });
        });
    </script>
    <script>
        function displayMsg(m) {
            var r = confirm("Do You want to " + m);
            if (r) {
                return true;
            } else {
                return false;
            }
        }
    </script>
</body>

</html>