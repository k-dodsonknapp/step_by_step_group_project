const GET_COMMENTS = "/comments/GET_COMMENTS";
const ADD_COMMENT = "/comments/ADD_COMMENT";
const UPDATE_COMMENT = "/comments/update";
const DELETE_COMMENT = 'comments/DELETE_COMMENT';

const getComments = (comments) => ({
  type: GET_COMMENTS,
  payload: comments,
});

const addComment = (comment) => ({
  type: ADD_COMMENT,
  payload: comment,
});

const updateComment = (comment) => ({
  type: UPDATE_COMMENT,
  payload: comment,
});

const deleteComment = (comment) => ({
  type: DELETE_COMMENT,
  payload: comment,
});

export const getAllComments = (projectId) => async (dispatch) => {
  const response = await fetch(`/api/comments/projects/${projectId}/comments`);
  if (response.ok) {
    const data = await response.json();
   
      dispatch(getComments(data));
      return data;

  
  }
};

export const addOneComment = (comment) => async(dispatch) => {
  const response = await fetch(`/api/comments/new`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(comment),
  });
  const data = await response.json();
  if (response.ok) {
  
    console.log('data:', data)
    dispatch(addComment(data));
    return data;
  }
};

export const updateOneComment = ({commentId, comment}) => async (dispatch) => {
  const response = await fetch(`/api/comments/${commentId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({commentId, comment}),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(updateComment(data));
    return data;
  }
};
export const deleteOneComment = (id) => async (dispatch) => {
  const res = await fetch(`/api/comments/${id}`, {
    method: "DELETE",
  });
  if (res.ok) {
    const comment = await res.json();
    dispatch(deleteComment(comment.id));
    return "Successfully deleted.";
  }
};

const initialState = {};

const commentReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_COMMENTS:
      newState = {
        ...state,
        ...state.comments = {
            ...action.payload
        }
      }
      return newState;
    case ADD_COMMENT:
      newState = {
        ...state,
        [action.payload.id]: action.payload
      };
     
      return newState;

    case UPDATE_COMMENT:
      state[action.payload.comment.id] = action.payload.comment;
      newState = { ...state };
      return newState;

    case DELETE_COMMENT:
      newState = { ...state };
      delete newState[action.payload];
      return newState;
    default:
      return state;
  }
}

export default commentReducer;