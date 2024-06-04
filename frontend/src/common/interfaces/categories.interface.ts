export interface CategoryEntry {
    category: string,
    children?: CategoryEntry[]
}

export type Categories = Array<CategoryEntry>
