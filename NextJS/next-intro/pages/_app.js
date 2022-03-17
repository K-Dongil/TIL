import Layout from "../component/Layout";
// import NavBar from "../component/NavBar1";
import "../styles/globals.css"

export default function App({Component, pageProps}){
  const test = "Hello";
  return (
    <div>
      <Layout>
        <Component {...pageProps} />
        <span>Test</span>
      </Layout>
      {/* <style jsx global>
        {`
          a {
            color: green;
          }
        `}
      </style> */}
    </div>
  )
}