
const quadra_select = document.getElementById('quadra')
const esporte_select = document.getElementById('esporte')

quadra_select.addEventListener("change", async (e) => {
  removeOptions(esporte_select)

  let esportes_json = await fetch('/quadra/esporte/' + quadra_select.value)
    .then((resp) => resp.json())
    .catch((error) => {
      console.log(error)
      return {1: 'Erro: por favor recarregue a página'}
    });
  console.log(esportes_json)


  for (let i = 0; i <= esportes_json.length-1; i++){
    let opt = document.createElement('option');
    opt.value = esportes_json[i];
    opt.innerHTML = esportes_json[i];
    esporte_select.appendChild(opt);
  }
})

function removeOptions(selectElement) {
   let i, L = selectElement.options.length - 1;
   for(i = L; i >= 0; i--) {
      selectElement.remove(i);
   }
}

