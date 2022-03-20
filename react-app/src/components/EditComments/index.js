import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { useHistory } from "react-router-dom";
import { getOneProject } from "../../store/project";
import { updateOneComment } from "../../store/comments";

const EditCommentForm = ({ commentId, projectId }) => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(updateOneComment(commentId));
  }, [dispatch, commentId]);

  const comment = useSelector((state) => state.comments[commentId]);

  const [idPath, setIdPath] = useState("")
  const [body, setBody] = useState(comment?.comment);
  const [editClicked, setEditClicked] = useState(true)
  const [editForm, setEditForm] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      "comment": body,
      commentId
    };
    const data = await dispatch(updateOneComment(payload));
    setEditClicked(false)
    setIdPath(data.id)
  }

  useEffect(() => {
    dispatch(getOneProject(projectId))
    dispatch(updateOneComment(commentId))
  }, [dispatch, idPath, body, commentId, projectId])

  // if (sessionUser) {
  return (
    <>{editClicked && (
      <div className="comment-">

        <form className="comment-form" onSubmit={handleSubmit}>
          <div className="edit-container">
            <div className="prf-image">

            </div>
            <div className="edit-comment">
              <input className="edit-input" type="text" value={body} onChange={e => setBody(e.target.value)} required />
              {/* <textarea value={body} onChange={updateBody} required /> */}
              <div className="btn-container">
              <button onClick={} className="cancel-edit" type="submit">Cancel</button>
                <button className="submit-comment" type="submit">Save</button>
              </div>
            </div>
          </div>


          {/* <button className="options" id="del-button" onClick={handleSubmit}> */}
          {/* Delete */}
          {/* </button> */}
        </form>
      </div>
    )}
    </>
  );
  // };
};

export default EditCommentForm;
