const queryString = window.location.search;
console.log(queryString);

const urlParams = new URLSearchParams(queryString);

const gender = urlParams.get('Gender');
const age = urlParams.get("Age");
const caffine = urlParams.get("Caffine");
const systolic = urlParams.get("Systolic");
const cholesterol = urlParams.get("Cholesterol");
const drinks = urlParams.get("Drinks");
const smoker = urlParams.get("Smoker");

function loaded() {
    document.getElementById("genderInput").innerHTML = gender;
    document.getElementById("ageInput").innerHTML = age;
    document.getElementById("caffineInput").innerHTML = caffine;
    document.getElementById("systolicInput").innerHTML = systolic;
    document.getElementById("cholesterolInput").innerHTML = cholesterol;
    document.getElementById("drinksInput").innerHTML = drinks;
    document.getElementById("smokerInput").innerHTML = smoker;
}

console.log(gender);
console.log(age);
console.log(caffine);
console.log(systolic);
console.log(cholesterol);
console.log(drinks);
console.log(smoker);