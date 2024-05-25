import Breadcrumb from "../Breadcrumb/Breadcrumb"

function TitlePage({titulo, links}) {
  return (
    <div className="my-2 bg-sky-600 w-full h-[150px] flex flex-col items-center justify-center gap-2">
        <span className="text-white text-6xl font-bold">{titulo}</span>
        <Breadcrumb links={links}/>
    </div>
  )
}

export default TitlePage