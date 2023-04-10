let url = window.location.href;
// http://127.0.0.1:5100/enterprise/home
let re = new RegExp('enterprise/(.*?)/|enterprise/(.*?)');
let className = url.match(re);

let currentPage = document.getElementById(className[1]);
currentPage.classList.add('current-select');