import React, { useRef, useEffect } from "react";

import { Swiper, SwiperSlide } from 'swiper/react';
import { Pagination, Autoplay, Navigation } from 'swiper/modules';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/pagination';

import './Slider.css'

import chevron_right from '../../assets/svg/chevron-right.svg'
import chevron_left from '../../assets/svg/chevron-left.svg'


import image from '../../assets/png/slide.png'


const Slider = () => {
    const swiperRef = useRef<HTMLDivElement | null>(null)

    useEffect(() => {
        const current = swiperRef.current
        if (current) current.style.setProperty("--slides-count", "4")  // 4 is simply number of slides
    }, [swiperRef])

    return (
        <div className={'slider_wrapper'} ref={swiperRef}>
            <Swiper
                modules={[Pagination, Autoplay, Navigation]}
                slidesPerView={1}
                autoplay={{
                    delay: 7000,
                    disableOnInteraction: false,
                    pauseOnMouseEnter: true,
                }}
                pagination={{ clickable: true }}
                navigation={{
                    nextEl: '.review-swiper-button-next',
                    prevEl: '.review-swiper-button-prev',
                }}
            >
                {/* Left Button */}
                <button className={'slider-button review-swiper-button-prev'}>
                    <img src={chevron_left} alt="" />
                </button>

                <SwiperSlide>
                    <img src={image} alt="slide" className={'slide'} />
                </SwiperSlide>
                <SwiperSlide>
                    <img src={image} alt="slide" className={'slide'} />
                </SwiperSlide>
                <SwiperSlide>
                    <img src={image} alt="slide" className={'slide'} />
                </SwiperSlide>
                <SwiperSlide>
                    <img src={image} alt="slide" className={'slide'} />
                </SwiperSlide>

                {/* Right Button */}
                <button className={'slider-button review-swiper-button-next'}>
                    <img src={chevron_right} alt="" />
                </button>
            </Swiper>
        </div>
    );
};


export default Slider;