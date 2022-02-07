import React from "react";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { getAllProjects } from "../../store/project";

const ProjectExplore = () => {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllProjects())
    }, [dispatch])

    return (
        <h1>Hello Project Explore page</h1>
    )
}

export default ProjectExplore;
