import React, {useState, useEffect} from 'react';

import classes from './Special.module.css'

import Sorting from "./sorting/Sorting";
import Card from "../card/Card";

import { ProductCard } from '../../common/interfaces/productCard.interface';

import { showPerClick, showAllCategoryName } from './constants';

interface ComponentProps {
    title: string,
    fetchCallback: (url: string) => Promise<any>,
}

const Special: React.FC<ComponentProps> = ({title, fetchCallback}) => {
    // global items pool after fetching, see useEffect
    const [productCards, setProductCards] = useState<ProductCard[]>([])
    // take a look at useEffect and comments
    const [categories, setCategories] = useState<string[]>([])
    // category that is currently being highlighted
    const [highlightedCategory, setHighlightedCategory] = useState<string>(showAllCategoryName)

    // show card per click
    const [showItemsAmount, setShowItemsAmount] = useState(showPerClick);

    useEffect(() => {
        //  loop over the fetching results, extracting only unique categories
        //  create a list of distinct categories... style: [name: str, name2: str, ...]
        const cats = ["All", "Headphones", "Smartphones", "Gaming Consoles", "Cables", "Data Storages", "Watches", "Speakers", "Tablets", "Air Diffusers"]
        setCategories(cats)


        // temp solution to fill items array
        const itemsPreload = []
        for (let i = 0; i < 12; i++) {
            const data = {
                "id": 1,
                "name": "lenovo legion 5 pro 16iah7h",
                "category": "Gaming Laptops",
                "description": "Metāla korpuss\r\nLenovo Legion 5 Pro 16IAH7H portatīvajam datoram ir izsmalcināts un praktisks metāla korpuss, kas ne vien pasargās Jūsu klēpjdatoru, bet arī piešķirs tam stilu un eleganci. Lai svarīgie faili būtu aizsargāti!",
                "brand": "Lenovo",
                "color": "Cosmic Red",
                "normal_price": "199.99",
                "price_after_discount": null,
                "stock": 0,
                "vendor_code": "hiphuqn01",
                "cover": {
                    "id": 1,
                    "picture": "http://localhost:8000/media/products/3_3-removebg-preview_1.png"
                }
            }
            itemsPreload.push(data)
        }

        setProductCards(itemsPreload)

    }, [])

    function handleButtonPressed() {
        if (showItemsAmount < productCards.length) {
            setShowItemsAmount(showItemsAmount + showPerClick)
        }
    }

    // function extractUniqueCategories(arr) {
    //     const cats = [showAllCategoryName]
    //     // will be used in useEffect above
    //     // will be soon
    // }

    return (
        <section className={classes.special_wrapper}>
            <h2 className={classes.title}>{title}</h2>
            <Sorting
                sortingCategories={categories}
                highlightedCategory={highlightedCategory}
                setHighlightedCategory={setHighlightedCategory}
                setDisplayAmount={setShowItemsAmount}
            />
            <div className={classes.cards_wrapper}>
                {
                    productCards.map((obj, index) => {
                        return index < showItemsAmount &&
                        (obj.category === highlightedCategory || highlightedCategory === showAllCategoryName)
                            ? <Card product={obj}/>
                            : null
                    })
                }
            </div>
            {
                showItemsAmount < productCards.length &&
                <button
                    className={classes.btn_expose_more}
                    onClick={handleButtonPressed}
                >
                    Show more
                </button>
            }
        </section>
    );
};

export default Special;