$(function () {
    initActionListeners();
});

function initActionListeners() {

    $('#star').on('click', function (ev) {
        ev.preventDefault();
        var button = ev.target;

        // Send AJAX
        $.ajax({
            url: "/apartment/"+this.getAttribute('data-id')+"/star/",
            type:'POST',
            data: {},
            success(data) {
                if (data.status == 'success') {
                    // Animate
                    if (!$(button).hasClass('starred')) {
                        $(button).html('<i class="fa fa-star"></i>&nbsp;取消收藏');
                        $(button).attr('count', Math.abs($(button).attr('count')) + 1);
                    } else {
                        $(button).html('<i class="fa fa-star-o"></i>&nbsp;收藏');
                        $(button).attr('count', Math.abs($(button).attr('count')) - 1);
                    }
                    $(button).toggleClass('starred');
                }
            },
            error(er) {
                swal("Error!", er.responseText, "error");
            }
        });
    });

}

