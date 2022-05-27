// import { useEffect, useState } from "react";
import Seo from "../component/Seo";
import Link from "next/link";
import { useRouter } from "next/router";

export default function Home({ results }) {
  // const [movies, setMovies] = useState([]);

  // useEffect(() => {
  //   (async () => {
  //     const { results } = await (await fetch(`/api/movies`)).json();
  //     setMovies(results);
  //   })();
  // }, []);

  const router = useRouter();
  // const onClick = (id, title) => {
  //   router.push(
  //     {
  //       pathname: `/movies/${id}`,
  //       query: {
  //         title,
  //       },
  //     },
  //     `/movies/${id}`
  //   );
  // };
  
  const onClick = (id, title) => {
    router.push(router.push(`/movies/${title}/${id}`));
  };

  return (
    <div className="container">

      <Seo title="Home" />
      
      
      {results?.map((movie) => (
        // <div className="movie" key={movie.id}>
        <div
          onClick={() => onClick(movie.id, movie.original_title)}
          className="movie"
          key={movie.id}
        >
          <img src={`https://image.tmdb.org/t/p/w500/${movie.poster_path}`} />
          {/* <h4>{movie.original_title}</h4> */}
          <h4>
            {/* <Link
              href={{
                pathname: `/movies/${movie.id}`,
                query: {
                  title: movie.original_title,
                },
              }}
              as={`/movies/${movie.id}`}
            > */}
            <Link href={`/movies/${movie.original_title}/${movie.id}`}>
              <a>{movie.original_title}</a>
            </Link>
          </h4>
        </div>
      ))}

      <style jsx>{`
        .container {
          display: grid;
          grid-template-columns: 1fr 1fr;
          padding: 20px;
          gap: 20px;
        }
        .movie img {
          max-width: 100%;
          border-radius: 12px;
          transition: transform 0.2s ease-in-out;
          box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
        }
        .movie:hover img {
          transform: scale(1.05) translateY(-10px);
        }
        .movie h4 {
          font-size: 18px;
          text-align: center;
        }
      `}</style>
    </div>
  )
}

export async function getServerSideProps() {
  const { results } = await (
    await (await fetch(`https://api.themoviedb.org/3/movie/popular?api_key=10923b261ba94d897ac6b81148314a3f`)).json()
  )
  return {
    props: {
      results,
    },
  };
}