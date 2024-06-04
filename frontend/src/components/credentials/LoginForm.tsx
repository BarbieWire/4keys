import React, { useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

import classes from './LoginForm.module.css'

import { SubmitHandler, useForm } from "react-hook-form";

import ServerError from '../../fetching/serverErrors';
import { FieldArray, Field } from '../../common/interfaces/credentials.interface';

import user from '../../assets/svg/user.svg';
import lock from '../../assets/svg/lock.svg';
import stars from '../../assets/video/stars.mp4'

import { loginPostRequest, retrieveUser } from '../../fetching/authentication';
import { useAppDispatch } from '../../redux/hooks';
import { login } from '../../redux/slices/userSlice';


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
    }
] as FieldArray


type T = "password" | "email"
interface Inputs {
    password: string,
    email: string,
}

const LoginForm = () => {
    const [serverError, setServerError] = useState<ServerError | null>(null)
    const { register, handleSubmit, formState: { errors } } = useForm<Inputs>();

    const dispatch = useAppDispatch();
    const navigate = useNavigate();

    const onSubmit: SubmitHandler<Inputs> = async (data) => {
        try {
            await loginPostRequest(data)
            const response = await retrieveUser()
            dispatch(login(response))
            navigate(`/`, { replace: true });
            
        } catch (error) {
            if (axios.isAxiosError(error)) {
                setServerError(error.response?.data as ServerError)
            } else {
                console.error(error);
            }
        }
    }

   
    console.log(serverError?.detail)

    return (
        <div className={classes.wrapper}>
            <form className={classes.align_fields} onSubmit={handleSubmit(onSubmit)}>
                <h2 className={classes.title}>Login</h2>
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
                                        type={item.type}
                                        className={classes.input_field}
                                        placeholder={`Type your ${item.name}`}
                                        {...register(item.name as T, { required: true })}
                                    />
                                </div>
                            </div>
                        )
                    })
                }
                <Link to={"/auth/forgot"} className={classes.forgot}>Forgot your password?</Link>
                <button className={classes.btn} type={"submit"}>
                    <span>Proceed</span>
                    <video autoPlay loop muted playsInline className={classes.buttonVideo}>
                        <source src={stars} type="video/mp4" />
                        Your browser does not support the video tag.
                    </video>
                </button>
                {
                    serverError && <span className={classes.err}>
                        Login failed: <b>{typeof serverError.detail === 'string' && serverError.detail}</b>
                    </span>
                }

                <div className={classes.singup_block}>
                    <h5>Still don't have an account?</h5>
                    <Link to={'/auth/registration'}>Sing up</Link>
                </div>
            </form>
        </div>
    );
};

export default LoginForm;