import Carousel from '../Carousel/Carousel';

function Slider() {
  const imagesSlides = [
    "https://dcdn.mitiendanube.com/stores/001/271/935/themes/idea/2-slide-1709682828687-6698020994-e27c9bd23cb3024be78d729e4c1e23471709682833-1920-1920.webp?692639951",
    "https://dcdn.mitiendanube.com/stores/001/271/935/themes/idea/2-slide-1709682828687-1881908734-1b09b983cb2d2ba77e16d0a628f37b3a1709682835-1920-1920.webp?692639951",
    "https://dcdn.mitiendanube.com/stores/001/271/935/themes/idea/2-slide-1709682828687-5407203596-b2ae56d5827102084dd032f3da6401421709682834-1920-1920.webp?692639951"
  ]

  return (
    <div className="py-[10px]">
      <div className="w-full h-[400px] xl:h-windvisible md:h-[700px] sm:h-[600px]">
        <Carousel slides={imagesSlides} autoSlide={true}/>
      </div>
    </div> 
  )
}

export default Slider;