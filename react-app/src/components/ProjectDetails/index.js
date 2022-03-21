import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { deleteOneProject, getOneProject } from "../../store/project";
import { addOneComment, deleteOneComment, updateOneComment } from "../../store/comments";
// import EditCommentForm from "../EditComments";
import "./Projects.css";

const ProjectDetails = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { projectId } = useParams();
  const project = useSelector((state) => state.projects[+projectId]);
  console.log("PPPPPPPPPP",)
  
  const user = useSelector((state) => state.session.user);
  const session = useSelector(state => state.session);
  // const commentState = useSelector((state) => state.comments);
  
  
  const [showCommentForm, setShowCommentForm] = useState(false);
  const [showCommentEditForm, setShowCommentEditForm] = useState(false);
  const [comment, setComment] = useState('');
  // console.log("IDKDKDKDKD", comment)
  const [newComment] = useState(0);
  const [commentId, setCommentId] = useState(0);
  console.log("TTTTTTT", commentId)
  const [editClicked, setEditClicked] = useState(true)
  const [showComment, setShowComment] = useState(true)
  const [showPostCommentBtn, setShowPostCommentBtn] = useState(true)
  // const editComment = useSelector((state) => state.comments);
  const [body, setBody] = useState(comment?.comment);
  const [editBody, setEditBody] = useState(project?.comments[commentId]?.comment);
  console.log("((((()((((((", project?.comments[commentId]?.comment)
  
  let reversedComments = []
  if (project) {
    project.comments.map(comment => {
      return reversedComments.unshift(comment)
    })
  }

  useEffect(() => {
    dispatch(updateOneComment(commentId));
  }, [dispatch, commentId]);


  useEffect(() => {
    addOneComment(newComment)
  }, [dispatch, newComment])

  useEffect(() => {
    dispatch(getOneProject(projectId))
  }, [dispatch, projectId])

  useEffect(() => {
    dispatch(getOneProject(+projectId));
  }, [dispatch, projectId]);

  const saveEditComment = async (e) => {
    e.preventDefault();
    const payload = {
      "comment": editBody,
      commentId
    };
    const data = await dispatch(updateOneComment(payload));
    // setIdPath(data.id)
  }

  const handleComment = async (e) => {
    e.preventDefault();
    const newComment = { 
      userId: user?.id, 
      projectId, 
      comment 
    };
    await dispatch(addOneComment(newComment));
    await dispatch(getOneProject(projectId))
    setShowCommentForm(false)
  };

  const cancel = (e) => {
    e.preventDefault();
    setEditClicked(false)
    setShowComment(true)
    setShowCommentEditForm(false);

  }

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

  const handleDeleteComment = async (e) => {
    console.log(e)
    e.preventDefault();
    await dispatch(deleteOneComment(e.target.id))
    dispatch(getOneProject(projectId))
  }

  const handleShowEditForm = async (e) => {
    e.preventDefault();
    setShowComment(false)
    const id = +e.target.id
    console.log("LLLLLLLL", id)
    setEditBody(project?.comments[+id]?.comment)
    setCommentId(id)
    // console.log(+commentId === +id)
    setComment(project.comments.id)
    // console.log(id)
    if (showCommentEditForm === false) {
      setShowCommentEditForm(true);
      setShowComment(false)
    } else {
      setShowCommentEditForm(false)
      setShowComment(true)
    }
    if (showCommentForm === true) {
      setShowCommentForm(false)
      setShowPostCommentBtn(true)
    }
  }

  const postComment = (e) => {
    e.preventDefault()
    if (showCommentForm === false) {
      setShowCommentForm(true)
    }else{
      setShowCommentForm(false)
    }
    setShowPostCommentBtn(false)
    if (showCommentEditForm === true) {
      setShowCommentEditForm(false)
    }
    
  }

  // const cancel = (e) => {
  //   e.preventDefault();
  //   setShowCommentEditForm(false)
  // }

  // const handleEditComment = async (e) => {
  //   // console.log("eeeeeeeeeeeee", e.target, e.target.value)
  //   e.preventDefault();
  //   // console.log("COOKMMMMMMENT",comment)

  //   // await dispatch(updateOneComment(e.target.id, newComment))
  //   // dispatch(getOneProject(projectId))
  // }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      "comment": body,
      commentId
    };
    await dispatch(updateOneComment(payload));
    setEditClicked(false)
    // setIdPath(data.id)
  }

  const cancelNewComment = (e) => {
    e.preventDefault();
    if (showCommentForm === true) {
      setShowCommentForm(false);
    }else {
      setShowCommentForm(true);
    }
    setShowPostCommentBtn(true)

  }

  // useEffect(() => {
  //   console.log(commentState);
  // }, [commentState]);

  return (
    <>
      {project && (
        <div id="project-container">
          <div className="title">{project?.title}</div>
          <div id="project-details">
            By
            <span className="username-category">{project?.owner?.username}</span>
            in<span className="username-category">{project?.category}</span>
            {session?.user?.id === project?.owner?.id && (
              <div className="btn-div">
                <button className="submit-comment" onClick={handleEditProjectButton}>Edit</button>
                <button className="submit-comment" onClick={handleDelete}>Delete</button>
              </div>
            )}
          </div>
          <div className="project-image-container">
            <img
              className="project-images"
              src={project?.titleImage}
              alt="Completed project"
            ></img>
          </div>
          <div id="overview-title">
            Project Overview:
            <p id="project-overview">{project?.overview}</p>
          </div>
          <ul id="supplies-title">
            Supplies Needed:
            {project?.supplies?.map((supply) => (
              <div key={supply?.id}>
                <li className="supply-list" >
                  {supply?.supply}

                </li>
              </div>
            ))}
          </ul>
          <ul>
            {project?.instructions?.map((instruction) => (
              <div className="instruction-container" key={instruction?.id}>
                <div className="instruction-title">
                  Step {instruction?.stepOrder} {instruction?.stepTitle}:
                </div>
                <div className="project-image-container">
                  <img
                    className="instruction-image"
                    key={instruction?.id}
                    src={instruction?.photoUrl}
                    alt={`Step ${instruction?.stepOrder}`}
                  ></img>
                </div>
                <li className="instructions" key={instruction?.id}>
                  {instruction?.instructions}
                </li>
              </div>
            ))}
          </ul>
          {showCommentForm && (
            // <form className="comment-form" onSubmit={handleComment}>
            // <label className="comments-title">Leave a comment here:</label>
            // <textarea
            //   className="comment-box"
            //   rows='5'
            //   cols='80'
            //   type="text"
            //   value={comment}
            //   onChange={(e) => setComment(e.target.value)}
            // ></textarea>
            <button onClick={handleComment} className="submit-comment" type="submit">Submit Comment</button>
            // </form>
          )}
          {/* <ul className="comments-title"> */}
          <h2 className="num-comments">{reversedComments.length} Comments</h2>
          {reversedComments?.map((comment) => (
            <div key={comment?.id}>
              <div className="comments" >
                <div className="user">
                  <div className="user-container">
                    <div className="userImg"></div>
                    <div className="username">
                      {comment.username}
                    </div>
                  </div>
                  {user?.id === comment?.userId && (
                    <div className="comment-btn-container">
                      <button className="submit-commentt" id={comment?.id} onClick={handleDeleteComment}>Delete</button>
                      <button className="submit-commentt" id={comment?.id} onClick={handleShowEditForm}>Edit</button>
                    </div>
                  )}
                </div>
                {showComment && (
                  <div className="comment">
                    {comment?.comment}
                  </div>
                )}
              </div>
              {+comment?.id === +commentId && (
                <div>
                  {showCommentEditForm && (
                    // <EditCommentForm commentId={comment.id} projectId={projectId} />
                    <div className="comment-">

                      <form className="comment-form" onSubmit={handleSubmit}>
                        <div className="edit-container">
                          <div className="prf-image">

                          </div>
                          <div className="edit-comment">
                            <textarea 
                            className="edit-input" 
                            type="text" 
                            value={editBody} 
                            onChange={e => 
                            setEditBody(e.target.value)} 
                            required 
                            />
                            {/* <textarea value={body} onChange={updateBody} required /> */}
                            <div className="btn-container">
                              <button onClick={cancel} className="cancel-edit" type="submit">Cancel</button>
                              <button onClick={saveEditComment} className="submit-comment" type="submit">Save</button>
                            </div>
                          </div>
                        </div>


                        {/* <button className="options" id="del-button" onClick={handleSubmit}> */}
                        {/* Delete */}
                        {/* </button> */}
                      </form>
                    </div>
                  )}
                </div>
              )}

              <div >

              </div>
            </div>
          ))}
          {user && showPostCommentBtn && (
            <div className="post-comment">
              <button
                id="leave-comment-btn"
                onClick={postComment}
              >
                Post Comment
              </button>
            </div>
          )}

          {showCommentForm && (
            <div className="comment-">

              <form className="comment-form" onSubmit={handleSubmit}>
                <div className="edit-container">
                  <div className="prf-image">

                  </div>
                  <div className="edit-comment">
                    <input placeholder="Please Leave a Comment" className="edit-input" type="text" value={body} onChange={e => setBody(e.target.value)} required />
                    {/* <textarea value={body} onChange={updateBody} required /> */}
                    <div className="btn-container">
                      <button onClick={cancelNewComment} className="cancel-edit" type="submit">Cancel</button>
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
          {/* </ul> */}
        </div>
      )}
    </>
  );
};

export default ProjectDetails;
