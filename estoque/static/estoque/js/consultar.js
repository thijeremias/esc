$(document).ready(function(){
    $(":button").click(function(){
        var campo = document.getElementById("id_descricao");
        var comp = "";
        if (campo.value === comp){
            campo.value = 0;
        }
    });
    
})