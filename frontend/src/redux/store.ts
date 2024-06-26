import { configureStore } from '@reduxjs/toolkit'
import { UserSlice } from './slices/userSlice'
import { WebsiteAppearanceSlice } from './slices/appearanceSlice'

export const store = configureStore({
    reducer: {
        users: UserSlice.reducer,
        websiteAppearance: WebsiteAppearanceSlice.reducer
    },
})

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch

