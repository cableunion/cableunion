/**
 * Created by MXW on 2015/10/15.
 */

(function(){
    $(document).ready(function() {
        $('#reviseForm').validationEngine({
            validationEventTriggers: "blur", //触发的事件
            inlineValidation: true, //是否及时验证
            promptPosition: "topRight", //提示所在位置, topLeft, topRight, bottomLeft,  centerRight, bottomRight
            showOneMessage: true
        });
    })
})();
