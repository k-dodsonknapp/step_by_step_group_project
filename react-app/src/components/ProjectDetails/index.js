import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom"
import { getOneProject } from "../../store/project";
import { addOneComment } from "../../store/comments";
import './Projects.css'

const ProjectDetails = () => {
    const dispatch = useDispatch()
    const { projectId } = useParams();
    const project = useSelector(state => state.projects[projectId])
    const user = useSelector(state => state.session.user)
    const commentState = useSelector(state => state.comments)
    console.log(user.id)

    const [showCommentForm, setShowCommentForm] = useState(false)
    const [showCommentEditForm, setShowCommentEditForm] = useState(false)
    const [comment, setComment] = useState('')

    useEffect(() => {
        dispatch(getOneProject(projectId))
    }, [dispatch, projectId])

    const handleComment = (e) => {
        e.preventDefault()

        const newComment = { 'userId': user.id, projectId, comment }
        dispatch(addOneComment(newComment))
    }

    const handleDelete = (e) => {
        e.preverntDefault()


    }

    useEffect(() => {
        console.log(commentState)
    }, [commentState])

    return (
        <>
            {project &&
                <div id='project-container'>
                    <div className='title'>{project.title}</div>
                    <div id='project-details'>By
                        <span className='username-category'>{project.owner.username}</span>
                        in<span className='username-category'>{project.category}</span>
                        {user &&
                            <div>
                                <button>
                                    Edit
                                </button>
                            </div>
                        }
                    </div>
                    <div className="project-image-container">
                        <img className='project-images' src={project.titleImage} alt='Completed project'></img>
                    </div>
                    <div id='overview-title'>Project Overview:
                        <p id='project-overview'>{project.overview}</p>
                    </div>
                    <ul id='supplies-title'>Supplies Needed:
                        {project.supplies.map((supply) => (
                            <>
                                <li className='supply-list' key={supply.id}>{supply.supply}</li>
                            </>
                        ))}

                    </ul>
                    <ul>
                        {project.instructions.map((instruction) => (
                            <div className="instruction-container">
                                <div className='instruction-title'>Step {instruction.stepOrder}:</div>
                                <div className='project-image-container'>
                                    <img
                                        className="instruction-image"
                                        key={instruction.id}
                                        src={instruction.photoUrl}
                                        alt={`Step ${instruction.stepOrder}`}>
                                    </img>
                                </div>
                                <li className='instructions' key={instruction.id}>{instruction.instructions}</li>
                            </div>
                        ))}
                    </ul>
                    {showCommentForm &&
                        <form onSubmit={handleComment}>
                            <label>Leave a comment here:</label>
                            <textarea
                                type='text'
                                onChange={(e) => setComment(e.target.value)}
                                value={comment}
                            ></textarea>
                            <button type='submit'>Submit Comment</button>
                        </form>
                    }
                    <ul id='comments-title'>Comments:
                        {user &&
                            <button id='leave-comment-btn' onClick={(e) => setShowCommentForm(true)}>Leave a comment</button>
                        }
                        {project.comments.map((comment) => (
                            <>
                                <li className='comments' key={comment.id}>{comment.comment}</li>
                                {user.id == comment.userId &&
                                    <div className="comment-btn-container">
                                        <button onClick={(e) => setShowCommentEditForm(true)}>Edit</button>
                                        <button onClick={handleDelete}>Delete</button>
                                    </div>
                                }
                            </>
                        ))}
                    </ul>
                </div>
            }
        </>
    )
}

export default ProjectDetails;
