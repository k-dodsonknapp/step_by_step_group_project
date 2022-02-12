import React from "react";
import { NavLink } from "react-router-dom"
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjects } from "../../store/project";
import './projectExplore.css'


const ProjectExplore = () => {
    const dispatch = useDispatch()
    const projects = useSelector(state => Object.values(state.projects))
    const [users, setUsers] = useState([])

    useEffect(() => {
        async function usersData() {
            const res = await fetch('/api/users/');
            const resData = await res.json();
            setUsers(resData.users);
        }
        usersData();
    }, [])

    useEffect(() => {
        dispatch(getAllProjects())
    }, [dispatch])

    const username = (id) => {
        const name = users.map(user => {
            if (id === user.id) {
                return user.username
            }
        })
        return name
    }
    return (
        <div className="explorePage">
            <div className="slideshow-container">
                <img src="https://media.istockphoto.com/photos/colorful-background-of-pastel-powder-explosionrainbow-color-dust-on-picture-id1180542165?k=20&m=1180542165&s=612x612&w=0&h=43hlhk8qdGYP4V-u3AAxD3kPDRIzHjMNWpr-VdBQ2Js="></img>
            </div>
            <ul>
                {projects?.map(project => (
                    <div className="allProjectsMap" key={project.id}>
                        <li className="eachProject">
                            <div className="projectImage">
                                <img src={`${project.titleImage}`} />
                            </div>
                            <div className="info-container">
                                <div className="title-by">
                                    <div>
                                        <p>{project?.title} by <NavLink to={`/users/${project.userId}`}>
                                            {project.username}
                                        </NavLink>  in <NavLink to={`/category/${project.category}`}>
                                                {project?.category}
                                            </NavLink>
                                        </p>
                                    </div>
                                    <div className="likes-views">
                                        <p>❤ 5  👁 105</p>
                                    </div>
                                </div>
                            </div>
                        </li>
                    </div>
                ))}
            </ul>
        </div >
    )
}

export default ProjectExplore;
