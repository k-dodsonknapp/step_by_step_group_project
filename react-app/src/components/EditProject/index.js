import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { getOneProject, updateOnePost } from "../../store/project";
// import EachSupply from "../EachSupply";
// import EditInstructions from "../EditInstructions";
import Instructions from "../Instructions";
import Supplies from "../Supplies";
import UploadPicture from "../UploadPicture";
import "./editProject.css";

function EditProject() {
  const userId = useSelector((state) => state?.session?.user["id"]);
  let { projectId } = useParams();
  projectId = parseInt(projectId);
  const project = useSelector((state) => state?.projects[projectId]);
  const dispatch = useDispatch();
  const history = useHistory();

  const [title, setTitle] = useState(project?.title);
  const [titleImage, setTitleImage] = useState(project?.titleImage);
  const [category, setCategory] = useState(project?.category);
  const [overview, setOverview] = useState(project?.overview);
  const [projectSupplies, setProjectSupplies] = useState(project?.supplies);

  // project instructions
  const [instructions, setInstructions] = useState(project?.instructions);

  useEffect(() => {
    dispatch(getOneProject(projectId));
  }, [dispatch, setTitle, projectId]);

  const handleEditProjectSubmit = async (e) => {
    e.preventDefault();
    const editedProject = {
      id: projectId,
      userId: userId,
      title: title,
      titleImage: titleImage,
      overview: overview,
      category: category,
      instructions: instructions,
      supplies: projectSupplies,
    };
    await dispatch(updateOnePost(editedProject));
    await dispatch(getOneProject(projectId));
    history.push(`/projects/${projectId}`);
  };

  return (
    <div className="editPage">
      <div className="edit-project-form">
        <form className="create-form" onSubmit={handleEditProjectSubmit}>
          <div className="label-input-container">
            <div className="submit-project">
              <button className="submitt-comment" type="submit">
                Submit your Project
              </button>
            </div>
            <div className="title-img-cat">
              <div className="titleImage-preview">
                <img
                  src={titleImage}
                  style={{ width: "310px", height: "245px", opacity: "0.6" }}
                  alt=""
                ></img>
              </div>
              <div className="title-category">
                <div className="project-title-input">
                  <h3>Edit the Basics</h3>
                  <label>Title:</label>
                  <input
                    type="text"
                    name="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                  ></input>
                </div>
                <div className="category-input">
                  <label>Category</label>
                  <select
                    name="category"
                    onChange={(e) => setCategory(e.target.value)}
                  >
                    <option value="Circuits">Circuits</option>
                    <option value="Workshop">Workshop</option>
                    <option value="Craft">Craft</option>
                    <option value="Cooking">Cooking</option>
                    <option value="Living">Living</option>
                    <option value="Outside">Outside</option>
                    <option value="Teachers">Teachers</option>
                  </select>
                </div>
                <div className="btn-div"></div>
                <div className="label-input">
                  <label>Image:</label>
                  {/* <input
                                        type="text"
                                        name="titleImage"
                                        value={titleImage}
                                        onChange={e => setTitleImage(e.target.value)}
                                    /> */}
                  <UploadPicture
                    className={"uploadPictureInput"}
                    setTitleImagee={setTitleImage}
                  />
                </div>
              </div>
            </div>
            <div className="title-img-cat">
              <div className="overview-input">
                <label>Overview</label>
                <input
                  type="text"
                  name="overview"
                  value={overview}
                  onChange={(e) => setOverview(e.target.value)}
                />
              </div>
            </div>
            <div className="edit-supply-cat">
              <div className="supply-input">
                <label>Supplies:</label>
                <Supplies
                  setProjectSupplies={setProjectSupplies}
                  project={project}
                  projectSupplies={projectSupplies}
                />
              </div>
            </div>
            <Instructions
              instructions={instructions}
              project={project}
              setInstructions={setInstructions}
            />
            {/* {project?.instructions?.map((instruction, i) => (
                            <EditInstructions
                                instructions={project?.instructions}
                                setInstructions={setInstructions}
                                instruction={instruction}
                                index={i} />
                        ))} */}
            {/* <div className="submit-project">
                            <button className="submitt-comment" type='submit'>Submit your Project</button>
                        </div> */}
          </div>
        </form>
        <div style={{ height: "100px" }}></div>
      </div>
    </div>
  );
}

export default EditProject;
