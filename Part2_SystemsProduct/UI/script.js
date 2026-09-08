const rates = {
    USD: 1.00,
    INR: 95.53,
    EUR: 0.86,
    GBP: 0.74,
    JPY: 159.32,
    AUD: 1.39,
    CAD: 1.39,
    SGD: 1.27
};

const amountInput = document.getElementById("amount");
const fromCurrency = document.getElementById("fromCurrency");
const toCurrency = document.getElementById("toCurrency");

const convertButton = document.getElementById("convertButton");
const swapButton = document.getElementById("swapButton");

const resultText = document.getElementById("resultText");
const errorMessage = document.getElementById("errorMessage");


convertButton.addEventListener("click", convertCurrency);


function convertCurrency() {

    errorMessage.textContent = "";

    const amount = parseFloat(amountInput.value);

    if (isNaN(amount)) {
        errorMessage.textContent = "Please enter a valid amount.";
        return;
    }

    if (amount <= 0) {
        errorMessage.textContent = "Amount must be greater than zero.";
        return;
    }

    const from = fromCurrency.value;
    const to = toCurrency.value;

    const fromRate = rates[from];
    const toRate = rates[to];

    const amountInUSD = amount / fromRate;
    const convertedAmount = amountInUSD * toRate;

    resultText.textContent =
        `${amount.toFixed(2)} ${from} = ${convertedAmount.toFixed(2)} ${to}`;
}


swapButton.addEventListener("click", function () {

    const oldFrom = fromCurrency.value;

    fromCurrency.value = toCurrency.value;
    toCurrency.value = oldFrom;

    if (amountInput.value) {
        convertCurrency();
    }
});
