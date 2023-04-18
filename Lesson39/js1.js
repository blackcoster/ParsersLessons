JQuery
Google Analytics
Ajax - для обновления без обновления
Selenium - для js

<script>
//1 1 2 3 5 8 13 21
function fibonacci(a,b){
var nextNum = a + b;
console.log(nextNum+' это следующее число');
if (nextNum)<100{
    fibonacci(b,nextNum);
}
}
fibonacci(1,1);
</script>

<script>
var fibonacci = function(){
var a = 1;
var b = 1;
return function(){
var temp = b
b = b + a;
a = temp;
return b;
}
}
</script>
