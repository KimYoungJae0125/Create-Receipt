const writeComma = (money) => {
    if(money instanceof String == false) {
        money = String(money)
    }
    return money.replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}