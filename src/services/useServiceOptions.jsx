const apiUrl = import.meta.env.VITE_API_URL;

function useServiceOptions() {

    const url = apiUrl + '/products_search';
    const obtenerDatos = async (setter) =>{
        try {
            const response = await fetch(url);
            if (!response.ok) {
            throw new Error(response.statusText);
            }
            const datos = await response.json();
            console.log(datos);
            setter(datos);

        } 
        catch (error) {
            console.error(error);
            setter([]);
        }        
    }
    return {handleOptions: obtenerDatos};

}

export default useServiceOptions;
