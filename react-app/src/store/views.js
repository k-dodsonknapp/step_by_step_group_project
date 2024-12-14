const GET_VIEW = '/views/:projectId';
const GET_ONE_VIEW = '/views/:id';
const NEW_VIEW = '/views/new';
const ADD_VIEW = '/views/add';

const getSingleProjectView = (view) => ({
    type: GET_ONE_VIEW,
    payload: view,
});

export const getOneView = (id) => async (dispatch) => {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/api/views/${id}`);
    if (res.ok) {
        const data = await res.json();
        if (data.errors) {
            return "error occured getting one project views"
        };
        dispatch(getSingleProjectView(data));
        return data;
    };
};

const getProjectView = (view) => ({
    type: GET_VIEW,
    payload: view,
});

export const getView = () => async (dispatch) => {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/api/views/`);
    if (res.ok) {
        const data = await res.json();
        if (data.errors) {
            return;
        }
        dispatch(getProjectView(data));
        return data;
    };
};

const newProjectView = (view) => ({
    type: NEW_VIEW,
    payload: view,
});

export const addNewProjectView = (view) => async (dispatch) => {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/api/views/new`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(view),
    });
    if (res.ok) {
        const data = await res.json();
        dispatch(newProjectView(data));
        return data;
    } else {
        return "error occured adding new view";
    };
};

const updateProjectView = (view) => ({
    type: ADD_VIEW,
    payload: view
});

export const updateView = (projectId, viewCount) => async (dispatch) => {
    console.log(projectId)
    console.log(viewCount)
    const res = await fetch(`${process.env.REACT_APP_API_URL}/api/views/add`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "projectId": projectId,
            "views": viewCount
        }),
    });
    if (res.ok) {
        const data = await res.json();
        dispatch(updateProjectView(data));
        return data;
    };
};

export default function viewReducer(state = {}, action) {
    let newState;
    switch (action.type) {
        case GET_VIEW:
            newState = { ...state };
            return {
                ...newState,
                "views": action.payload.views
            };
        case GET_ONE_VIEW:
            newState = { ...state };
            return {
                ...newState,
                "view": action.payload
            };
        case ADD_VIEW:
            newState = { ...state };
            newState.view = action.payload.view;
            return state;
        default:
            return state;
    };
};