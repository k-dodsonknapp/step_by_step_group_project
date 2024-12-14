import React, { useEffect, useState } from "react";
import "./Carousel.css";

export const CarouselItem = ({ children, width, carouselItem }) => {
  return (
    <div className="carousel-item" style={{ width: width }}>
      {children}
    </div>
  );
};

function Carousel({ children }) {
  const [activeIndex, seActiveIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      updateIndex(activeIndex + 1);
    }, 10000);
    return () => {
      if (interval) {
        clearInterval(interval);
      }
    };
  });

  const updateIndex = (newIndex) => {
    if (newIndex < 0) newIndex = React.Children.count(children) - 1;
    else if (newIndex >= React.Children.count(children)) {
      newIndex = 0;
    }

    seActiveIndex(newIndex);
  };

  return (
    <div className="carousel">
      <div
        className="inner"
        style={{ transform: `translateX(-${activeIndex * 100}%)` }}
      >
        {React.Children.map(children, (child, index) => {
          return React.cloneElement(child, { width: "100%" });
        })}
      </div>
    </div>
  );
}

export default Carousel;
