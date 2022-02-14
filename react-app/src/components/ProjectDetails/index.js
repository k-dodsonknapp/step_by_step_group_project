import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { deleteOneProject, getOneProject } from "../../store/project";
import { addOneComment, updateOneComment } from "../../store/comments";
import "./Projects.css";

const ProjectDetails = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { projectId } = useParams();
  const project = useSelector((state) => state.projects[projectId]);
  // console.log("PROJECTSsssssssssss", project)
  const user = useSelector((state) => state.session.user);
  const session = useSelector(state => state.session);
  const commentState = useSelector((state) => state.comments);

  const [showCommentForm, setShowCommentForm] = useState(false);
  const [showCommentEditForm, setShowCommentEditForm] = useState(false);
  const [comment, setComment] = useState("");
  const [newComment, setNewComment] = useState("");

  let reversedComments = []
  if (project) {
    project.comments.map(comment => {
      reversedComments.unshift(comment)
    })
    console.log('comments', reversedComments)
  }
  useEffect(() => {
    dispatch(getOneProject(projectId));
  }, [dispatch, projectId]);

  const handleComment = (e) => {
    e.preventDefault();
    const newComment = { userId: user.id, projectId, comment };
    dispatch(addOneComment(newComment));
    setShowCommentForm(false)
  };

  const handleEdit = (e) => {
    e.preventDefault();
    const newComment = { userId: user.id, projectId, comment };
    dispatch(updateOneComment(newComment));
  };

  const handleEditProjectButton = (e) => {
    e.preventDefault();
    history.push(`/projects/${projectId}/edit`)
  }

  const handleDelete = async (e) => {
    e.preventDefault();
    const projectDelete = await dispatch(deleteOneProject(projectId))
    if (projectDelete) {
      history.push('/')
    }
  }
  // const deleteComment = async (id) => {
  //   await dispatch(spotStore.thunk_deleteSpot({ id }));
  //   history.push("/spots");
  // };

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
                <button onClick={handleDelete}>Delete</button>
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
                rows='5'
                cols='80'
                type="text"
                onChange={(e) => setComment(e.target.value)}
                value={comment}
              ></textarea>
              <button className="submit-comment" type="submit">Submit Comment</button>
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
                    <button onClick={handleEdit}>Edit</button>
                    <button onClick={handleEdit}>Delete</button>
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
