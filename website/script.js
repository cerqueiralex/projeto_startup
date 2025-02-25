function enviarCompra(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const dados = Object.fromEntries(formData);
    
    fetch("http://localhost:8000/compras", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        alert("Compra realizada com sucesso!");
        console.log(data);
    })
    .catch(error => {
        alert("Erro ao processar a compra.");
        console.error(error);
    });
}