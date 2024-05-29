
function obtenerLinks(listaString){
    if(!listaString) return [];
    const nueva = listaString;
    const url = window.location.origin + "/";
    const resultado = []
    const urls = window.location.pathname.split("/");
    nueva.forEach(element => {
        const objeto = {text:element, url:null}
        if(element !== ">"){
            objeto.url = url + urls.shift();
        }
        resultado.push(objeto);
    });
    resultado[0].text = "Inicio";
    return resultado;
}
function Breadcrumb({links}) {
    const lista = obtenerLinks(links);
  return (
    <div className="flex gap-1 text-white text-sm">
        {
         lista.map(obj => (obj.url !== null? <a href={obj.url}>{obj.text}</a>:<span>{obj.text}</span>))
        }
    </div>
  )
}

export default Breadcrumb