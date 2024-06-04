import { PayloadAction, createSlice } from "@reduxjs/toolkit"

type DraggableStrip = {
    dragging: boolean,
    startX: number,
    scrollLeft: number,
    moving: boolean
}

interface WebsiteAppearance {
    backgroundTinted: boolean,
    searchPrompt: string,
    draggableStrip: DraggableStrip
}

const initialState: WebsiteAppearance = {
    backgroundTinted: false,
    draggableStrip: {
        dragging: false,
        startX: 0,
        scrollLeft: 0,
        moving: false
    },
    searchPrompt: "",
}


export const WebsiteAppearanceSlice = createSlice({
    name: "Appearance",
    initialState,
    reducers: {
        darkenBackground: (state, action: PayloadAction<boolean>) => {
            state.backgroundTinted = action.payload
        },

        updateSearchingPrompt: (state, action: PayloadAction<string>) => {
            state.searchPrompt = action.payload
        },

        updateDraggableStrip: (state, action: PayloadAction<object>) => {
            state.draggableStrip = {
                ...state.draggableStrip,
                ...action.payload
            }
        },
    }
})

export const { darkenBackground, updateDraggableStrip, updateSearchingPrompt } = WebsiteAppearanceSlice.actions;
export default WebsiteAppearanceSlice.reducer;