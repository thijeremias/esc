window.onload = function () {
    document.getElementById("id_desconto").onchange = function(){valorVendaDesconto();};
    document.getElementById("id_acrescimo").onchange = function(){valorVendaAcrescimo();};
    $("#id_venda_produto").change(function(){
        var array = $(this).val();
        var valor = document.getElementById("id_valor");
        valor.value = 0.0;
        for(var i = 0; i < array.length; i++){
            novaAjax(array[i]);
        }
    });

};

function valorVendaDesconto () {
    
    var desconto = document.getElementById("id_desconto");
    var valor = document.getElementById("id_valor");
    valor.value = Number(valor.value) - Number(desconto.value);
    
}

function valorVendaAcrescimo () {
    
    var acrescimo = document.getElementById("id_acrescimo");
    var valor = document.getElementById("id_valor");
    valor.value = Number(valor.value) + Number(acrescimo.value);
    
}
function novaAjax(id) {
    $.ajax({
        type: 'GET',
        url: "/vendas/ajax/vendas/",
        async: true,
        cache: false,
        dataType : "json",
        data:{"id":id},
        success: function(jsonData){
            var dados = JSON.parse(jsonData);
            atribuiValor(dados[0].fields.valor);
            
        }
});
}

function atribuiValor(valor){
    var valor2 = document.getElementById("id_valor");
    var valor1 = Number(valor2.value) + Number(valor);
    valor2.value = valor1.toFixed(2);
}