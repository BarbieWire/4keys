import React, { useEffect, useState } from 'react';
import { Link } from "react-router-dom";

import classes from './Navbar.module.css'

import Ibag from '../../assets/svg/bag.svg'
import Ichevron from '../../assets/svg/chevron-down.svg'
import Ilogin from '../../assets/svg/log-in.svg'
import Iclose from '../../assets/svg/close.svg'

import Ilogout from '../../assets/svg/log-out.svg'
import Icredit from '../../assets/svg/credit-card.svg'
import Ibox from '../../assets/svg/box.svg'
import Iarchieve from '../../assets/svg/archive.svg'

import { useAppDispatch, useAppSelector } from '../../redux/hooks';
import { updateSearchingPrompt, darkenBackground } from '../../redux/slices/appearanceSlice';

import CategoryMenu from "./menu/CategoryMenu";

import { logoutPostRequest } from '../../fetching/authentication';
import { Categories } from '../../common/interfaces/categories.interface';
import { logout } from '../../redux/slices/userSlice';


const Navbar = () => {
    const [categoryMenuDisclosed, setCategoryMenuDisclosing] = useState<boolean>(false)
    const [profileDisclosed, setProfileDisclosed] = useState<boolean>(false)
    const [sideMenuDisclosed, setSideMenuDisclosed] = useState<boolean>(false)

    const searchPrompt = useAppSelector(state => state.websiteAppearance.searchPrompt)
    const userStatus = useAppSelector(state => state.users)
    const tintedBackground = useAppSelector(state => state.websiteAppearance.backgroundTinted)

    const dispatch = useAppDispatch()

    useEffect(() => {
        !tintedBackground && setCategoryMenuDisclosing(false)
    }, [tintedBackground])

    const categories: Categories = [
        {
            category: "Accessories",
            children: [
                {
                    category: "Tommy Hilfiger",
                    children: [
                        {
                            category: "shoes",
                        },
                        {
                            category: "clothes",
                        },
                        {
                            category: "hats",
                        },
                        {
                            category: "boots",
                        },
                        {
                            category: "jeans",
                        },
                    ]
                },
                {
                    category: "Moncler"
                },
                {
                    category: "Supreme"
                },
                {
                    category: "RipnDip",
                    children: [
                        {
                            category: "boots",
                        },
                        {
                            category: "jeans",
                        },
                    ]
                },
                {
                    category: "Posty and Co"
                },
                {
                    category: "Canada goose"
                },
                {
                    category: "H&M"
                },
                {
                    category: "Adidas",
                    children: [
                        {
                            category: "shoes",
                        },
                        {
                            category: "clothes",
                        },
                        {
                            category: "hats",
                        },
                        {
                            category: "boots",
                        },
                        {
                            category: "jeans",
                        },
                    ]
                },
                {
                    category: "Nike"
                },
                {
                    category: "Puma"
                },
            ]
        },
        {
            category: "Accessories",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Bags, Wallets and Luggage",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Face",
            children: [
                {
                    category: "Tommy Hilfiger",
                    children: [
                        {
                            category: "shoes",
                        },
                        {
                            category: "clothes",
                        },
                        {
                            category: "hats",
                        },
                        {
                            category: "boots",
                        },
                        {
                            category: "jeans",
                        },
                    ]
                },
                {
                    category: "Moncler"
                },
                {
                    category: "Supreme"
                },
                {
                    category: "RipnDip",
                    children: [
                        {
                            category: "boots",
                        },
                        {
                            category: "jeans",
                        },
                    ]
                },
                {
                    category: "Posty and Co"
                },
                {
                    category: "Canada goose"
                },
                {
                    category: "H&M"
                },
                {
                    category: "Adidas",
                    children: [
                        {
                            category: "shoes",
                        },
                        {
                            category: "clothes",
                        },
                        {
                            category: "hats",
                        },
                        {
                            category: "boots",
                        },
                        {
                            category: "jeans",
                        },
                    ]
                },
                {
                    category: "Nike"
                },
                {
                    category: "Puma"
                },
            ]
        },
        {
            category: "Books",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Accessories",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Clothing",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Motorbike",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Shoes",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Check Trousers",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Check Trousers",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Clothing",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        },
        {
            category: "Handbag",
            children: [
                {
                    category: "Lorem Ipsum 2"
                }
            ]
        }
    ]

    const handleProfile = () => {
        setProfileDisclosed(!profileDisclosed)
    }

    const handleCategoryMenu = () => {
        setCategoryMenuDisclosing(!categoryMenuDisclosed)
        dispatch(darkenBackground(true))
    }

    const handleLogout = async () => {
        try {
            await logoutPostRequest()
            dispatch(logout())
        } catch (error) { }
    }

    return (
        <>
            <header className={classes.nav_container}>
                <nav className={classes.nav_wrapper}>
                    <div className={classes.left}>

                        <label className={classes.menuButtonContainer} htmlFor="menu-toggle" onClick={() => { setSideMenuDisclosed(true) }}>
                            <div className={classes.menuButton}></div>
                        </label>

                        <Link to={"/"} className={classes.logo} tabIndex={1}>4Keys</Link>
                        <div className={sideMenuDisclosed ? [classes.btn_wrapper, classes.active].join(" ") : classes.btn_wrapper}>
                            <img src={Iclose} alt="close" onClick={() => setSideMenuDisclosed(false)} className={classes.close} />

                            <button
                                className={[classes.btn, classes.btn_flex].join(' ')}
                                onClick={handleCategoryMenu}
                                tabIndex={2}
                            >
                                Categories
                                <img src={Ichevron} alt="chevron down" className={classes.chevron} />
                            </button>
                            <Link to={"/about"} className={classes.btn} tabIndex={3}>About</Link>
                            <Link to={"/delivery"} className={classes.btn} tabIndex={4}>Delivery</Link>
                            <Link to={"/services"} className={classes.btn} tabIndex={5}>Services</Link>
                        </div>
                    </div>
                    <div className={classes.right}>
                        <div className={classes.input_field_wrapper}>
                            <input
                                type="text"
                                onChange={e => dispatch(updateSearchingPrompt(e.target.value))}
                                value={searchPrompt}
                                placeholder={"Search"}
                                className={classes.search_bar}
                                tabIndex={6}
                            />
                            <button className={[classes.btn, classes.search_btn].join(' ')} tabIndex={7}></button>
                        </div>
                        <a className={classes.bag} href={'/cart'} tabIndex={8}>
                            <img src={Ibag} alt="shopping bag" />
                        </a>
                        {
                            userStatus.authenticated && <button
                                className={classes.profile_button}
                                onClick={handleProfile}
                                tabIndex={9}
                            >
                                {userStatus.currentUser.email.slice(0, 1)}
                            </button>
                        }
                        {
                            !userStatus.authenticated && <Link
                                to={"/auth/login"}
                                className={classes.profile_button}
                                tabIndex={9}
                            >
                                <img src={Ilogin} alt="login icon" />
                            </Link>
                        }
                        {
                            (userStatus.authenticated && profileDisclosed) &&
                            <div className={classes.profile_menu}>
                                <ul>
                                    <div className={classes.greetings}>
                                        Welcome, <span>{userStatus.currentUser.email}</span>
                                    </div>
                                    <br />
                                    <li tabIndex={10}>
                                        <Link to={"/wishlist"}>
                                            My Wishlist
                                            <img src={Ibox} alt="wishlist icon" />
                                        </Link>

                                    </li>
                                    <li tabIndex={11}>
                                        <Link to={"/promocodes"}>
                                            My Promocodes
                                            <img src={Icredit} alt="promocodes icon" />
                                        </Link>

                                    </li>
                                    <li tabIndex={12}>
                                        <Link to={"/history"}>
                                            Order History
                                            <img src={Iarchieve} alt="history icon" />
                                        </Link>
                                    </li>
                                    <hr className={classes.separator} />
                                    <li tabIndex={13} onClick={handleLogout}>
                                        Logout
                                        <img src={Ilogout} alt="history icon" />
                                    </li>
                                </ul>
                            </div>
                        }
                    </div>
                </nav>
            </header>
            {
                categoryMenuDisclosed && <CategoryMenu categories={categories} />
            }
        </>
    );
};

export default Navbar;