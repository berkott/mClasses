function getCoinData(coinId) {
    fetch(`https://api.coinpaprika.com/v1/coins/${coinId}`)
        .then(response => {
            console.log(response.json());
        });
}

getCoinData("doge-dogecoin");
getCoin("doge-dogecoin");

// Asynchronous functions
async function getCoin(coinId) {
    // you can only use await inside async functions
    let response = await fetch(`https://api.coinpaprika.com/v1/coins/${coinId}`);
    let data = await response.json();
    console.log(data);
}
