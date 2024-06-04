import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { SubmitHandler, useForm } from "react-hook-form";

import axios from 'axios';
import ServerError from '../../fetching/serverErrors';

import classes from './LoginForm.module.css'

import user from "../../assets/svg/user.svg";
import lock from "../../assets/svg/lock.svg";
import eye from "../../assets/svg/eye.svg"

import { FieldArray, Field, KeyType } from '../../common/interfaces/credentials.interface';

import { RegisterCredentials } from '../../fetching/authentication';

import { registerPostRequest } from '../../fetching/authentication';

const fieldsMap = [
    {
        type: "email",
        placeholder: "Email",
        name: "email",
        key: "fields_email",
        icon: user,
    },
    {
        type: "password",
        placeholder: "Password",
        name: "password",
        key: "fields_password",
        icon: lock,
    },
    {
        type: "password",
        placeholder: "Repeate your password",
        name: "repeat_password",
        key: "fields_repeat_password",
        icon: lock,
    }
] as FieldArray

type T = "password" | "email" | "repeat_password"


const RegistrationForm = () => {
    const [serverError, setServerError] = useState<ServerError | null>(null)
    const [success, setSuccess] = useState<boolean>(false)

    const [showPassword, setShowPassword] = useState<KeyType[]>([])

    const { register, handleSubmit, formState: { errors } } = useForm<RegisterCredentials>();

    const onSubmit: SubmitHandler<RegisterCredentials> = async (credentials) => {
        setServerError(null);
        setSuccess(false);
        try {
            const response = await registerPostRequest(credentials);
            setServerError(null);
            setSuccess(true);
        } catch (error) {
            if (axios.isAxiosError(error)) {
                setServerError(error.response?.data as ServerError);
            } else {
                console.error(error);
            }
        }
    };

    const appendField = (field: KeyType) => {
        setShowPassword(state => {
            return [...state, field]
        })
    }

    const removeField = (item: KeyType) => {
        const arr = [...showPassword].filter(i => i !== item)
        setShowPassword(arr)
    };

    const handleUnhide = (item: KeyType) => {
        const presence = showPassword.find(i => i === item)
        if (presence) removeField(item)
        else appendField(item)
    }

    const extractMessages = (response: ServerError): string | null => {
        const messages = Object.entries(response.detail)
        if (messages.length > 0)
            return `${messages[0][0]}: ${messages[0][1]}`
        return null;
    };


    return (
        <div className={classes.wrapper}>
            <form className={classes.align_fields} onSubmit={handleSubmit(onSubmit)}>
                <h2 className={classes.title}>Registration</h2>
                {
                    fieldsMap.map((item: Field) => {
                        return (

                            <div key={item.key} className={classes.entry_wrapper}>
                                <div className={classes.placeholder_wrapper}>
                                    <p className={classes.field_name}>{item.placeholder}</p>
                                </div>
                                <div className={errors[item.name as T] ? [classes.fields_wrapper, classes.err].join(' ') : classes.fields_wrapper}>
                                    <img src={item.icon} alt={"svg icon"} className={classes.icon} />
                                    <input
                                        type={item.type === 'password' && !showPassword.find(i => i === item.key) ? item.type : "text"}
                                        className={classes.input_field}
                                        placeholder={`Type your ${item.type}`}
                                        {...register(item.name as T, { required: true })}
                                    />
                                    {
                                        item.type === "password" &&
                                        <img src={eye} alt="eye" onClick={() => handleUnhide(item.key)} className={classes.eye} />
                                    }
                                </div>
                            </div>
                        )
                    })
                }
                <button className={classes.btn} type={"submit"}>
                    <span>Register</span>
                </button>
                {
                    serverError && <span className={classes.err}>
                        <b>{typeof serverError.detail === 'string' ? serverError.detail : extractMessages(serverError)}</b>
                    </span>
                }
                {
                    success && <span className={classes.err}>
                        <b>Account has been successfully created, please check your email for confirmation letter</b>
                    </span>
                }

                <div className={classes.singup_block}>
                    <h5>already have an account?</h5>
                    <Link to={'/auth/login'}>Login</Link>
                </div>
            </form>
        </div>
    );
};

export default RegistrationForm;