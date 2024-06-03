
function Footer() {
  return (
    <div className="w-full">
        <div className="w-full pb-[20px] pt-[40px] flex justify-center items-center gap-[10px]">
          <div className="size-[50px] flex justify-center items-center">
            <a href="https://instagram.com/artesofasillones" target="_blank">
              <img src="https://img.icons8.com/?size=256&id=32292&format=png" alt="instagram" className="cursor-pointer size-[30px] hover:size-[36px]"/>
            </a>
          </div>
          <div className="size-[50px] flex justify-center items-center">
            <a href="https://www.facebook.com/artesofasillones" target="_blank">
              <img src="https://img.icons8.com/?size=256&id=87264&format=png" alt="facebook" className="cursor-pointer size-[32px] hover:size-[38px]"/>
            </a>
          </div>
          <div className="size-[50px] flex justify-center items-center">
            <a href="https://www.tiktok.com/@artesofasillones" target="_blank">
              <img src="https://img.icons8.com/?size=256&id=aKlZySb1lsX8&format=png" alt="tiktok" className="cursor-pointer size-[34px] hover:size-[40px]"/>
            </a>
          </div>
        </div>

        <div className="w-full py-[15px] flex justify-center gap-[30px]">
          <span className="font-rubik cursor-pointer hover:text-slate-500">Bases y condiciones</span>
          <span className="font-rubik cursor-pointer hover:text-slate-500">Envíos</span>
        </div>

        <div className="w-full py-[15px] xl:px-[400px] md:px-0 flex md:flex-row flex-col items-center md:gap-0 gap-4 justify-between">
          <span className="font-rubik text-xs">© Copyright Re-Arte-Sofa - 2024</span>
          <span className="font-rubik text-xs">Creado por Ezequiel M.L.</span>
          <span className="font-rubik text-xs">Todos los derechos reservados.</span>
        </div>
    </div>
  )
}

export default Footer;