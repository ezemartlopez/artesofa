import Truck from "@assets/PaymentMethods/truck.svg";
import Dollar from "@assets/PaymentMethods/dollar.svg";
import CardCredit from "@assets/PaymentMethods/creditcard.svg";

function PaymentMethods() {
  return (
    <div className='w-full py-10 flex sm:flex-row sm:justify-around items-center flex-col gap-[20px]'>
        <div className="w-[280px] flex flex-col justify-start items-center">
            <img src={Truck} alt="truck" className='size-[100px]'/>
            <span className="text-[22px] font-rubik font-light">Hacemos envíos</span>
            <span className="text-sm font-rubik font-light">A todo el país, obvio.</span>
        </div>
        <div className="w-[280px] flex flex-col justify-start items-center">
            <img src={CardCredit} alt="truck" className='size-[100px]'/>
            <span className="text-[22px] font-rubik font-light">Pagá en cuotas</span>
            <span className="text-sm font-rubik font-light">6 sin interés</span>
        </div>
        <div className="w-[280px] flex flex-col justify-start items-center">
            <img src={Dollar} alt="truck" className='size-[100px]'/>
            <span className="text-[22px] font-rubik font-light">Tenemos mega-promos</span>
            <span className="text-sm font-rubik font-light">¡Descuentos en efectivo!</span>
        </div>
    </div>
  )
}

export default PaymentMethods