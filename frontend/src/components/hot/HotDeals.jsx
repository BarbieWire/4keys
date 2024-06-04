import React, {useEffect, useState} from 'react';

import classes from './HotDeals.module.css';

import HotDealsCard from "./card/HotDealsCard";

import {itemsDisplayedOnOneSlide} from "./constants";


const HotDeals = ({title}) => {
    const [items, setItems] = useState([])
    const [pageCount, setPageCount] = useState(0)
    const [currentPage, setCurrentPage] = useState(1)

    useEffect(() => {
        const itemsPreload = []
        for (let i = 0; i < 14; i++) {
            const data = {
                "id": i,
                "name": "Sony Playstation 5  + DualSense wireless controller Cosmic Red",
                "category": "Gaming Consoles",
                "description": "The latest Sony PlayStation introduced in November 2020. Powered by an eight-core AMD Zen 2 CPU and custom AMD Radeon GPU, the PS5 is offered in two models: with and without a 4K Blu-ray drive. Supporting a 120Hz video refresh, the PS5 is considerably more powerful than the PS4 and PS4 Pro.",
                "brand": "Sony",
                "color": "Cosmic Red",
                "price": 900,
                "discount": 100,
                "stock": 0,
                "vendor_code": "g24i7621r87",
                "main_image": "http://localhost:8000/media/products/Screenshot_2022-12-07_182855-removebg_1.png"
            }
            itemsPreload.push(data)
        }

        setPageCount(Math.ceil(itemsPreload.length / itemsDisplayedOnOneSlide))
        setItems(itemsPreload)
    }, [])

    function createPagination() {
        const dots = []
        for (let i = 1; i < pageCount + 1; i++) {
            dots.push(
                <span
                    className={currentPage === i ? classes.active : null}
                    onClick={() => setCurrentPage(i)}
                >
                </span>
            )
        }
        return dots
    }

    return (
        <section className={classes.main_section}>
            <h2 className={classes.title}>{title}</h2>
            <div className={classes.cards_wrapper}>
                {
                    items.map((item, index) => {
                        return Math.ceil((index + 1) / itemsDisplayedOnOneSlide) === currentPage &&
                        <HotDealsCard dataObject={item} id={item.id}/>
                    })
                }
            </div>
            <div className={classes.pagination_wrapper}>
                {
                    /* dots here (pagination) */
                    createPagination()
                }
            </div>
        </section>
    );
};

export default HotDeals;