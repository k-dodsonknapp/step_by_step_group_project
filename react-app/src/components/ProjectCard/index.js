import React from "react";
import { NavLink } from "react-router-dom";
import FavoriteCount from "../FavoriteCount";
import ViewCount from "../ViewCount";
import "./projectCard.css";
import fallbackImage from "../../assets/images/Screenshot-2024-12-03-214059.png";

function ProjectCard({ projects, views }) {
  return (
    <>
      {projects
        .map(
          (project, index) =>
            index < 5 && (
              <div key={project.id} className="allProjectsMap">
                <li className="eachProject">
                  <NavLink to={`/projects/${project?.id}`}>
                    <div className="projectImage">
                      <img
                        src={`${project?.titleImage}`}
                        alt=""
                        onError={(e) => (e.target.src = fallbackImage)}
                      />
                    </div>
                  </NavLink>
                  <div className="info-container">
                    <div className="title-by">
                      <div>
                        <p className="title-card">
                          <span className="title-card-span">
                            <span className="project-title-span">
                              {project?.title}
                            </span>
                            <span className="by-span">by</span>
                            <NavLink
                              to={`/users/${project?.userId}`}
                              className="user-link"
                            >
                              {project?.username}
                            </NavLink>
                            <span className="in-span">in</span>
                            <NavLink
                              to={`/category/${project?.category}`}
                              className="category-link"
                            >
                              {project?.category}
                            </NavLink>
                          </span>
                        </p>
                      </div>
                      <div className="likes-views">
                        <FavoriteCount project={project} />
                        <ViewCount views={views} project={project} />
                      </div>
                    </div>
                  </div>
                </li>
              </div>
            )
        )
        .reverse()}
    </>
  );
}

export default ProjectCard;
