import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { deleteOneProject, getOneProject } from "../../store/project";
import { addOneComment, deleteOneComment, updateOneComment } from "../../store/comments";
import "./Projects.css";
import { getOneView, updateView } from "../../store/views";
import UserPhoto from "../UserPhoto";
import { addPostFavorite, deletePostFavorite, getPostFavorites } from "../../store/favortie";
// import { BsDot } from 'react-icons/bs';

const ProjectDetails = () => {

  const dispatch = useDispatch();
  const history = useHistory();
  const { projectId } = useParams();
  const project = useSelector((state) => state?.projects[+projectId]);
  const favorites = useSelector((state) => state?.favorites);
  console.log(favorites.favorite, "favorites");
  let view = useSelector(state => state?.views?.view)
  const user = useSelector((state) => state?.session?.user);
  console.log(user, "user")
  const session = useSelector(state => state?.session);
  console.log("session", session)
  const [showCommentForm, setShowCommentForm] = useState(false);
  const [showCommentEditForm, setShowCommentEditForm] = useState(false);
  // const [newComment] = useState(0);
  const [commentId, setCommentId] = useState(0);
  const [showComment, setShowComment] = useState(true);
  const [showPostCommentBtn, setShowPostCommentBtn] = useState(true);
  const [body, setBody] = useState('');
  const [editBody, setEditBody] = useState('');
  const [textColor, setTextColor] = useState('#bbb');
  const [favoriteComment, setFavoriteComment] = useState(true);
  const [favoriteLength, setFavoriteLength] = useState(0);

  console.log(favoriteLength, "favoriteLength")

  useEffect(() => {
    window.scrollTo(0, 0);
    let payload;
    if (favorites.favorite !== undefined) {
      // setFavoriteLength(favorites.favorite.length)
      payload = favorites.favorite.find(favorite => favorite.projectId === +projectId && favorite.userId === user.id)
      setFavoriteLength(favorites.favorite.length)
    }
    if (favorites.favorite && payload) {
      setFavoriteComment(false);
      setTextColor(setFavoriteComment ? '#b64360' : '#bbb');
    }
  }, []);

  useEffect(() => {
    if (favorites.favorite) {
      setFavoriteLength(favorites?.favorite?.length)
    }
    dispatch(getPostFavorites(+projectId));
  }, [dispatch])

  useEffect(() => {
    const addView = {
      "projectId": +projectId
    };
    dispatch(updateView(addView));
    dispatch(getOneView(+projectId));
    dispatch(getOneProject(projectId));
    dispatch(getOneProject(+projectId));
  }, [dispatch, projectId]);

  const saveEditComment = async (e) => {
    e.preventDefault();
    const payload = {
      "comment": editBody,
      commentId
    };
    await dispatch(updateOneComment(payload));
    if (showCommentEditForm === true) {
      setShowCommentEditForm(false);
      setShowComment(true);
    }
    await dispatch(getOneProject(+projectId));
  };

  const handleComment = async (e) => {
    e.preventDefault();
    const newComment = {
      userId: user?.id,
      projectId,
      comment: body,
      username: user?.username,
    };
    await dispatch(addOneComment(newComment));
    await dispatch(getOneProject(projectId));
    setBody('');
    setShowCommentForm(false);

    if (showPostCommentBtn === false) {
      setShowPostCommentBtn(true);
    };
  };

  const cancel = (e) => {
    e.preventDefault();
    setShowComment(true);
    setShowCommentEditForm(false);
  };

  const handleEditProjectButton = (e) => {
    e.preventDefault();
    history.push(`/projects/${projectId}/edit`);
  };

  const handleDelete = async (e) => {
    e.preventDefault();
    const projectDelete = await dispatch(deleteOneProject(projectId));
    if (projectDelete) {
      history.push('/');
    };
  };

  const handleDeleteComment = async (e) => {
    console.log(e)
    e.preventDefault();
    await dispatch(deleteOneComment(e.target.id));
    dispatch(getOneProject(projectId));
  };

  const handleShowEditForm = (commentId) => async (e) => {
    e.preventDefault();
    setShowComment(false);
    const id = +e?.target?.id;
    const comments = project.comments;
    let comms = {};
    comments.map(comment => {
      return comms[comment.id] = comment
    });
    setEditBody(comms[commentId].comment);
    setCommentId(id);
    if (showCommentEditForm === false) {
      setShowCommentEditForm(true);
      setShowComment(false);
    } else {
      setShowCommentEditForm(false);
      setShowComment(true);
    };
    if (showCommentForm === true) {
      setShowCommentForm(false);
      setShowPostCommentBtn(true);
    };
  };

  const postComment = (e) => {
    e.preventDefault()
    if (showCommentForm === false) {
      setShowCommentForm(true);
    } else {
      setShowCommentForm(false);
    };
    setShowPostCommentBtn(false);
    if (showCommentEditForm === true) {
      setShowCommentEditForm(false);
    };
  };

  const cancelNewComment = (e) => {
    e.preventDefault();
    if (showCommentForm === true) {
      setShowCommentForm(false);
    } else {
      setShowCommentForm(true);
    };
    setShowPostCommentBtn(true);
  };


  const favorite = async (e) => {

    console.log("ASDFASDF")
    e.preventDefault();
    if (user) {
      const payload = favorites.favorite.find(favorite => favorite.projectId === +projectId && favorite.userId === user.id)
      // console.log(payload, "NNNN")
      if (!payload) {
        setFavoriteComment(false);
        setTextColor(setFavoriteComment ? '#b64360' : '#bbb');
        const fav = {
          "projectId": +projectId,
          "userId": +user?.id,
        };
        dispatch(addPostFavorite(fav));
        dispatch(getOneProject(+projectId));
        setFavoriteLength(favorites?.favorite?.length)
        favorites.favorite.length++
        console.log(favoriteLength, "FAVORITE LENGTH")
      } else {
        return alert("You've already favorited this project")
      }
    } else {
      return alert("You must be logged in to favorite a project");
    }
    // dispatch(getPostFavorites(+projectId));

    // console.log(payload,"PAYLOAD")
    // if (favorites?.favorite?.includes(projectId)) {
    //   await dispatch(deleteOneProject(payload));
    // } else {
    //   await dispatch(addPostFavorite(+projectId));
    // }


    // const unfavorite = async (e) => {
    //   e.preventDefault();
    //   const payload = {
    //     "projectId": +projectId,
    //     "userId": user?.id,
    //   };
    //   await dispatch(getPostFavorites(+projectId));
    //   if (favorites?.favorite.includes(projectId)) {
    //     await dispatch(deletePostFavorite(payload));
    //   } else {
    //     await dispatch(getOneProject(+projectId));
    //   }
  }

  useEffect(() => {
    dispatch(getPostFavorites(+projectId));
  }, [dispatch]);

  const handleLogin = (e) => {
    history.push('/login');
  };

  const handleSignUp = (e) => {
    history.push('/sign-up');
  };

  return (
    <>
      {project && (
        <div id="project-container">
          <div className="title">{project?.title}</div>
          {/* <button className="favorite_btn"><span className="heart_span">❤</span> <span className="favorite_span">Favorite</span></button> */}
          <div id="project-details">
            By
            <span className="username-category">{project?.owner?.username}</span>
            in<span className="username-category">{project?.category}</span>
            <p>
              {/* <button>
                ❤
              </button> */}
              <span>❤ {favorites.favorite.length}</span>
              <span>👁 {view?.viewCount}</span>
            </p>
            {session?.user?.id === project?.owner?.id && (
              <div className="btn-div">
                <button className="submit-comment" onClick={handleEditProjectButton}>Edit</button>
                <button className="submit-comment" onClick={handleDelete}>Delete</button>
              </div>
            )}
          </div>
          <div className="project-image-container">
            <div className="favorite_btn_div">
              <button className="favorite_btn" onClick={favorite}><span className="heart_span" style={favorites.favorite.length ? { color: '#b64360' } : { color: "black" }}>❤</span> <span className="favorite_span">Favorite</span></button>
            </div>
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
            Supplies:
            {project?.supplies?.map((supply) => (
              <div key={supply?.id}>
                <li className="supply-list" >
                  <p>-</p>{supply?.supply}
                </li>
              </div>
            ))}
          </ul>
          {project?.instructions?.map((instruction) => (
            <div className="instruction-container" key={instruction?.id}>
              <div className="instruction-title">
                Step {instruction?.stepOrder}: {instruction?.stepTitle}
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
          <h2 className="num-comments">{project?.comments?.length} Comments</h2>
          {project?.comments?.map((comment) => (
            <div key={comment?.id}>
              <div className="comments" >
                <div className="user">
                  <div className="user-container">
                    <div className="userImg">
                      {/* {comment?.userId} */}
                      <UserPhoto userId={comment?.userId} />
                    </div>
                    <div className="username">
                      {comment?.username}
                    </div>
                  </div>
                  {user?.id === comment?.userId && (
                    <div className="comment-btn-container">
                      <button className="submit-commentt" id={comment?.id} onClick={handleDeleteComment}>Delete</button>
                      <button className="submit-commentt" id={comment?.id} onClick={handleShowEditForm(comment.id)}>Edit</button>
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
                    <div className="comment-">
                      <form className="comment-form" >
                        <div className="edit-container">
                          <div className="prf-image">
                            {/* hello */}
                            <img id="createCommnetUserPhoto" src={user.userPhoto}></img>
                          </div>
                          <div className="edit-comment">
                            <textarea
                              className="edit-input"
                              type="text"
                              value={editBody}
                              onChange={e =>
                                setEditBody(e?.target?.value)
                              }
                              required
                            />
                            <div className="btn-container">
                              <button onClick={cancel} className="cancel-edit" type="submit">Cancel</button>
                              <button onClick={saveEditComment} className="submit-comment" type="submit">Save</button>
                            </div>
                          </div>
                        </div>
                      </form>
                    </div>
                  )}
                </div>
              )}
              <div >
              </div>
            </div>
          )).reverse()}
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
          {!user && (
            <div className="not-logged-in">
              <div className="login-sign-up">
                <p>Want to leave a comment?</p>
                <button onClick={handleLogin} className="projectDetailsLogin">Login Here!</button>
              </div>
              <div className="login-sign-up">
                <p>Haven't signed up?</p>
                <button onClick={handleSignUp} className="projectDetailsLogin">Sign Up Here!</button>
              </div>
            </div>
          )}
          {showCommentForm && (
            <div className="comment-">
              <form className="comment-form" onSubmit={handleComment}>
                <div className="edit-container">
                  <div className="prf-image">
                    <img id="createCommnetUserPhoto" src={user.userPhoto}></img>
                  </div>
                  <div className="edit-comment">
                    <textarea
                      placeholder="Please Leave a Comment"
                      className="edit-input"
                      type="text"
                      value={body}
                      onChange={e =>
                        setBody(e?.target?.value)
                      }
                      required />
                    <div className="btn-container">
                      <button onClick={cancelNewComment} className="cancel-edit">Cancel</button>
                      <button className="submit-comment" type="submit">Save</button>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          )}
        </div>
      )}
    </>
  );
};

export default ProjectDetails;
