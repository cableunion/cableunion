/**
 * Created by MXW on 2015/9/19.
 */
(function(){
    var __login = {
        urls: {
            captcha_url: '/account/captcha.gif/'
        },
        init: function(){
            this.loginForm();
            $('#captcha').click(function(){
                __login.getCaptcha();
            })
        },
        getCaptcha: function(){
            //load 从服务器拉取数据
            $('#captcha').load(__login.urls.captcha_url + '?t=' + new Date().getTime(), {}, function(){
                $('#captcha').attr('src', '/static/img/captchas/captcha.gif' + '?t=' + new Date().getTime());
            });
        },
        loginForm: function(){
            $('#loginFormID').validationEngine({
                validationEventTriggers: "blur", //触发的事件
                inlineValidation: true, //是否及时验证
                promptPosition: "topRight", //提示所在位置, topLeft, topRight, bottomLeft,  centerRight, bottomRight
                showOneMessage: true,
                formErrorArrow: false
            })
        }
    };
    $(document).ready(function(){
        __login.init();
        __login.getCaptcha();
    })
})();
