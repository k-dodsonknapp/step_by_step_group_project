import React from "react";
import { NavLink } from "react-router-dom"
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjects } from "../../store/project";
import './projectExplore.css'


const ProjectExplore = () => {
    const dispatch = useDispatch()
    const projects = useSelector(state => Object.values(state.projects))
    // const session = useSelector(state => session.user)
    const [users, setUsers] = useState([])

    console.log("USERS", users)

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

    // console.log(users)
    const username = (id) => {
        const name = users.map(user => {
            if (id === user.id) {
                return user.username
            }
        })
        return name
    }
    console.log("USERNAME", username(1))

    return (
        // {}
        <div className="explorePage">
            <h1>Hello Project Explore page</h1>
            <ul>
                {projects?.map(project => (
                    <div className="allProjectsMap" key={project.id}>
                        <li className="eachProject">
                            <p>{project?.title}</p>
                            <div>
                                <p>by <NavLink to={`/users`}>{username(project.userId)}</NavLink> in {project?.category}</p>
                            </div>
                            <div>
                                <img src={`${project.titleImage}`} />
                            </div>
                        </li>
                    </div>
                ))}
            </ul>
        </div>
    )
}

export default ProjectExplore;
