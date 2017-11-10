window.onload = function () {
    document.getElementById("id_desconto").onchange = function(){valorVendaDesconto();};
    document.getElementById("id_acrescimo").onchange = function(){valorVendaAcrescimo();};
    
    $(document).on("click","#id_link",function(){
        var valor_atual = document.getElementById("id_valor");
        valor_atual.value = 0;
        var produtos = document.getElementsByName("produto_id");
        var qtds = document.getElementsByName("quantidade");
        for(var i = 0; i < produtos.length; i++){
            novaAjax(produtos[i].value,qtds[i].value);
        }
        adicionaForm();
         
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

function novaAjax(id,qtd) {
    $.ajax({
        type: 'GET',
        url: "/vendas/ajax/vendas/",
        async: true,
        cache: false,
        dataType : "json",
        data:{"id":id},
        success: function(jsonData){
            var dados = JSON.parse(jsonData);
            atribuiValor(dados[0].fields.valor,qtd);
            
        }
});
}

function atribuiValor(valor,qtd){
    var valor2 = document.getElementById("id_valor");
    var valor1 = Number(valor2.value) + (Number(valor)*qtd);
    valor2.value = valor1.toFixed(2);
}

function adicionaForm(){
    var form = $(".form-inline:first").clone();
    $("#id_add").append(form);
}