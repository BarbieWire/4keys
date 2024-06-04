import React, {useEffect} from 'react';

import { useAppSelector } from '../redux/hooks';

import {Outlet} from "react-router-dom";
import {useNavigate} from "react-router-dom";


const AuthLayout = () => {
    const isAuthenticated = useAppSelector(state => state.users.authenticated)
    const navigate = useNavigate();
    
    useEffect(() => {
        if (isAuthenticated) navigate("/");
    }, [isAuthenticated, navigate])

    return (
        <Outlet/>
    );
};

export default AuthLayout;