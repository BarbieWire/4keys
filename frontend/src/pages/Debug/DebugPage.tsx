import React from 'react';

import { loginPostRequest } from '../../fetching/authentication';

const DebugPage = () => {
    const credentials = {
        email: "kirillbondarenko365@gmail.com",
        password: "youtube2020"
    }
    return (
        <div style={{fontSize: "12em"}}>
            <button onClick={() => loginPostRequest(credentials)}>click me </button>
        </div>
    );
};

export default DebugPage;