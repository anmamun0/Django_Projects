const allProduct = (cat) => {
    document.getElementById('all_items').innerHTML = 'loading...'

    fetch('https://fakestoreapi.com/products')
        .then((res) => res.json())
        .then((data) => displayAllData(data,cat)) 
}

const displayAllData = (data,cat) => {
  
    const all_items = document.getElementById('all_items'); 
    document.getElementById('all_items').innerHTML = ''

    let i = 0;
   
    data.forEach(element =>
    {  
        if (cat.length==0 ||  cat == element.category)
        {
            all_items.innerHTML +=
                `
                <div class="max-w-sm rounded overflow-hidden shadow-lg bg-white m-2 text-xs m-auto">
                
                <img class="h-44 m-auto p-10"
                    src="${element.image}" alt="Random Image" >
                <div class="px-6 py-4">
                    <div class="font-bold text-md mb-2">${element.title.substring(0,20)}</div>

                    <p class="text-gray-700  "> ${element.description.substring(0,30)}<br> 
                    </p>
                    <p class="text-gray-700  "> ${element.category} 
                    </p>
                </div>
                <div class="px-6  pb-2"> <span
                        class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                    Prie: ${element.price}$ </span>
                    
                </div>
                `; 
        }
    });
    // const d = document.createElement('div')
    // d.classList.add('chack1')
    // d.innerHTML = `
    //     <p>Its chack1 class name </p>
    // `  
    // all_items.appendChild(d)

    // clone = d.cloneNode(d)
    // all_items.insertBefore(clone,all_items.firstChild)
}

allProduct('')

const allCategory = () => {
    fetch('https://fakestoreapi.com/products/categories')
            .then(res=>res.json())
            .then(data=>displayCategory(data))
}
const displayCategory = (data) => {
    console.log(data)
    const allCategory = document.getElementById('allCategory')
    allCategory.innerHTML = ''; // Clear existing content 
    
    data.forEach(category => {
        allCategory.innerHTML += `
        <span class="inline-block bg-gray-200 hover:bg-gray-300 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2 cursor-pointer" onclick="allProduct('${category}')" >
        ${category}
        </span>`;
    });
}

allCategory();














const practice = () => {
    const  items = document.getElementById('anParent');
    items.firstElementChild.innerHTML = "<p>I find you</p>"
    items.lastElementChild.innerHTM = "<p>I also find you</p>"

    document.getElementById('hide-button').addEventListener('click', () => {
        document.getElementById('hide-button').parentElement.style.display = 'none'
    })

    const btn = document.getElementById('hide-button')
    const parent = btn.parentElement


    const par = document.getElementById('parent')
    par.insertAdjacentHTML('beforeend', '<div>Inserted before the element</div>');
    
}
// practice();

const practice2 = () => {
    const form = document.getElementById('myForm').addEventListener('submit', (event) => {
        event.preventDefault()

        const form = document.getElementById('myForm');

        const name = form.querySelector("input[type='text']").value
        const email = form.querySelector("input[type='email']").value 
 
        console.log(email)
    })
 
}
   
// practice2()



// category
// : 
// "men's clothing"
// description
// : 
// "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
// id
// : 
// 1
// image
// : 
// "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
// price
// : 
// 109.95
// rating
// : 
// {rate: 3.9, count: 120}
// title
// : 
// "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"