import fetch from 'node-fetch'

function finalEmail(){
  let url='https://formal-email-template-api.herokuapp.com/templates/Product%20launch%20email';
  let str=fetch(url)
  .then(response => response.json())
  .then(data => document.getElementById("final").innerHTM=data);

}
// let data=fetch(url);
// console.log(data);





// console.log(template)

// let pattern = "\[(.*?)\]"
// let y = pattern.findall(pattern)

// for (let i = 0; i < y.length; i++) {
//   console.log(y[i])
// }