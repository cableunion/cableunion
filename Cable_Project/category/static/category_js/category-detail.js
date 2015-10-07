/**
 * Created by MXW on 2015/10/5.
 */

(function(){
    var category_detail = {
        init: function(){
            $('#horizontalTab').easyResponsiveTabs({
                type: 'default', //Types: default, vertical, accordion
                width: 'auto', //auto or any width like 600px
                fit: true   // 100% fit in a container
            });

            $('#products').slides({
                preload: true,
                preloadImage: 'img/loading.gif',
                effect: 'slide, fade',
                crossfade: true,
                slideSpeed: 350,
                fadeSpeed: 500,
                generateNextPrev: true,
                generatePagination: false
            });
        }
    };

    $(document).ready(function(){
        category_detail.init();
    })
})();
