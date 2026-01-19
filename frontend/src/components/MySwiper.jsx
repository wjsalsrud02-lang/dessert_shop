import { Swiper, SwiperSlide } from "swiper/react";
import { Autoplay, Pagination } from "swiper/modules";

import "swiper/css";
import "swiper/css/pagination";
import "./MySwiper.css";

function MySwiper() {
  return (
    <section className="main-swiper">
      <Swiper
        modules={[Autoplay, Pagination]}
        autoplay={{ delay: 4000 }}
        loop={true}
        pagination={{ clickable: true }}
      >
        <SwiperSlide>
          <div
            className="slide"
            style={{ backgroundImage: "url(/images/banner1.jpg)" }}
          >
            <h2>CREAMYDAY’</h2>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div
            className="slide"
            style={{ backgroundImage: "url(/images/banner2.jpg)" }}
          >
            <h2>Sweet Dessert Time</h2>
          </div>
        </SwiperSlide>

        <SwiperSlide>
          <div
            className="slide"
            style={{ backgroundImage: "url(/images/banner3.jpg)" }}
          >
            <h2>Everyday is Creamy</h2>
          </div>
        </SwiperSlide>
      </Swiper>
    </section>
  );
}

export default MySwiper;
