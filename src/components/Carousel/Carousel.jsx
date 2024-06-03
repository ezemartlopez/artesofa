import { useState, useEffect } from "react"

export default function Carousel({
    slides,
    autoSlide = false,
    autoSlideInterval = 3000,
    cover = false
  }) {
  const [currentIndex, setCurrentIndex] = useState(0);

  const prevSlide = () => {
    if(slides.length > 1){
    const isFirstSlide = currentIndex === 0;
    const newIndex = isFirstSlide ? slides.length - 1 : currentIndex - 1;
    setCurrentIndex(newIndex);      
    }
  };

  const nextSlide = () => {
    //const isLastSlide = currentIndex === slides.length - 1;
    //const newIndex = isLastSlide ? 0 : currentIndex + 1;
    if(slides.length > 1){
      setCurrentIndex((currentIndex === slides.length - 1) ? 0 : currentIndex + 1);
    }
  };

  const goToSlide = (slideIndex) => {
    setCurrentIndex(slideIndex);
  };

  useEffect(() => {
    const slideInterval = autoSlide? setInterval(nextSlide, autoSlideInterval): null;
    
    return () => clearInterval(slideInterval);
  }, [currentIndex]);

  return (
    <div className='min-w-max h-full w-full relative group'>
      <div style={{ backgroundImage: `url(${slides[currentIndex]})`, backgroundColor:"#F7F2EF", backgroundSize: cover?"cover":"contain"}} className='w-full h-full rounded-2xl bg-center bg-no-repeat duration-500'></div>
      {/* Left Arrow */}
      <div className='hidden group-hover:block absolute top-[50%] -translate-x-0 translate-y-[-50%] left-5 text-2xl rounded-full p-2 bg-slate-500/50 text-white cursor-pointer'>
        <div onClick={prevSlide} size={30}>
          <svg className="size-4 stroke-2 text-white rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor"  d="M5 1 1 5l4 4"/>
          </svg> 
        </div>
      </div>
      {/* Right Arrow */}
      <div className='hidden group-hover:block absolute top-[50%] -translate-x-0 translate-y-[-50%] right-5 text-2xl rounded-full p-2 bg-slate-500/50 text-white cursor-pointer'>
        <div onClick={nextSlide} size={30}>
          <svg className="w-4 h-4 stroke-2 text-white rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" d="m1 9 4-4-4-4"/>
          </svg> 
        </div>
      </div>

      <div className='absolute z-10 flex bottom-2 w-full justify-center gap-4'>
        {slides.map((slide, slideIndex) => (
          <div key={slideIndex} onClick={() => goToSlide(slideIndex)} className='cursor-pointer size-6 '>
            <div className={`w-3 h-3 rounded-full mx-1 cursor-pointer ${slideIndex === currentIndex? "bg-gray-600" : "bg-gray-400"}`}></div>
          </div>
        ))}
      </div>
    </div>
  )
}