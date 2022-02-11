const GET_PROJECTS = "/projects/";
const GET_PROJECT = "/projects/:projectId"
const ADD_PROJECTS = "/projects/new";
const UPDATE_PROJECTS = "/projects/update";
const DELETE_PROJECTS = "/projects/delete";

// const GET_PROJECT = "/projects/:id";

const getProjects = (projects) => ({
  type: GET_PROJECTS,
  payload: projects,
});

const getProject = (project) => ({
  type: GET_PROJECT,
  payload: project,
});

const addProjects = (projects) => ({
  type: ADD_PROJECTS,
  payload: projects,
});

const updateProjects = (projects) => ({
  type: UPDATE_PROJECTS,
  payload: projects,
});

const deleteProjects = (projectId) => ({
  type: DELETE_PROJECTS,
  payload: projectId,
});

export const getAllProjects = () => async (dispatch) => {
  const response = await fetch("/api/projects/");
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    console.log(data)
    dispatch(getProjects(data));
    return data;
  }
};

export const getOneProject = (projectId) => async (dispatch) => {
  const response = await fetch(`/api/projects/${projectId}`);
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(getProject(data));
    return data;
  }
};

export const addOneProject = (data) => async (dispatch) => {
  const response = await fetch("/api/projects/new", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(addProjects(data));
    return data;
  }
};

export const updateOnePost = (data) => async (dispatch) => {
  const response = await fetch(`/api/projects/${data.id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(updateProjects(data));
    return data;
  }
};

export const deleteOneProject = (projectId) => async (dispatch) => {
  const response = await fetch(`/api/projects/${projectId}`, {
    method: "DELETE",
  });
  if (response.ok) {
    dispatch(deleteProjects(projectId));
    return "Deleted.";
  }
};

const initialState = {};

export default function projectReducer (state = initialState, action) {
  let newState;
  switch (action.type) {
    case GET_PROJECTS:
      newState = { ...state };
      action.payload.projects.map((project) => newState[project.id] = project);
      return newState;

    case GET_PROJECT:
      newState = { ...state, [action.payload.project.projectId]: action.payload.project}
      return newState

    case ADD_PROJECTS:
      newState = {
        ...state,
        [action.payload.id]: action.payload,
      };
      return newState;

    case UPDATE_PROJECTS:
      state[action.payload.id] = action.payload;
      newState = { ...state };
      return newState;

    case DELETE_PROJECTS:
      newState = { ...state };
      delete newState[action.payload];
      return newState;

    default:
      return state;
  }
}
