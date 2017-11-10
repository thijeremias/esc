window.onload = function () {
        $("form").submit(function(){
            return validaConfigurar();
       });
};

function validaConfigurar() {
    if ($("#id_valor_hora").val() != 0){
        var config = $("#id_valor_hora").val();
        var moto = $("#id_valor_hora_moto").val();
        alert("Configuração realizada com sucesso!\nValor para carros R$ "+config
        +"\nValor para motos R$ "+moto);
        return true;
        
    }else {
        alert("Por favor digite um valor para a hora");
        return false;
    }
    
    
}