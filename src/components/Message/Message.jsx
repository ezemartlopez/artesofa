import React from 'react'

function Message({text}) {
  return (
    <li className="w-full bg-green-500 text-white text-sm font-semibold rounded-lg py-2 px-4">{text}</li>
  );
}

export default Message;