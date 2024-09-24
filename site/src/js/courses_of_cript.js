function get_course_cript(){
const options = {method: 'GET'};

let response = fetch('https://api.mobula.io/api/1/market/data?asset=Bitcoin', options)
  .then(response => response.json())
  .then(response => {
    let bitcoinData = response.data.price;
    console.log(bitcoinData);
    return bitcoinData;
  })
  .catch(err => console.error(err));

  
}