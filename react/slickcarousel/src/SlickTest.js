import React, { Component } from 'react';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "./SlickTest.css"


const SlickTest = () => {
  const settings = {
    dots: true,
    infinite: true,
    autoplay: true,
    // className: "center",
    // centerMode: true,
    // centerPadding: "60px",
    fade:true, //center랑 중복 불가능
    autoplaySpeed: 1000,
    speed: 1000,
    slidesToShow: 1,
    slidesToScroll: 1
    
  };
  return(
    <div className="SlickTest">
        <div>
            <h3>Best Beer</h3>
        </div>
        <div className="carousel">
          <Slider {...settings}>
              <CustomSlide index={1}></CustomSlide>
              <CustomSlide index={2}></CustomSlide>
              <CustomSlide index={3}></CustomSlide>
              <CustomSlide index={4}></CustomSlide>
          </Slider>
        </div>
    </div>
  )
}

function CustomSlide(props) {
  const imgSrc = "img/abc.png"
  return(
    <div {...props}>
      <img src={imgSrc}/>
    </div>
  )
}

export default SlickTest;


