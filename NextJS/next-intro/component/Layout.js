import NavBar from "./NavBar1";

export default function Layout({children}) {
  return (
    <>
      <NavBar />
      <div>{children}</div>
    </>
  )
}