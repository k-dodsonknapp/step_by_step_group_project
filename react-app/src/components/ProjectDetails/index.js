import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom"
import { getOneProject } from "../../store/project";
import './Projects.css'

const ProjectDetails = () => {
    const dispatch = useDispatch()
    const { projectId } = useParams();
    const project = useSelector(state => state.projects[projectId])
    console.log(project)

    useEffect(() => {
        dispatch(getOneProject(projectId))
    }, [dispatch, projectId])

    return (
        <>
            {project &&
                <>
                    {/* <h1>Hello from Project by id page</h1> */}
                    <div class='title'>{project.title}</div>
                    <div id='project-details'>By
                        <span className='username-category'>{project.owner.username}</span>
                        in<span className='username-category'>{project.category}</span>
                    </div>
                    <div className="project-image-container">
                        <img classname='project-images'src={project.titleImage} alt='Completed project'></img>
                    </div>
                    <div id='overview-container'>
                        <div id='overview-title'>Project Overview:
                            <p id='project-overview'>{project.overview}</p>
                        </div>
                    </div>
                    <ul>
                        {project.instructions.map((instruction) => (
                            <li key={instruction.id}>{instruction.instructions}</li>
                        ))}
                    </ul>
                </>
            }
        </>
    )
}

export default ProjectDetails;
