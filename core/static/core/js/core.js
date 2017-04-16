$(function () {
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });

        setInterval(function () {
            $('.autoload').each(function () {
                $(this).load($(this).attr('data-url'))
            });
        }, 3000);


        $(".chosen-select").chosen();

        $.fm({debug: false})
    }
);

