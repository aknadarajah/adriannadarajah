"use strict";

const phoneContainer = document.getElementById("phone");
const phoneNumber = docuement.getElementById("telephone-number");
phoneContainer.addEventListener("animationend", function () {
  setTimeout(() => {
    phoneNumber.style.display = "block";
  }, 5000);
});
