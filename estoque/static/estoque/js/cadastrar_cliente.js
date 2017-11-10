$(document).ready(function(){
    $("form").submit(function(){
        if ($("#id_cpf").val().length != 11){
            alert("O CPF deve conter 11 dígitos");
            return false;
        }else{
            return true;
        }
    });
})