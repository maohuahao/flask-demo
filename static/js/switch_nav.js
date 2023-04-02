let itemAll  = document.querySelectorAll('.item');

itemAll.forEach((item)=>{
    item.addEventListener('click', ()=>{
        itemAll.forEach((item)=>{
            item.classList.remove("current-select");
        })
        console.log(item);
         item.classList.add("current-select");
    })
})
