// http://localhost:3000/movies/:id

import { useRouter } from "next/router";
import Seo from "../../component/Seo";

export default function Detail({ params }) {
  const router = useRouter();
  console.log(router);

  // const [title, id] = router.query.params || [];

  const [title, id] = params || [];
  return (
    <div>
      <Seo title={title} />
      {/* <h4>{router.query.title || "Loading..."}</h4> */}
      <h4>{title}</h4>
    </div>
  );
}

export function getServerSideProps({ params: { params } }) {
  return {
    props: {
      params
    },
  };
}