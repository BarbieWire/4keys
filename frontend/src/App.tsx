import React, { useEffect } from 'react';
import './index.css'
import axios from 'axios';

import { Outlet } from 'react-router-dom';

import { useAppSelector, useAppDispatch } from './redux/hooks'
import { login } from './redux/slices/userSlice'
import { darkenBackground } from './redux/slices/appearanceSlice';

import { retrieveUser } from './fetching/authentication';

import ServerError from './fetching/serverErrors';


function App() {
    const dispatch = useAppDispatch()

    const tintedBackground = useAppSelector(state => state.websiteAppearance.backgroundTinted)

    const authRequest = async () => {
        try {
            const response = await retrieveUser()
            if (response.is_active) dispatch(login(response))

        } catch (error) {
            if (axios.isAxiosError(error)) {
                error.response?.data as ServerError
            }
        }
    }

    useEffect(() => {authRequest()}, [])

    return (
        <div className="App">
            {
                tintedBackground &&
                <div
                    className={'tintedOverlay'}
                    onClick={() => dispatch(darkenBackground(false))}>
                        {/* dark tinted overlay with the max z-index */}
                </div>
            }
            <Outlet />
        </div>
    );
}

export default App;
