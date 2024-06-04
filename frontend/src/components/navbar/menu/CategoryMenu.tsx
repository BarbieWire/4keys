import React, { useState } from 'react';
import classes from "./Category.module.css";

import { Link } from "react-router-dom";

import { Categories, CategoryEntry } from '../../../common/interfaces/categories.interface';


const CategoryMenu = (props: { categories: Categories }) => {
    const { categories } = props
    const [highlightedCategory, setHighlightedCategory] = useState(0)

    function handleMouseOver(elemIndex: number) {
        setHighlightedCategory(elemIndex)
    }

    const current: CategoryEntry = categories[highlightedCategory]

    return (
        <div className={classes.category_menu_wrapper}>
            <div className={classes.category_menu}>
                <ul>
                    {
                        categories.map((item, index) => {
                            return (
                                <li
                                    onMouseOver={() => handleMouseOver(index)}
                                    className={index === highlightedCategory ? classes.active : undefined}
                                >
                                    {item.category}
                                </li>
                            )
                        })
                    }
                </ul>
            </div>
            <div className={classes.sub_category_menu}>
                <div className={classes.sub_category_content}>
                    {
                        current.children && current.children.map((secondLevelCategories, index1) => {
                            return (
                                <div className={classes.sub_section} id={`${index1}`}>
                                    <Link to={''}>
                                        <span>{secondLevelCategories.category}</span>
                                    </Link>
                                    {
                                        secondLevelCategories.children &&
                                        secondLevelCategories.children.map((subItem, index2) => {
                                            return <Link to={''} id={`${index2}`}>{subItem.category}</Link>
                                        })
                                    }
                                </div>
                            )
                        })
                    }

                </div>
            </div>
        </div>
    );
};

export default CategoryMenu;