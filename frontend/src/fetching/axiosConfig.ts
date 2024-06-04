import axios from "axios";

/*  
url of remote server
most likely will be moved to separate file
*/
const baseHostURL = "http://127.0.0.1:8000";

/* 
API class instance which will handle 
all the request throughout the lifecycle of application 
*/

const ApiService = axios.create({
    baseURL: baseHostURL,
    validateStatus: (status) => status >= 200 && status < 300,
    withCredentials: true,
})

ApiService.interceptors.response.use(
    (response) => {
        // Log successful response
        console.log('Interceptor Success Response:', response);
        return response;
    },
    async (error) => {
        const originalReq = error.config;

        // Log error response before any processing
        console.log('Interceptor Error Response:', error.response);

        if (error.response.status === 401 && originalReq && !originalReq._isRetry) {
            originalReq._isRetry = true;
            try {
                console.log('Attempting to refresh token');
                await axios(ApiService.defaults.baseURL + "/api/auth/token/refresh/", {
                    withCredentials: true,
                    method: "post"
                });
                console.log('Token refreshed successfully');
                return ApiService.request(originalReq);
            } catch (err) {
                console.error("Unable to obtain a new pair of tokens", err);
            }
        }

        // Log and re-throw the error if it's not handled
        console.log('Interceptor Final Error:', error);
        throw error;
    }
);

export default ApiService
