/**
 * Created by Administrator on 2017/3/7.
 */

(function (jq) {
    jq.extend({
        valid:function (form) {
            jq(form).find(':submit').click(function () {
                jq(form).find('.item span').remove();
                var flag = true;
                jq(form).find(':text,:password').each(function () {

                    var require = $(this).attr('require');
                    if(require){
                        var val = $(this).val();
                        if(val.length<=0){
                            var label = $(this).attr('label');
                            var tag = document.createElement('span');
                            tag.innerText = label + "不能为空";
                            $(this).after(tag);
                            flag = false;
                            return false;
                        }

                        var minLen = $(this).attr('min-len');
                        if(minLen){
                            var minLenInt = parseInt(minLen);
                            if(val.length<minLenInt){
                                var label = $(this).attr('label');
                                var tag = document.createElement('span');
                                tag.innerText = label + "最小长度为" + minLen;
                                $(this).after(tag);
                                flag = false;
                                return false;


                            }
                        }
                        var phone = $(this).attr('phone');
                        if(phone){
                            //用户输入内容是否是手机格式
                            var phoneReg = /^1[3|5|8]\d{9}$/;
                            if(!phoneReg.test(val)){
                                var label = $(this).attr('label');
                                var tag = document.createElement('span');
                                tag.innerText = label + "格式错误";
                                $(this).after(tag);
                                flag = false;
                                return false;

                            }

                        }

                    }

                     //每一个元素执行次 匿名函数
                    /*
                    var val = $(this).val();
                    if(val.length<=0){
                        var label = $(this).attr('label');
                        var tag = document.createElement('span');
                        tag.innerText = label + "不能为空";
                        $(this).after(tag);
                        flag = false;
                        return false;
                }
                */
                });

                return false;
            });
        }
    });
})(jQuery)
