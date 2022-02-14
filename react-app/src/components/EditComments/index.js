import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { getOneProject } from "../../store/project";
import {
  getAllComments,
  addOneComment,
  updateOneComment,
  deleteOneComment,
} from "../../store/comments";

const EditCommentForm = ({ commentId, projectId }) => {
  // const { commentId } = useParams();
  // console.log(commentId)
  const history = useHistory();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(updateOneComment(commentId));
  }, [dispatch, commentId]);

  const comment = useSelector((state) => state.comments[commentId]);
  console.log("HOPEFULLY", comment)
  const sessionUser = useSelector((state) => state.session.user);

  const [idPath, setIdPath] = useState("")
  const [name, setName] = useState(comment?.id);
  const [body, setBody] = useState(comment?.comment);
  const updateBody = (e) => setBody(e.target.value);
  const ahandleSubmit = async (e) => {
    e.preventDefault();
    dispatch(deleteOneComment(commentId));
  };
  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      "comment": body,
      commentId
    };

    const data = await dispatch(updateOneComment(payload));
    console.log("ERIC SMELLS", data.projectId)
    setIdPath(data.id)
    // history.push("/")
    // history.push(`/projects/${data.projectId}`)
    window.location.reload(true)

  }

  useEffect(() => {
    dispatch(getOneProject(projectId))
  }, [dispatch, idPath, body])

  // if (sessionUser) {
  return (
    <>
      <form onSubmit={handleSubmit}>
        <input type="text" value={body} onChange={e => setBody(e.target.value)} required />
        {/* <textarea value={body} onChange={updateBody} required /> */}
        <button type="submit">Edit</button>

        {/* <button className="options" id="del-button" onClick={handleSubmit}> */}
        {/* Delete */}
        {/* </button> */}
      </form>
    </>
  );
  // };
};

export default EditCommentForm;
