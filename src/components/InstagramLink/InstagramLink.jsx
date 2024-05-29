import Instagram from "@assets/InstagramLink/instagram.svg";

function InstagramLink() {
  return (
    <div className="font-rubik w-full h-[250px] flex flex-col justify-center items-center gap-4">
        <div className="w-full flex justify-center items-center hover:opacity-50 cursor-pointer">
            <div className="h-full flex items-end">
              <a href="https://instagram.com/artesofasillones" target="_blank">
                <object data={Instagram} type="image/svg+xml" className="sm:size-[45px] size-[25px] cursor-pointer"></object>
              </a>
            </div>
            <a href="https://instagram.com/artesofasillones" target="_blank">
              <h3 className="sm:text-[60px] sm:leading-[55px] text-[35px] leading-[30px] font-bold text-orange-500 opacity-90 flex items-center">artesofasillones</h3>
            </a>
        </div>
        <a href="https://instagram.com/artesofasillones" target="_blank" className="min-w-[100px] max-w-max h-[36px] px-[20px] rounded-full border border-orange-500 text-orange-500 text-[12px] hover:bg-orange-500 hover:text-white transition-colors duration-500 flex items-center">S E G U I N O S</a>
    </div>
  )
}

export default InstagramLink;