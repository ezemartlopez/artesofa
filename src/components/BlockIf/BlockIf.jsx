
function BlockIf({children, condition=false}) {
  return (condition? children: null);
}

export default BlockIf;