import ApiService from "./axiosConfig";
import { User } from "../redux/slices/userSlice";

export interface LoginCredentials {
    email: string,
    password: string,
}

export interface RegisterCredentials {
    email: string,
    password: string,
    repeat_password: string
}

type LogoutResponse = {
    detail: string,
    status_code: number
}

export type EmailVerifiedResponse = {
    detail: string,
    status_code: number
}


export const loginPostRequest = async (credentials: LoginCredentials): Promise<User> => {
    const url: string = "/api/auth/login/"
    const response = await ApiService.post(url, credentials)
    return response.data
}

export const logoutPostRequest = async (): Promise<LogoutResponse> => {
    const url: string = "/api/auth/logout/"
    const response = await ApiService.post(url)
    return response.data
}

export const retrieveUser = async (): Promise<User> => {
    const url: string = "/api/auth/user/"
    const response = await ApiService.get(url)
    return response.data
}

export const registerPostRequest = async (credentials: RegisterCredentials): Promise<object> => {
    const url: string = "/api/auth/register/"
    const response = await ApiService.post(url, credentials)
    return response.data
}

export const verifyEmailConfirm = async (uidb64: string, token: string): Promise<EmailVerifiedResponse> => {
    const url: string = `/api/auth/verify-email-confirm/${uidb64}/${token}/`
    const response = await ApiService.get(url)
    return response.data
}