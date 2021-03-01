const queryString = window.location.search;
console.log(queryString);

const urlParams = new URLSearchParams(queryString);

const gender = urlParams.get('Gender');
const age = urlParams.get("Age");
const height = urlParams.get("Height");
const weight = urlParams.get("Weight");
const caffeine = urlParams.get("Caffeine (MG)");
const systolic = urlParams.get("Systolic");
const cholesterol = urlParams.get("Cholesterol");
const drinks = urlParams.get("Drinks");
const smoker = urlParams.get("Smoker");

function loaded() {
    document.getElementById("genderInput").innerHTML = gender;
    document.getElementById("ageInput").innerHTML = age;
    document.getElementById("heightInput").innerHTML = height;
    document.getElementById("weightInput").innerHTML = weight;
    document.getElementById("caffeineInput").innerHTML = caffeine;
    document.getElementById("systolicInput").innerHTML = systolic;
    document.getElementById("cholesterolInput").innerHTML = cholesterol;
    document.getElementById("drinksInput").innerHTML = drinks;
    document.getElementById("smokerInput").innerHTML = smoker;
}

console.log(gender);
console.log(age);
console.log(height);
console.log(weight);
console.log(caffeine);
console.log(systolic);
console.log(cholesterol);
console.log(drinks);
console.log(smoker);

params = [gender, age, height, weight, caffeine, systolic, cholesterol, drinks, smoker]

console.log(params)

// function pass_values() {
//                  $.ajax(
//                  {
//                      type:'POST',
//                      contentType:'application/json;charset-utf-08',
//                      dataType:'json',
//                      url:'http://127.0.0.1:5000/Results.html?Gender=' + gender + '&Age=' + age + '&Height=' + height + '&Weight=' + weight + '&Caffeine+%28MG%29=' + caffeine + '&Systolic=' + systolic + '&Cholesterol=' + cholesterol + '&Drinks=' + drinks + '&Smoker=' + smoker,
//                      success:function (data) {
//                          var reply=data.reply;
//                          if (reply=="success")
//                          {
//                              return url;
//                          }
//                          else
//                              {
//                              alert("some error ocured in session agent")
//                              }
 
//                      }
//                  }
//              );
//  }

// d3.json("/our-data-api", function (mydata) { 
//     data = mydata
//     console.log(data); 
// });