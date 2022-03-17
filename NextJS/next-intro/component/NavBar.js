import Link from "next/link";
import { useRouter } from "next/router";
import customStyles from "./NavBar.module.css";

export default function NavBar(){
  const router = useRouter();
  return (
    <nav>
      <Link href="/">
        <a className={router.pathname === "/" ? customStyles.active : ""}>
          Home
        </a>
      </Link>
      <Link href="/about">
        <a className={router.pathname === "/about" ? customStyles.active : ""}>
          About
        </a>
      </Link>
      <Link href="/">
        <a className={`${customStyles.deco} ${router.pathname === "/" ? customStyles.active : ""}`}>
          Home
        </a>
      </Link>
      <Link href="/about">
        <a className={[customStyles.deco, router.pathname === "/about" ? customStyles.active : ""].join(" ")}>
          About
        </a>
      </Link>
    </nav>
  )
}