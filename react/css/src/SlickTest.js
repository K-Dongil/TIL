import React, { Component } from 'react';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

// class CustomSlide extends Component {
//   render() {
//     const { index, ...props } = this.props;
//     return (
//       <div {...props}>
//         <h3>{index}</h3>
//       </div>
//     );
//   }
// }

// export default class SimpleSlider extends Component {
//   render() {
//     const settings = {
//       dots: true,
//       infinite: true,
//       speed: 500,
//       slidesToShow: 1,
//       slidesToScroll: 1
//     };
//     return (
//       <div>
//         <h2>Custom Slides</h2>
//         <Slider {...settings}>
//           <CustomSlide index={1} />
//           <CustomSlide index={2} />
//           <CustomSlide index={3} />
//           <CustomSlide index={4} />
//           <CustomSlide index={5} />
//           <CustomSlide index={6} />
//         </Slider>
//       </div>
//     );
//   }
// }




const SliderSlick = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1
  };
  return(
    <div className="SliderSlick">
      <div>
          <h3>Best Beer</h3>
      </div>
      <Slider {...settings}>
      
          <div>
          <CustomSlick index={"1"}>ddd</CustomSlick>
          </div>
          <div>
            <h3>3</h3>
          </div>
          <div>
            <h3>4</h3>
          </div>
          <div>
            <h3>5</h3>
          </div>
          <div>
            <h3>6</h3>
          </div>
      </Slider>
    </div>
  )
}

function CustomSlick(props) {
  return(
    <div key={props.index}>dddd</div>
  )
}

export default SliderSlick;