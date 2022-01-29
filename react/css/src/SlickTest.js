import React, { Component } from 'react';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "./SlickTest.css"


const SliderSlick = () => {
  const settings = {
    dots: true,
    infinite: true,
    autoplay: false,
    // className: "center",
    // centerMode: true,
    // centerPadding: "60px",
    // fade:true, //center랑 중복 불가능
    autoplaySeed: 100,
    speed: 500,
    slidesToShow: 2,
    slidesToScroll: 1
    
  };
  return(
    <div className="SliderSlick">
      <div>
          <h3>Best Beer</h3>
      </div>
      <div className="carousel">
        <Slider {...settings} className="fffff">
            <CustomSlick index={1} className="sdsd"></CustomSlick>
            <h1>sdf</h1>
            <CustomSlick index={1}></CustomSlick>
            <CustomSlick index={3}></CustomSlick>
            <CustomSlick index={5}></CustomSlick>
        </Slider>
      </div>
    </div>
  )
}

function CustomSlick(props) {
  const imgSrc = "img/2.png"
  return(
    <img src={imgSrc}/>
    // <div className="divSide" key={props.index} >
    //   <img src={imgSrc}/>
    // </div>
  )
}

export default SliderSlick;


