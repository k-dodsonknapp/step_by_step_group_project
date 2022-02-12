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

const EditCommentForm = () => {
  const { commentId } = useParams();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(updateOneComment(commentId));
  }, [dispatch, commentId]);

  const comment = useSelector((state) => state.comment[commentId]);
  const sessionUser = useSelector((state) => state.session.user);

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
      ...comment,
    };

    await dispatch(updateOneComment(payload));

    if (sessionUser) {
      return (
        <>
          <form onSubmit={handleSubmit}>
            <input type="text" value={name} onChange={updateBody} required />
            <textarea value={body} onChange={updateBody} required />
            <button type="submit">Edit</button>

            <button className="options" id="del-button" onClick={ahandleSubmit}>
              Delete
            </button>
          </form>
        </>
      );
    }
  };
};

export default EditCommentForm;
