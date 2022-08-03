import React, { useState } from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjects } from "../../store/project";
import './projectExplore.css';
import { getView } from "../../store/views";
import ProjectCard from "../ProjectCard";
import { getAllFavorites } from "../../store/favortie";
import Carousel, { CarouselItem } from "../Carousel";
import { NavLink } from "react-router-dom";


const ProjectExplore = () => {

    const dispatch = useDispatch();
    const circuits = useSelector(state => Object.values(state.projects).filter(project => project.category === "Circuits"))
    const workshop = useSelector(state => Object.values(state.projects).filter(project => project.category === "Workshop"))
    const craft = useSelector(state => Object.values(state.projects).filter(project => project.category === "Craft"))
    const cooking = useSelector(state => Object.values(state.projects).filter(project => project.category === "Cooking"))
    const living = useSelector(state => Object.values(state.projects).filter(project => project.category === "Living"))
    const outside = useSelector(state => Object.values(state.projects).filter(project => project.category === "Outside"))
    const teachers = useSelector(state => Object.values(state.projects).filter(project => project.category === "Teachers"))
    const views = useSelector(state => state.views.views);
    // const favorties = useSelector(state => state?.favorites)
    const projects = useSelector(state => Object.values(state.projects))
    const numOfProjects = projects.length - 1;
    const [carouselItem1, setCarouselItem1] = useState(projects)
    const [carouselItem2, setCarouselItem2] = useState(projects)
    const [carouselItem3, setCarouselItem3] = useState(projects)
    const [carouselItem4, setCarouselItem4] = useState(projects)
    const [carouselItem5, setCarouselItem5] = useState(projects)
    // console.log(carouselItem1)

    useEffect(() => {
        const getRandomInt = (numOfProjects => {
            return Math.floor(Math.random() * numOfProjects);
        })
        setCarouselItem1(projects[getRandomInt(numOfProjects)])
        setCarouselItem2(projects[getRandomInt(numOfProjects)])
        setCarouselItem3(projects[getRandomInt(numOfProjects)])
        setCarouselItem4(projects[getRandomInt(numOfProjects)])
        setCarouselItem5(projects[getRandomInt(numOfProjects)])
    }, [numOfProjects])

    // console.log(numOfProjects)

    useEffect(() => {
        dispatch(getAllProjects());
        dispatch(getView());
        dispatch(getAllFavorites())
    }, [dispatch]);


    return (
        <div className="explorePage">
            {/* <div className="carousel-div"> */}

            <Carousel>
                <CarouselItem carouselItem={carouselItem1}>
                    <img className="carousel-img" src={carouselItem1?.titleImage}></img>
                    <h1 className='carousel-project-title'>
                        <NavLink className="link" to={`/projects/${carouselItem1?.id}`} >{carouselItem1?.title} </NavLink>
                    </h1>                    
                    <h4 className='carousel-project-username'>By: {carouselItem1?.username} </h4>
                </CarouselItem>
                <CarouselItem carouselItem2={carouselItem2}>
                    <img className="carousel-img" src={carouselItem2?.titleImage}></img>
                    <h1 className='carousel-project-title'>
                        <NavLink className="link" to={`/projects/${carouselItem2?.id}`} >{carouselItem2?.title} </NavLink>
                    </h1>
                    <h4 className='carousel-project-username'>By: {carouselItem2?.username} </h4>
                </CarouselItem>
                <CarouselItem carouselItem3={carouselItem3}>
                    <img className="carousel-img" src={carouselItem3?.titleImage}></img>
                    <h1 className='carousel-project-title'>
                        <NavLink className="link" to={`/projects/${carouselItem3?.id}`} >{carouselItem3?.title} </NavLink>
                    </h1>
                    <h4 className='carousel-project-username'>By: {carouselItem3?.username} </h4>
                </CarouselItem>
                <CarouselItem carouselItem4={carouselItem4}>
                    <img className="carousel-img" src={carouselItem4?.titleImage}></img>
                    <h1 className='carousel-project-title'>
                        <NavLink className="link" to={`/projects/${carouselItem4?.id}`} >{carouselItem4?.title} </NavLink>
                    </h1>
                    <h4 className='carousel-project-username'>By: {carouselItem4?.username} </h4>
                </CarouselItem>
                <CarouselItem carouselItem5={carouselItem5}>
                    <img className="carousel-img" src={carouselItem5?.titleImage}></img>
                    <h1 className='carousel-project-title'>
                        <NavLink className="link" to={`/projects/${carouselItem5?.id}`} >{carouselItem5?.title} </NavLink>
                    </h1>
                    <h4 className='carousel-project-username'>By: {carouselItem5?.username} </h4>
                </CarouselItem>
            </Carousel>
            {/* </div> */}
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
            <ul className="project-list">
                {/* <div id="explore-sign">
                    <h2>{explore}</h2>
                </div> */}
                <h2>
                    {"Circuits >"}
                </h2>
                <div id="explore-sign">
                    <ProjectCard projects={circuits} views={views} />
                </div>
                <h2>
                    {"Workshop >"}
                </h2>
                <div id="explore-sign">
                    <ProjectCard projects={workshop} views={views} />
                </div>
                <h2>
                    {"Craft >"}
                </h2>
                <div id="explore-sign">
                    <ProjectCard projects={craft} views={views} />
                </div>
                <h2>
                    {"Cooking >"}
                </h2>
                <div id="explore-sign">
                    <ProjectCard projects={cooking} views={views} />
                </div>
                <h2>
                    {"Living >"}
                </h2>
                <div id="explore-sign">
                    <ProjectCard projects={living} views={views} />
                </div>
                <h2>
                    {"Outside >"}
                </h2>
                <div id="explore-sign">
                    <ProjectCard projects={outside} views={views} />
                </div>
                <h2>
                    {"Teachers >"}
                </h2>
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
