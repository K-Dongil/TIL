import NavBar from "./NavBar1";

export default function Layout({children}) {
  return (
    <>
      <NavBar></NavBar>
      <div>{children}</div>
    </>
  )
}