import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import axios from 'axios';

import classes from './VerifyEmailConfirm.module.css'

import { verifyEmailConfirm, EmailVerifiedResponse } from '../../fetching/authentication';
import ServerError from '../../fetching/serverErrors';

import { useNavigate } from 'react-router-dom';

import Isuccess from '../../assets/svg/check-square.svg'
import IFailed from '../../assets/svg/x-square.svg'


type verifyEmailCredentials = {
    uidb64: string,
    token: string,
}


const VerifyEmailConfirm = () => {
    const [serverError, setServerError] = useState<ServerError | null>(null)
    const [emailVerified, setEmailVerified] = useState<EmailVerifiedResponse>()
    const [timer, setTimer] = useState<number>(3)

    const { uidb64, token } = useParams<verifyEmailCredentials>()

    const navigate = useNavigate();

    const activateEmail = async () => {
        if (uidb64 && token) { // Add a type guard
            try {
                const response = await verifyEmailConfirm(uidb64, token);
                setEmailVerified(response)

            } catch (error) {
                if (axios.isAxiosError(error)) {
                    setServerError(error.response?.data as ServerError)
                }
            }
        } else {
            // Handle the case when uidb64 or token is undefined
            console.error("Missing UID or token.");
        }
    }

    useEffect(() => {
        activateEmail()
    }, [])

    useEffect(() => {
        let timerId: NodeJS.Timeout;

        if (emailVerified && emailVerified.status_code === 200) {
            timerId = setInterval(() => {
                setTimer(prevTimer => {
                    if (prevTimer <= 1) {
                        clearInterval(timerId);
                        navigate('/auth/login');
                    }
                    return prevTimer - 1;
                });
            }, 1000);
        }

        return () => clearInterval(timerId); // Clean up the interval on component unmount
    }, [emailVerified, navigate]);

    return (
        <div className={classes.alignBox}>
            {
                (serverError && typeof serverError.detail === "string") &&
                <div className={classes.messageWrapper}>
                    <img src={IFailed} alt="failed"/>
                    <h2>Unable to verify your email address: {serverError.detail}</h2>
                </div>
            }
            {
                (emailVerified && emailVerified?.status_code === 200) &&
                <div className={classes.messageWrapper}>
                    <img src={Isuccess} alt="success"/>
                    <h2 className={classes.success}>Your email has been successfully verified, redirect to login page in {timer} seconds...</h2>
                </div>
            }
        </div>
    );
};

export default VerifyEmailConfirm;