import React from 'react';
import classes from './Explore.module.css'

import new_img from '../../assets/png/Screenshot-2021-05-13-at-14.44 1.png'
import popular_img from '../../assets/png/Apple-iPhone-14-Pro-iPhone-14-Pro-Max-hero-220907.jpg 1.png'

import fire from '../../assets/svg/fire.svg'
import lightning from '../../assets/svg/lightning.svg'


const Explore = () => {
    return (
        <div className={classes.explore_wrapper}>
            <div className={classes.element}>
                <img src={new_img} alt="new"/>
                <div className={classes.overflow}></div>
                <div className={classes.marker_wrapper}>
                    <object data={lightning}>New</object>
                    <p>New</p>
                </div>
            </div>
            <div className={classes.element}>
                <img src={popular_img} alt=""/>
                <div className={classes.overflow}></div>
                <div className={classes.marker_wrapper}>
                    <object data={fire}>Popular</object>
                    <p>Popular</p>
                </div>
            </div>
        </div>
    );
};

export default Explore;