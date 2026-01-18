let list = document.querySelector(".list")

fetch("data.json")
  .then(function(response) {
    return response.json();
  })
  .then(function(data) { 
    let l = data[0];

    function rander(arr, parent) {
      for (let i = 0; i <= Object.keys(arr).length; i++) {
        let key = `user${i+1}`;
        parent.innerHTML += `
                <li class="item">
                    <img class="item__img" src="./asses/victor.jpg" alt="">
                    <div class="item__info">
                        <h2 class="item__name">User name: ${arr[key].name}</h1>
                        <p class="item__email">User email: <span>${arr[key].email}</span></p>
                        <p class="item__pass">User password: ${arr[key].password}</p>
                    </div>
                </li>
             `
      }
    }
    rander(l,list)
  })
  .catch((error) => {
    console.error("Xatolik:", error);
  });