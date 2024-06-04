interface Cover {
    id: number,
    picture: string
}

export interface ProductCard {
    id: number;
    name: string;
    category: string;
    description: string;
    brand: string;
    color: string;
    normal_price: string;
    price_after_discount: number | null;
    stock: number;
    vendor_code: string;
    cover: Cover | null
}
