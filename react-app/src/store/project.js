const GET_PROJECTS = "/projects/";
const GET_PROJECT = "/projects/:projectId";
const ADD_PROJECTS = "/projects/new";
const UPDATE_PROJECTS = "/projects/update";
const DELETE_PROJECTS = "/projects/delete";
const SEARCH_RESULTS = "/howto/search";
// const ADD_VIEW = "/projects/add/views";

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

const searchResult = (results) => ({
  type: SEARCH_RESULTS,
  payload: results,
});

export const getAllProjects = () => async (dispatch) => {
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/projects/`);
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(getProjects(data));
    return data;
  }
};

export const getOneProject = (projectId) => async (dispatch) => {
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/projects/${projectId}`);
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
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/projects/new`, {
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
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/projects/${data.id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  if (response.ok) {
    const project = await response.json();
    dispatch(updateProjects(project));
    return project;
  }
};

export const deleteOneProject = (projectId) => async (dispatch) => {
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/projects/${projectId}`, {
    method: "DELETE",
  });
  if (response.ok) {
    dispatch(deleteProjects(projectId));
    return "Deleted.";
  }
};

export const search = (search) => async (dispatch) => {
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/search/${search}`);
  if (response.ok) {
    const data = await response.json();
    dispatch(searchResult(data));
    return data;
  }
};

// const updateProjectView = (view) => ({
//   type: ADD_VIEW,
//   payload: view,
// });

// export const updateView = (projectId) => async (dispatch) => {
//   const res = await fetch(`${process.env.REACT_APP_API_URL}/api/projects/add/views`, {
//     method: "PUT",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       projectId: projectId,
//       // views: 2,
//     }),
//     credentials: 'include', 
//   });
//   // console.log("Response status:", res.status);
//   // console.log("Response text:", await res.text());
//   if (res.ok) {
//     const data = await res.json();
//     dispatch(updateProjectView(data));
//     return data;
//   }
// };

const initialState = {};

export default function projectReducer(state = initialState, action) {
  let newState;
  switch (action.type) {
    case GET_PROJECTS:
      newState = { ...state };
      action.payload.projects.map(
        (project) => (newState[project.id] = project)
      );
      return newState;

    case GET_PROJECT:
      newState = {
        ...state,
        [action.payload.project.projectId]: action.payload.project,
      };
      return newState;

    case ADD_PROJECTS:
      newState = {
        ...state,
        [action.payload.projectId]: action.payload,
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

    case SEARCH_RESULTS:
      newState = {};
      action.payload.projects.map(
        (project) => (newState[project.id] = project)
      );
      return newState;
    // case ADD_VIEW:
    //   newState = { ...state };
    //   console.log(newState)
    //   return state;
    default:
      return state;
  }
}
