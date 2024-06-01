import Breadcrumb from "../Breadcrumb/Breadcrumb"

function TitlePage({titulo, links}) {
  return (
    <div className="my-2 bg-sky-600 w-full sm:h-[150px] h-[100px] rounded-md flex flex-col items-center justify-center sm:gap-6 gap-2">
        <span className="text-white sm:text-6xl text-4xl font-bold">{titulo}</span>
        <Breadcrumb links={links}/>
    </div>
  )
}

export default TitlePage