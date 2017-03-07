/**
 * Created by Administrator on 2017/3/6.
 */

//方式一：自执行
(function (jq) {
    jq.extend({
               'dalong1': function (arg) {
                   console.log(arg);
               }
            });

    function f1() {

    }
})(jQuery);

/*
方式二：闭包
a = function (jq) {


     $.extend({
               'dalong1': function (arg) {
                   console.log(arg);
               }
            });

    function f1() {

    }
$.a(jq);

}

a(jQuery);

*/
