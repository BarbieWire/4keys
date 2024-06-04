import React from 'react';

// components
import Slider from "../components/slider/Slider";
import Explore from "../components/explore/Explore";
import Special from "../components/special/Special";
import HotDeals from "../components/hot/HotDeals";

import { popularGetRequest, recentlyAddedGetRequest } from '../fetching/products';

const HomePage = () => {
    return (
        <div className="container">
            <Slider/>
            <Explore/>

            <Special title={"Popular"} fetchCallback={popularGetRequest}/>
            {/* <HotDeals title={"Hot Deals"}/> */}
            {/* <Special title={"New Added"} fetchCallback={recentlyAddedGetRequest}/> */}
           
        </div>
    );
};

export default HomePage;