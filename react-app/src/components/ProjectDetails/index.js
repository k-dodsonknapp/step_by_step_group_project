import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom"
import { getOneProject } from "../../store/project";

const ProjectDetails = () => {
    const dispatch = useDispatch()
    const { projectId } = useParams();
    const project = useSelector(state => state.projects[projectId])
    console.log('project:', project)
    useEffect(() => {
        dispatch(getOneProject(projectId))
    }, [])

    return (
        <>
            {project &&
                <>
                    <h1>Hello from Project by id page</h1>
                    <div>{project.title}</div>
                    <div>{project.owner.username}</div>
                    <ul>
                        {project.instructions.map((instruction) => (
                            // console.log('------',instruction.instructions)
                            <li>{instruction.instructions}</li>
                        ))}
                    </ul>
                </>
            }
        </>
    )
}

export default ProjectDetails;
