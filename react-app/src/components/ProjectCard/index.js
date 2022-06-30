import React from 'react'
import { useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom'
import ViewCount from '../ViewCount'
import "./projectCard.css"

function ProjectCard({ projects, views }) {

    return (
        <>
            {projects.map(project => (
                <div key={project.id} className="allProjectsMap">
                    <li className="eachProject">
                        <a href={`/projects/${project?.id}`}>
                            <div className="projectImage">
                                <img src={`${project?.titleImage}`} alt="" />
                            </div>
                        </a>
                        <div className="info-container">
                            <div className="title-by">
                                <div>
                                    <p className='title-card'>
                                        <span className='title-card-span'>
                                            <span className='project-title-span'>
                                                {project?.title}
                                            </span>
                                            <span className='by-span'>
                                                by
                                            </span>
                                                <NavLink to={`/users/${project?.userId}`} className='user-link'>
                                                    {project?.username}
                                                </NavLink>
                                            <span className='in-span'>
                                            in
                                            </span>
                                            <NavLink to={`/category/${project?.category}`} className="category-link">
                                                {project?.category}
                                            </NavLink>
                                        </span>
                                    </p>
                                </div>
                                <div className="likes-views">
                                    <ViewCount views={views} project={project}/>
                                </div>
                            </div>
                        </div>
                    </li>
                </div>

            ))}
        </>
    )
}

export default ProjectCard