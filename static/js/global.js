var modal = document.getElementById("detailModal");
var span = document.getElementsByClassName("close")[0]

const showModal = async (args) => {
    const response = await fetch(`adjective/detail/${args}`);
    const data = await response.json()
    console.log(data)
}

