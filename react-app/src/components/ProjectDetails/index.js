import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { getOneProject } from "../../store/project";
import {
  addOneComment,
  updateOneComment,
  getAllComments,
  deleteOneComment,
} from "../../store/comments";
import "./Projects.css";

const ProjectDetails = ({ id }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { projectId } = useParams();
  const { commentId } = useParams();
  console.log("cId", commentId);
  const project = useSelector((state) => state.projects[projectId]);
  const user = useSelector((state) => state.session.user);
  const session = useSelector((state) => state.session);
  const commentState = useSelector((state) => state.comments);

  const [showCommentForm, setShowCommentForm] = useState(false);
  const [showCommentEditForm, setShowCommentEditForm] = useState(false);
  const [comment, setComment] = useState("");
  const [newComment, setNewComment] = useState("");
  const [handledComment, setHandledComment] = useState({});

  const handleClick = async (e) => {
    e.preventDefault();
    dispatch(getAllComments(projectId));
  };

  let reversedComments = [];
  if (project) {
    project.comments.map((comment) => {
      reversedComments.unshift(comment);
    });
    // console.log('comments', reversedComments[id])
  }
  useEffect(() => {
    dispatch(getAllComments(id));
    dispatch(getOneProject(projectId));
  }, [dispatch, projectId]);

  const handleComment = async (e) => {
    e.preventDefault();
    const newComment = { userId: user.id, projectId, comment };
    dispatch(addOneComment(newComment));
    setShowCommentForm(false);
    // history.push(`/projects/${projectId}`);
  };

  const handleDelete = async (e, id) => {
    // e.preventDefault();
    //  console.log(project.comments.shift(id))
    console.log('this is e', e)
    let comments = project.comments;
    for (let i = 0; i > comments.length; i++) {
      let commentObj = comments[i];
      // if (commentObj.id === id) {
      const res = await dispatch(deleteOneComment(commentObj.id));
      // }
      // }
    }
  };

  if (project) {
    console.log("--------", project);
  }

  const handleEditProjectButton = (e) => {
    e.preventDefault();
    history.push(`/projects/${projectId}/edit`);
  };

  useEffect(() => {
    console.log(commentState);
  }, [commentState]);

  return (
    <>
      {project && (
        <div id="project-container">
          <div className="title">{project.title}</div>
          <div id="project-details">
            By
            <span className="username-category">{project.owner.username}</span>
            in<span className="username-category">{project.category}</span>
            {session.user.id === project.owner.id && (
              <div>
                <button onClick={handleEditProjectButton}>Edit</button>
              </div>
            )}
          </div>
          <div className="project-image-container">
            <img
              className="project-images"
              src={project.titleImage}
              alt="Completed project"
            ></img>
          </div>
          <div id="overview-title">
            Project Overview:
            <p id="project-overview">{project.overview}</p>
          </div>
          <ul id="supplies-title">
            Supplies Needed:
            {project.supplies.map((supply) => (
              <>
                <li className="supply-list" key={supply.id}>
                  {supply.supply}
                </li>
              </>
            ))}
          </ul>
          <ul>
            {project.instructions.map((instruction) => (
              <div className="instruction-container">
                <div className="instruction-title">
                  Step {instruction.stepOrder}:
                </div>
                <div className="project-image-container">
                  <img
                    className="instruction-image"
                    key={instruction.id}
                    src={instruction.photoUrl}
                    alt={`Step ${instruction.stepOrder}`}
                  ></img>
                </div>
                <li className="instructions" key={instruction.id}>
                  {instruction.instructions}
                </li>
              </div>
            ))}
          </ul>
          {showCommentForm && (
            <form className="comment-form" onSubmit={handleComment}>
              <label className="comments-title">Leave a comment here:</label>
              <textarea
                className="comment-box"
                rows="5"
                cols="80"
                type="text"
                onChange={(e) => setComment(e.target.value)}
                value={comment}
              />
              <button
                className="submit-comment"
                onClick={handleComment}
                type="submit"
              >
                Submit Comment
              </button>
            </form>
          )}
          <ul className="comments-title">
            Comments:
            {user && (
              <button
                id="leave-comment-btn"
                onClick={(e) => setShowCommentForm(true)}
              >
                Post a comment
              </button>
            )}
            {reversedComments.map((comment) => (
              <>
                <li className="comments" key={comment.id}>
                  {comment.comment}
                </li>
                {user.id == comment.userId && (
                  <div className="comment-btn-container">
                    <button onClick={handleDelete}>Edit</button>
                    <button onClick={handleDelete}>Delete</button>
                  </div>
                )}
              </>
            ))}
          </ul>
        </div>
      )}
    </>
  );
};

export default ProjectDetails;
