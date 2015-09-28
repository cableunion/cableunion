/**
 * Created by MXW on 2015/9/19.
 */

(function(global){
    var __register = {
        username: $('#ajaxUsername'),
        email: $('#ajaxEmail'),

        init: function(){
            $.ajaxSetup({cache:false});
//            var ajaxCheck = function(){};
//            ajaxCheck.prototype = {
//                setFlag: function(){
//                    //
//                },
//                check: function(){
//
//                }
//            };
            __register.username.blur(function(){
                if ($.trim(__register.username.val()) == '' && __register.username.val().length < 5) {
                    return false;
                }
                if (__register.username.val().length > 25) {
                    __register.username.validationEngine('showPrompt', '用户名太长了，不能超过25个字符!', '', 'topRight', true);
                    return false;
                } else {
                    __register.username.validationEngine('hideAll');
                }

                $.get('/account/register-check-handle/', {flag: 'username', username: __register.username.val().trim()}, function(result){
                    if (result.status == -1) {
                        __register.username.validationEngine('showPrompt', '该用户名已经存在!', '', 'topRight', true);
                    } else {
                        __register.username.validationEngine('hideAll');
                    }
                }, 'json')
            });

            __register.email.blur(function(){
                var regex = /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i;
                if ($.trim(__register.email.val()) == '' && !regex.test(__register.email.val())) {
                    return false;
                }

                $.get('/account/register-check-handle/', {flag: 'email', email: __register.email.val().trim()}, function(result){
                    if (result.status == -1) {
                        __register.email.validationEngine('showPrompt', '该邮箱已经注册!', '', 'topRight', true);
                    } else {
                        __register.email.validationEngine('hideAll');
                    }
                }, 'json')
            });



        }

    };

    $(document).ready(function(){
        $('#formID').validationEngine({
            validationEventTriggers: "blur", //触发的事件
            inlineValidation: true, //是否及时验证
//            success: false, //为true时即使有不符合的也提交表单,false表示只有全部通过验证了才能提交表单,默认false
            promptPosition: "topRight", //提示所在位置, topLeft, topRight, bottomLeft,  centerRight, bottomRight
            showOneMessage: true,
            ajaxFormValidation: false, //不用ajax请求，用表单跳转
            ajaxFormValidationMethod: 'POST',
            onBeforeAjaxFormValidation: function(form, options){
                /**
                 * 没有效果  思路留着
                 * */
                var $loc_province = $('#loc_province'), loc_province_text = $loc_province.find('option[value=' + $loc_province.val() + ']').text(),
                    $loc_city = $('#loc_city'), loc_city_text = $loc_city.find('option[value=' + $loc_city.val() +']').text(),
                    $loc_town = $('#loc_town'), $loc_town_text = $loc_town.find('option[value=' + $loc_town.val() + ']').text();

                $loc_province.val(loc_province_text);
                $loc_city.val(loc_city_text);
                $loc_town.val($loc_town_text);
            },
            onAjaxFormComplete: function(status, form, json, options){
                console.log(status);
                alert('注册成功！')
            },
            failure: function(){
                alert('error!')
            },
            success: function(){
                alert('注册成功！')
            }
        });

        __register.init();
    });
})(window);