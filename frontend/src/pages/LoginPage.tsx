import React from 'react';
import CredentialForm from "../components/credentials/LoginForm";
import loginPNG from "../assets/backgrounds/login5.jpg"


const LoginPage = () => {
    return (
        <div style={{ backgroundImage: `url(${loginPNG})`, backgroundSize: "cover" }}>
            <CredentialForm/>
        </div>
    );
};


export default LoginPage;