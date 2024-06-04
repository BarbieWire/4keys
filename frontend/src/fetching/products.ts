import axiosFetch from "./axiosConfig";


export const popularGetRequest = async (): Promise<object> => {
    const url: string = "api/products/?filter=popularity&page=1"
    const response = await axiosFetch.get(url)
    console.log(response)
    return response.data
}

export const recentlyAddedGetRequest = async (): Promise<object> => {
    const url: string = "api/products/?filter=newness&page=1"
    const response = await axiosFetch.post(url)
    console.log(response)
    return response.data
}