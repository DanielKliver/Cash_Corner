async function showk(){
  
const input_sum = document.getElementById('input_sum');
const input_valut = document.getElementById('input_valut');
const output_sum = document.getElementById('output_sum');
const output_valut = document.getElementById('output_valut');  

var res = 0;
if(input_sum !== null && input_sum.value!== null)
{
    let course_one = await get_course_cript(input_valut.value);

    let course_two = await get_course_cript(output_valut.value);

    if(input_valut.value == 'Rub')
    {
        res = fx(input_sum.value).from("RUB").to("USD");
        res = res/course_two;
        console.log(res);
        if(output_valut.value=='Rub')
        {
            res = input_sum.value;
        }
        
    }
    if(output_valut.value == 'Rub')
    {
        if(input_valut.value =='Rub')
            {
                res = input_sum.value;
            }
            else{
        res = input_sum.value*course_one;
        res = fx(res).from("USD").to("RUB");
        console.log(res);
            }
        
    }
    else if(input_valut.value!='Rub' && output_valut.value!='Rub')
    {
    res = ((input_sum.value*course_one)/course_two);
    res = res.toFixed(8);
    }
    
}
else
{
    console.log('Element not found')
}
if(!isNaN(res))
{
output_sum.value = res;

}
}

