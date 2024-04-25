import BlockIf from "@components/BlockIf/BlockIf";
  
function Modal({children, condition, show, closeModal}) {
  
  return (
    <BlockIf condition={condition}>
      <div className="fixed top-0 w-screen h-screen z-30">
        <div className=" w-full h-full relative " aria-labelledby="modal-title" role="dialog" aria-modal="true">
          <div className="absolute w-full h-full bg-gray-500 opacity-75" onClick={closeModal}></div>
          <div className="w-full h-full flex">
            <div className="h-full flex-grow sm:w-auto w-0"></div>
            <div className={"transition-transform duration-300 transform ease-linear " + (show? "": "translate-x-full")}>
              {children}
            </div>
          </div>
        </div>
      </div>
    </BlockIf>
  );
}

export default Modal;
