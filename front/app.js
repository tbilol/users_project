let list = document.querySelector(".list")

fetch("data.json")
  .then(function(response) {
    return response.json();
  })
  .then(function(data) { 
    let l = data[0];
    

    function rander(arr, parent) {
      Object.entries(arr).forEach(([key,value]) => {
        parent.innerHTML += `
                <li class="item">
                    <img class="item__img" src="./asses/victor.jpg" alt="">
                    <div class="item__info">
                        <h2 class="item__name">User name: ${value.name}</h1>
                        <p class="item__email">User email: <span>${value.email}</span></p>
                        <p class="item__pass">User password: ${value.password}</p>
                    </div>
                </li>
             `
      })
    }
    rander(l,list)
  })
  .catch((error) => {
    console.error("Xatolik:", error);
  });