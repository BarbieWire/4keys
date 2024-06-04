import App from './App';
import React from 'react';
import ReactDOM from 'react-dom/client';

import './index.css'

import { Provider } from "react-redux";
import { store } from "./redux/store";

// npm install react-router-dom
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";

// // layouts
import MainLayout from "./layouts/MainLayout";
import AuthLayout from "./layouts/AuthLayout";

// imported pages
import HomePage from "./pages/HomePage";
import CartPage from "./pages/CartPage";

// Debug and etc.
import DebugPage from "./pages/Debug/DebugPage";

// pages
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegistrationPage";
import VerifyEmailConfirm from './pages/VerifyEmailConfirm/VerifyEmailConfirm';



// create a page constructor
// to add a new route simply create a new obj with properties path and element.
const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {
                path: "/",
                element: <MainLayout />,
                children: [
                    {
                        path: "/",
                        element: <HomePage />,
                    },
                    {
                        path: "/cart",
                        element: <CartPage />
                    },
                    {
                        path: "/testing",
                        element: <DebugPage />
                    }
                ]
            },

            {
                path: "/auth",
                element: <AuthLayout />,
                children: [
                    {
                        path: "/auth/login",
                        element: <LoginPage />
                    },
                    {
                        path: "/auth/registration",
                        element: <RegisterPage />
                    }
                ],
            },

            {
                path: "/api",
                element: <AuthLayout />,
                children: [
                    {
                        path: "/api/auth/verify-email-confirm/:uidb64/:token",
                        element: <VerifyEmailConfirm />
                    },
                ]
            }
        ]
    }
]);


const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <Provider store={store}>
        <RouterProvider router={router} />
    </Provider>
);
