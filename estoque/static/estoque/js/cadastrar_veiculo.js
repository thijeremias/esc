//scrip utilizado nas páginas cadastrar_veiculo e entrada

$(document).ready(function(){
    $("form").submit(function(){
        if ($("#id_placa").val().length != 7){
            alert("A placa deve conter 7 dígitos.");
            return false;
        }else{
            return true;
        }
    });
})