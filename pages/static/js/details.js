window.onload = () => {
    document.getElementById('finalPrice').innerHTML = writeComma(remainMoney())
}
const remainMoney = () => {
    let remainMoney = 0;
    for(let unusedMoney of document.getElementsByClassName('unusedMoney')) {
        remainMoney += Number(unusedMoney.innerHTML.replace(/\,/g, ''));
    }
    for(let usedMoney of document.getElementsByClassName('usedMoney')) {
        remainMoney -= Number(usedMoney.innerHTML.replace(/\-|,/g, ''));
    }
    return remainMoney;
}