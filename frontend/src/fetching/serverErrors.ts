interface Detail {
    [key: string]: string[];
}

interface ServerError {
    status_code: number,
    code: string,
    detail: string | Detail
}

export default ServerError