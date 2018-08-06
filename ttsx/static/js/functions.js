function subgoods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/ttsx/subgoods/',
        type: 'POST',
        data: {'goods_id': id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success:function(data) {
            if (data.count >= 1) {
                $('.num_show_' + id).val(data.count)
                $('#price' + id).html(data.goods_price)
            }else {
                alert('不买拉倒')
            }
            console.log(data);
        },
        error:function (data) {
            alert('请求失败')
        }
    })
}


function addgoods(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/ttsx/addgoods/',
        type: 'POST',
        data: {'goods_id': id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success:function (data) {
            if (data.code == '200') {
                console.log(data)
                $('.num_show_' + id).val(data.count)
                $('#price' + id).html(data.goods_price)
            }
        },
        error:function (data) {
            alert('请求失败')
        }
    })
}


$.get('/ttsx/goodsnum/', function (data) {
    if (data.code == '200'){
        console.log(data);
        for (var i=0; i<data.carts.length; i += 1){
            $('.num_show_'+ data.carts[i].goods_id).val(data.carts[i].count)
        }
    }
});


// 计算商品总价
function tatal_price() {
    $.get('/ttsx/tatalprice/', function (data) {
        console.log(data);
        if (data.code == '200'){
            console.log(data)
        }
    })
}
tatal_price();
