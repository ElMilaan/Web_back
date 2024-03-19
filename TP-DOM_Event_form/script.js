// FORM

const phone = document.getElementById("phone");

function limitPhoneNumber() {
  phone.value = phone.value.replace(/[^\d]/g, "");
}

//EVENTS
