const allUser = () => {
    
    fetch('https://fakestoreapi.com/users')
        .then((res) => res.json())
        .then((data) => allUserDisplay(data));
}
const allUserDisplay = (data) => {
    row = document.getElementById('user-table-row');
    console.log(data);

    data.forEach(user => {
        row.innerHTML += `
         <tr>
            <td class="py-2 px-4 border-b">${user.id}</td>
            <td class="py-2 px-4 border-b">${user.username}</td>
            <td class="py-2 px-4 border-b">${user.address.city}</td>
            <td class="py-2 px-4 border-b">${user.email}</td>

            <td class="py-2 px-4 border-b">
                <div class="flex gap-4 justify-end text-xs text-white">
                    <a class="bg-blue-500 px-2 py-2 rounded-lg  cursor-pointer">
                    View </a>
                    <a class="bg-blue-500 px-2 py-2 rounded-lg   cursor-pointer">
                    Login </a>
                </div>
            </td>

        </tr> 
    `
    });
    
}
allUser()







 


// var swiper = new Swiper('.swiper', {
//     slidesPerView: 3,
//     direction: getDirection(),
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//     },
//     on: {
//       resize: function () {
//         swiper.changeDirection(getDirection());
//       },
//     },
//   });

//   function getDirection() {
//     var windowWidth = window.innerWidth;
//     var direction = window.innerWidth <= 760 ? 'vertical' : 'horizontal';

//     return direction;
//   }