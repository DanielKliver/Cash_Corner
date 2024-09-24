function showk(){
const input_sum = document.getElementById('input_sum')
const input_valut = document.getElementById('input_valut')

var res = 0;
if(input_sum !== null && input_sum.value!== null)
{
    res = input_sum.value*get_course_cript();
    console.log(get_course_cript())
}
else
{
    console.log('Element not found')
}
const get_sum = document.getElementById('input_get_sum')
if(!isNaN(res))
{
get_sum.value = res;
console.log(res)
}
}

