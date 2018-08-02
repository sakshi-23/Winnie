$(function(){

    setInterval(function(){
        $.get( "/get-orders", function( data ) {
        data=JSON.parse(data)
            if (data.value!=""){
                 $( "#five" ).removeClass("hidden")
                 $("#five .card-chart").attr("data-background-color","red")
                 $("table").prepend("<tr class='newOrder'><td>"+data.value+"</td></tr>")
            }
        });
    }, 2000);


    $("table").on("click","tr",function(){

        $(this ).addClass("progress").removeClass("newOrder")
        if (!$(".newOrder").html()){
            $("#five .card-chart").attr("data-background-color","orange")

        }

    })



});