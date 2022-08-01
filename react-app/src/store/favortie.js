const GET_FAVORITES = '/api/favorite';

const getFavorites = (favorites) => ({
    type: GET_FAVORITES,
    favorites
})

export const getPostFavorites = (id) => async (dispatch) => {
    const response = await fetch(`/api/favorite/${id}`);
    const favorites = await response.json();
    if (response.ok) {
        dispatch(getFavorites(favorites));
        return favorites;
    }
}

const GET_ALL_FAVORITES = '/api/favorite/'

const allFavorites = (favorites) => ({
    type: GET_ALL_FAVORITES,
    favorites
})

export const getAllFavorites = () => async (dispatch) => {
    const response = await fetch(`/api/favorite/`);
    const favorites = await response.json();
    if (response.ok) {
        dispatch(allFavorites(favorites));
        return favorites;
    }
}

const ADD_FAVORITE = '/api/favorite/add';

const addFavorite = (favorite) => ({
    type: ADD_FAVORITE,
    favorite
});

export const addPostFavorite = (favoriteObj) => async (dispatch) => {
    // console.log(favoriteObj, "favoriteObj");
    const response = await fetch('/api/favorite/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(favoriteObj)
    });
    const favorite = await response.json();
    if (response.ok) {
        dispatch(addFavorite(favorite));
        return favorite;
    }
}

const DELETE_FAVORITE = '/api/favorite/delete';

const deleteFavorite = (favorite) => ({
    type: DELETE_FAVORITE,
    favorite
});

export const deletePostFavorite = (favorite) => async (dispatch) => {
    // console.log("delete favorite", favorite);
    const response = await fetch('/api/favorite/delete', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(favorite)
    });
    const favorites = await response.json();
    if (response.ok) {
        dispatch(deleteFavorite(favorites));
        return favorites;
    }
}

export default function favoritesReducer(state = [], action) {
    let newState;
    switch (action.type) {
        case GET_FAVORITES:
            return action.favorites;
        case GET_ALL_FAVORITES:
            return action.favorites;
        case ADD_FAVORITE:
            // console.log("WWWWWW", action);
            newState = { ...state };

            newState = { ...newState, [action.favorite.id]: action.favorite };
            return newState;
        case DELETE_FAVORITE:
            newState = {...state}
            // console.log(newState.favorite, "newState");
            delete newState[action.favorite.id];
            return newState;
            // return state.filter(favorite => favorite.id !== action.favorite.id);
        default:
            return state;
    }
}