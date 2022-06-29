import React from 'react'
import { useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom'
import ViewCount from '../ViewCount'

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
                                    <p>{project?.title} by <NavLink to={`/users/${project?.userId}`}>
                                        {project?.username}
                                    </NavLink> in <NavLink to={`/category/${project?.category}`}>
                                            {project?.category}
                                        </NavLink>
                                    </p>
                                </div>
                                <div className="likes-views">
                                    <ViewCount views={views} project={project} />
                                    {/* {views.map(view => (
                                view.viewCount
                    ))

                }
                    <p>❤ 5  👁 105</p> */}
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