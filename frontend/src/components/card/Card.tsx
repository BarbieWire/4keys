import React from 'react';
import { Link } from "react-router-dom";

import { ProductCard } from '../../common/interfaces/productCard.interface';

import classes from './Card.module.css';

import bag from '../../assets/svg/bag.svg';

interface Picture {
    id: number;
    picture: string;
}

interface ComponentProps {
    product: ProductCard
}

const Card: React.FC<ComponentProps> = ({ product }) => {
    function handleAddToCart() {

    }

    function handleBuyImmediately() {

    }

    return (
        <div className={classes.card_wrapper}>
            <Link className={classes.card} to={`products/${product.vendor_code}/`}>
                {
                    product.cover && product.cover.picture
                        ? <img src={product.cover.picture} alt={product.name} />
                        : <p>No cover available</p>
                }

                <p className={classes.product_name}>{product.name}</p>

                <div className={classes.secondary_data_container}>
                    <span className={classes.brand_name}>{product.brand}</span>
                    <span
                        className={product.price_after_discount ? [classes.price_tag, classes.discount].join(" ") : classes.price_tag}
                    >
                        {product.normal_price}$
                    </span>
                    {
                        product.price_after_discount &&
                        <span className={classes.price_tag}>
                            {product.price_after_discount}$
                        </span>
                    }
                </div>
            </Link>

            <div className={classes.hover_bar}>
                <button
                    className={[classes.btn, classes.buy_btn].join(" ")}
                    onClick={handleBuyImmediately}
                >
                    Buy {product.price_after_discount ? product.price_after_discount : product.normal_price}$
                </button>
                <button
                    className={[classes.btn, classes.cart_btn].join(" ")}
                    onClick={handleAddToCart}
                >
                    <img src={bag} alt="bag" />
                </button>
            </div>
        </div>
    );
};

export default Card;