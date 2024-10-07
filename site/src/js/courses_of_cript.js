async function get_course_cript(valut){

    console.log(valut)
    if(valut == 'bitcoin')
    {
const options = {method: 'GET'};
let coinData = 0;
let response = await fetch('https://api.mobula.io/api/1/market/data?asset=bitcoin', options)
  .then(async response =>await response.json())
  .then(response => {
    coinData = response.data.price;
    console.log(coinData);
  })
  .catch(err => console.error(err));
  return coinData;
}

if(valut == 'litecoin')
    {
const options = {method: 'GET'};
let coinData = 0;
let response = await fetch('https://api.mobula.io/api/1/market/data?asset=litecoin', options)
  .then(async response =>await response.json())
  .then(response => {
    coinData = response.data.price;
    console.log(coinData);
  })
  .catch(err => console.error(err));
  return coinData;

}

if(valut == 'ethereum')
    {
const options = {method: 'GET'};
let coinData = 0;
let response = await fetch('https://api.mobula.io/api/1/market/data?asset=ethereum', options)
  .then(async response =>await response.json())
  .then(response => {
    coinData = response.data.price;
    console.log(coinData);
  })
  .catch(err => console.error(err));
  return coinData;

}



if(valut == 'tether')
    {
const options = {method: 'GET'};
let coinData = 0;
let response = await fetch('https://api.mobula.io/api/1/market/data?asset=tether', options)
  .then(async response =>await response.json())
  .then(response => {
    coinData = response.data.price;
    console.log(coinData);
  })
  .catch(err => console.error(err));
  return coinData;

}



}





