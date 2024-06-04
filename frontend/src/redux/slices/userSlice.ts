import { PayloadAction, createSlice } from "@reduxjs/toolkit"

export interface User {
    is_active: boolean,
    email: string,
};

export interface UserAuthenticated {
    authenticated: boolean,
    currentUser: User
};

const initialState: UserAuthenticated = {
    authenticated: false,
    currentUser: {
        is_active: false,
        email: "",
    }
};

export const UserSlice = createSlice({
    name: "User",
    initialState,
    reducers: {
        login: (state, action: PayloadAction<User>) => {
            if (action.payload.is_active) {
                state.authenticated = true
                state.currentUser = action.payload
            }
        },
        logout: (state) => {
            state.authenticated = false
            const user = {is_active: false, email: ""} as User
            state.currentUser = user
        },
    }
});

export const { login, logout } = UserSlice.actions;
export default UserSlice.reducer

