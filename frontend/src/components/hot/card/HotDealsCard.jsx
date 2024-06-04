import React from 'react';

import {Link} from "react-router-dom";

import classes from './HotDealsCard.module.css'


const HotDealsCard = ({dataObject}) => {
    return (

        <Link className={classes.card} to={`products/${dataObject.vendor_code}/`}>
            <img src={dataObject.main_image} alt="main" className={classes.main_image}/>
            <div className={classes.data_wrapper}>
                <span className={classes.product_name}>{dataObject.name}</span>
                <div className={classes.secondary_data_container}>
                    <span className={classes.brand_name}>{dataObject.brand}</span>
                    <span
                        className={dataObject.discount ? [classes.price_tag, classes.discount].join(" ") : classes.price_tag}
                    >
                    {dataObject.price}$
                    </span>
                    {
                        dataObject.discount &&
                        <span className={classes.price_tag}>
                        {dataObject.price - dataObject.discount}$
                    </span>
                    }
                </div>
            </div>
        </Link>
    );
};

export default HotDealsCard;