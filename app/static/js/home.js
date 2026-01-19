const form = document.querySelector('form')
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const data = new FormData(event.target);
    const jsonObject = Object.fromEntries(data.entries());
    const jsonString = JSON.stringify(jsonObject, null, 2);
    
    console.log(jsonString);
});