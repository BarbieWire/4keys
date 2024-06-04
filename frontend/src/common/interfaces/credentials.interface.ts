type InputType = "email" | "phone" | "text" | "password" | "number" | "date" | "url" | "search" | "checkbox" | "radio" | "file" | "color" | "range";
type KeyType = `fields_${InputType}` | `fields_repeat_${InputType}`

interface Field {
    type: InputType,
    placeholder: string,
    name: string,
    key: KeyType,
    icon: string
}

type FieldArray = Field[]

export type {
    FieldArray,
    Field,
    KeyType
}
