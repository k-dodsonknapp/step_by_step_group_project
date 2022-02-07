import React from "react";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useParams } from "react-router-dom"
import { getOneProject } from "../../store/project";

const ProjectDetails = () => {
    const dispatch = useDispatch()
    const { projectId } = useParams();

    useEffect(() => {
        dispatch(getOneProject(projectId))
    }, [dispatch, projectId])

    return (
        <h1>Hello from Project by id page</h1>
    )
}

export default ProjectDetails;
