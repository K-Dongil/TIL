import Layout from "../component/Layout";
import "../styles/globals.css"

export default function App({Component, pageProps}){
  const test = "Hello";
  return (
    <div>
      <Layout>
        <Component {...pageProps} />
        <div>Test</div>
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