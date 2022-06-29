import React from "react";
import { NavLink } from "react-router-dom";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjects } from "../../store/project";
import './projectExplore.css';
import { getView } from "../../store/views";
import ViewCount from "../ViewCount";
import ProjectCard from "../ProjectCard";


const ProjectExplore = () => {

    const dispatch = useDispatch();
    // const projects = useSelector(state => Object?.values(state?.projects));
    const circuits = useSelector(state => Object.values(state.projects).filter(project => project.category === "Circuits"))
    const workshop = useSelector(state => Object.values(state.projects).filter(project => project.category === "Workshop"))
    const craft = useSelector(state => Object.values(state.projects).filter(project => project.category === "Craft"))
    const cooking = useSelector(state => Object.values(state.projects).filter(project => project.category === "Cooking"))
    const living = useSelector(state => Object.values(state.projects).filter(project => project.category === "Living"))
    const outside = useSelector(state => Object.values(state.projects).filter(project => project.category === "Outside"))
    const teachers = useSelector(state => Object.values(state.projects).filter(project => project.category === "Teachers"))
    const views = useSelector(state => state.views.views);
    const explore = "Explore >";

    useEffect(() => {
        dispatch(getAllProjects());
        dispatch(getView());
    }, [dispatch]);


    return (
        <div className="explorePage">
            <div className="slideshow-container">
                <img src="https://media.istockphoto.com/photos/colorful-background-of-pastel-powder-explosionrainbow-color-dust-on-picture-id1180542165?k=20&m=1180542165&s=612x612&w=0&h=43hlhk8qdGYP4V-u3AAxD3kPDRIzHjMNWpr-VdBQ2Js=" alt=""></img>
            </div>
            <div className="content-container">
                <div className="content">
                    <h2>Instructions STEP-BY-STEP</h2>
                    <p>
                        We make it easy to learn how to make anything, one step at a time. From the stovetop to the workshop, you are sure to be inspired by the awesome projects that are shared everyday.
                    </p>
                </div>
                <div className="content">
                    <h2>MADE by THE COMMUNITY </h2>
                    <p>
                        Step-by-Steps are created by you. No matter who you are, we all have secret skills to share. Come join our community of curious makers, innovators, teachers, and life long learners who love to share what they make.
                    </p>
                </div>
                <div id="place" className="content">
                    <h2>A PLACE</h2>
                    <p>
                        Making things. We can't prove it, but we know it to be true. Find your place, and join one of the friendliest online communities anywhere.
                    </p>
                </div>
            </div>
            <ul>
                {/* <div id="explore-sign">
                    <h2>{explore}</h2>
                </div> */}
                <h2>{"Circuits >"}</h2>
                <div id="explore-sign">
                    <ProjectCard projects={circuits} views={views} />
                </div>
                <h2>{"Workshop >"}</h2>
                <div id="explore-sign">
                    <ProjectCard projects={workshop} views={views} />
                </div>
                <h2>{"Craft >"}</h2>
                <div id="explore-sign">
                    <ProjectCard projects={craft} views={views} />
                </div>
                <h2>{"Cooking >"}</h2>
                <div id="explore-sign">
                    <ProjectCard projects={cooking} views={views} />
                </div>
                <h2>{"Living >"}</h2>
                <div id="explore-sign">
                    <ProjectCard projects={living} views={views} />
                </div>
                <h2>{"Outside >"}</h2>
                <div id="explore-sign">
                    <ProjectCard projects={outside} views={views} />
                </div>
                <h2>{"Teachers >"}</h2>
                <div id="explore-sign">
                    <ProjectCard projects={teachers} views={views} />
                </div>
                {/* {projects?.map(project => ( */}
                {/* // <div key={project.id} className="allProjectsMap">
                    //     <li className="eachProject">
                    //         <a href={`/projects/${project?.id}`}>
                    //             <div className="projectImage">
                    //                 <img src={`${project?.titleImage}`} alt="" />
                    //             </div>
                    //         </a>
                    //         <div className="info-container">
                    //             <div className="title-by">
                    //                 <div>
                    //                     <p>{project?.title} by <NavLink to={`/users/${project?.userId}`}>
                    //                         {project?.username}
                    //                     </NavLink> in <NavLink to={`/category/${project?.category}`}>
                    //                             {project?.category}
                    //                     </NavLink>
                    //                     </p>
                    //                 </div>
                    //                 <div className="likes-views">
                    //                     <ViewCount views={views} project={project} />
                    //                     {/* {views.map(view => (
                    //                         view.viewCount
                    //                     ))

                    //                     }
                    //                     <p>❤ 5  👁 105</p> 
                    //                 </div>
                    //             </div>
                    //         </div>
                    //     </li>
                 // </div> */}
                {/* ))}  */}
            </ul>
        </div >
    )
}

export default ProjectExplore;
