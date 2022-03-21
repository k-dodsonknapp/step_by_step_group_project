const GET_COMMENTS = "/comments/";
const ADD_COMMENT = "/comments/new";
const UPDATE_COMMENT = "/comments/update";
const DELETE_COMMENT = "/comments/delete";

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
  const response = await fetch(`/api/projects/${projectId}/comments`);
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }

    dispatch(getComments(data));
    return data;
  }
};

export const addOneComment = (comment) => async (dispatch) => {
  const response = await fetch(`/api/comments/new`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(comment),
  });
  if (response.ok) {
    const data = await response.json();
    console.log('data:', data)
    dispatch(addComment(data.comment));
    return data.comment;
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
    console.log(data)
    return data;
  }
};
export const deleteOneComment = (id) => async (dispatch) => {
  const res = await fetch(`/api/comments/${id}`, {
    method: "DELETE",
  });
  if (res.ok) {
    dispatch(deleteComment(id));
    return "Successfully deleted.";
  }
};

const initialState = {};

export default function commentReducer(state = initialState, action) {
  let newState;
  switch (action.type) {
    case GET_COMMENTS:
      newState = {};
      action.payload.comments.map(
        (comment) => (newState[comment.id] = comment)
      );
      console.log(newState)
      return newState;

    case ADD_COMMENT:
      newState = {
        ...state,
      };
      newState[action.payload.id] = action.payload
      return newState;

    case UPDATE_COMMENT:
      state[action.payload.commentId] = action.payload.comment;
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
