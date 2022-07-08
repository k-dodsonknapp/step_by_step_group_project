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
    console.log(favoriteObj, "favoriteObj");
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

const DELETE_FAVORITE = '/api/favorites/delete';

const deleteFavorite = (favorite) => ({
    type: DELETE_FAVORITE,
    favorite
});

export const deletePostFavorite = (favorite) => async (dispatch) => {
    const response = await fetch(DELETE_FAVORITE, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(favorite)
    });
    const favorite = await response.json();
    if (response.ok) {
        dispatch(deleteFavorite(favorite));
        return favorite;
    }
}

export default function favoritesReducer (state = [], action) {
    let newState;
    switch (action.type) {
        case GET_FAVORITES:
            return action.favorites;
        case GET_ALL_FAVORITES:
            return action.favorites;
        case ADD_FAVORITE:
            console.log("WWWWWW",action);
            return { ...state, action };
        case DELETE_FAVORITE:
            return state.filter(favorite => favorite.id !== action.favorite.id);
        default:
            return state;
    }
}