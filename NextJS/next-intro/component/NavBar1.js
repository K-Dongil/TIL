// styled JSX
import Link from "next/link";
import { useRouter } from "next/router";

export default function NavBar(){
  const router = useRouter();
  return (
    <nav>
      <Link href="/">
        <a className={router.pathname === "/" ? "active" : "not_active"}>
          Home
        </a>
      </Link>
      <Link href="/about">
        <a className={router.pathname === "/about" ? "active" : "not_active"}>
          About
        </a>
      </Link>
      <style jsx>
        {`
          nav {
            backgound-color:tomato;
          }
          a {
            text-decoration: none;
          }
          .active {
            color: blue;
          }
          .not_active{
            color: red;
          }
        `}
      </style>
    </nav>
  )
}