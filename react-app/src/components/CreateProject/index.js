import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { addOneProject } from "../../store/project";
import { useHistory } from "react-router-dom";
import "./createProject.css";
import UploadPicture from "../UploadPicture";
import { addNewProjectView } from "../../store/views";

const CreateProject = () => {
  const userId = useSelector((state) => state.session.user["id"]);
  const dispatch = useDispatch();
  const history = useHistory();

  // const [newProjectId, setNewProjectId] = useState()

  const [showErrors] = useState(false);
  const [errors, setErrors] = useState([]);
  const [title, setTitle] = useState("");
  const [overview, setOverview] = useState("");
  const [category, setCategory] = useState("");

  const [showSupplyErrors, setShowSupplyErrors] = useState(false);
  const [supplyErrors, setSupplyErrors] = useState([]);
  const [supplies, setSupplies] = useState([]);
  const [supply, setSupply] = useState("");
  const [amount] = useState(0);

  const [showInstructionErrors, setShowInstructionErrors] = useState(false);
  const [instructionErrors, setInstructionErrors] = useState([]);
  const [instructions, setInstructions] = useState([]);
  const [stepOrder, setStepOrder] = useState(1);
  const [stepTitle, setStepTitle] = useState("");
  const [stepInstructions, setStepInstructions] = useState("");
  const [photoUrl, setPhotoUrl] = useState(
    "https://www.elmhurst.edu/wp-content/uploads/2018/12/5-skills-project-management-degree-elmhurst-college-infographic-thumb.jpg"
  );
  const [videoUrl, setVideoUrl] = useState("");

  const [imagePreview, setImagePreview] = useState(
    "https://www.elmhurst.edu/wp-content/uploads/2018/12/5-skills-project-management-degree-elmhurst-college-infographic-thumb.jpg"
  );

  // useEffect(() => {
  //     // const newSupply = { supply, amount }
  //     setSupplies([...supplies, supply])
  // }, [setSupply])

  const handleProjectSubmit = async (e) => {
    e.preventDefault();
    // addAnotherStep(e)
    setSupplies([...supplies, supply]);
    // addSupply()
    if (instructionErrors.length === 0) {
      const newInstruction = {
        stepOrder,
        stepTitle,
        instructions: stepInstructions,
        photoUrl,
        videoUrl,
      };
      const project = {
        userId,
        title,
        titleImage: imagePreview,
        overview,
        category,
        supplies,
        instructions: [...instructions, newInstruction],
      };

      const data = await dispatch(addOneProject(project));
      const projectId = data?.projectId;

      const newView = {
        projectId: projectId,
        viewCount: 0,
      };
      dispatch(addNewProjectView(newView));
      history.push(`/projects/${projectId}`);
    } else {
      setShowInstructionErrors(true);
    }
  };

  useEffect(() => {
    const inFuncErrors = [];
    if (title.length < 6 || title === "") {
      inFuncErrors.push("Please provide a longer title");
    }
    if (overview.length < 10 || overview === "") {
      inFuncErrors.push("Please provide a longer overview");
    }
    setErrors(inFuncErrors);
  }, [title, overview, showErrors]);

  useEffect(() => {
    const inFuncErrors = [];
    if (supply.length < 3) {
      inFuncErrors.push("Please provide a supply name");
    }
    setSupplyErrors(inFuncErrors);
  }, [supply, showSupplyErrors]);

  useEffect(() => {
    const inFuncErrors = [];
    if (stepInstructions.length < 10) {
      inFuncErrors.push("Please provide more instructions");
    }
    if (stepTitle.length < 5) {
      inFuncErrors.push("Please provide a longer title");
    }
    setInstructionErrors(inFuncErrors);
  }, [stepTitle, stepInstructions, photoUrl, showInstructionErrors]);

  const addAnotherStep = (e) => {
    e.preventDefault();
    if (instructionErrors.length === 0) {
      const newInstruction = {
        stepOrder,
        stepTitle,
        instructions: stepInstructions,
        photoUrl,
        videoUrl,
      };
      setInstructions([...instructions, newInstruction]);
      setStepOrder(stepOrder + 1);
      setStepTitle("");
      setStepInstructions("");
      setPhotoUrl(
        "https://www.elmhurst.edu/wp-content/uploads/2018/12/5-skills-project-management-degree-elmhurst-college-infographic-thumb.jpg"
      );
      setVideoUrl("");
      setShowInstructionErrors(false);
    } else {
      setShowInstructionErrors(true);
    }
  };

  const addSupply = (e) => {
    e.preventDefault();
    if (supplyErrors.length === 0) {
      const newSupply = {
        supply,
        amount,
      };
      setSupplies([...supplies, newSupply]);
      setSupply("");
      setShowSupplyErrors(false);
    } else {
      setShowSupplyErrors(true);
    }
  };

  return (
    <div className="create-page">
      <div className="edit-project-form">
        <form className="create-form" onSubmit={handleProjectSubmit}>
          <div className="label-input-container">
            <div className="submit-project">
              <button className="submitt-comment" type="submit">
                Submit your Project
              </button>
            </div>
            <div className="title-img-cat">
              <div className="titleImage-preview">
                <img
                  src={imagePreview}
                  style={{ width: "310px", height: "245px", opacity: "0.6" }}
                  alt=""
                ></img>
              </div>
              <div className="title-category">
                <div className="project-title-input">
                  <h3>Layout the Basics</h3>
                  <label>Project Title</label>
                  <input
                    placeholder="Title?!  We need a title!"
                    type="text"
                    name="title"
                    value={title}
                    required="required"
                    onChange={(e) => setTitle(e.target.value)}
                    maxLength={150}
                  ></input>
                  <div className="char-count">{title.length}/150</div>
                </div>
                <div className="category-input">
                  <label>Category</label>
                  <select
                    name="category"
                    onChange={(e) => setCategory(e.target.value)}
                  >
                    <option style={{ display: "none", color: "gray" }}>
                      Select your option
                    </option>
                    <option value="Circuits">Circuits</option>
                    <option value="Workshop">Workshop</option>
                    <option value="Craft">Craft</option>
                    <option value="Cooking">Cooking</option>
                    <option value="Living">Living</option>
                    <option value="Outside">Outside</option>
                    <option value="Teachers">Teachers</option>
                  </select>
                </div>
                <div>
                  <UploadPicture setTitleImagee={setImagePreview} />
                </div>
              </div>
            </div>
            <div className="label-input"></div>
            <div className="title-img-cat">
              <div className="overview-input">
                <label>Overview</label>
                <input
                  placeholder="Tell us a bit about the project!"
                  type="text"
                  name="overview"
                  value={overview}
                  onChange={(e) => setOverview(e.target.value)}
                ></input>
              </div>
              <div></div>
            </div>
            <div className="supply-cat">
              {supplies.map((sup) => (
                <div key={sup.id} className="supply-input">
                  {/* <label>Supplies</label>  */}
                  <input
                    disabled={true}
                    placeholder="List a supply"
                    type="text"
                    name="supply"
                    value={sup.supply}
                    required
                    onChange={(e) => setSupply(e.target.value)}
                  ></input>
                </div>
              ))}
              {/* <button className="submitt-comment" onClick={addSupply}>add supply</button> */}
              <div className="supply-input">
                <label>Supply</label>
                <input
                  placeholder="Add supplies needed for this project"
                  type="text"
                  name="supply"
                  value={supply}
                  // required
                  onChange={(e) => setSupply(e.target.value)}
                ></input>
                {showSupplyErrors && (
                  <>
                    <ul>
                      {supplyErrors.map((error) => (
                        <li>{error}</li>
                      ))}
                    </ul>
                  </>
                )}
              </div>
            </div>
            <button className="submitt-comment" onClick={addSupply}>
              Add Supply
            </button>

            {instructions.map((instruction) => (
              <div key={instruction.id} className="title-img-catt">
                <div className="titleImage-preview">
                  <img
                    src={instruction.photoUrl}
                    style={{ width: "310px", height: "245px", opacity: "0.6" }}
                    alt=""
                  ></img>
                </div>
                <div>
                  <div className="step-title">
                    <label>Step {instruction.stepOrder}:</label>
                    <input
                      disabled={true}
                      placeholder="ENTER STEP TITLE"
                      type="text"
                      name="stepTitle"
                      value={instruction.stepTitle}
                      onChange={(e) => setStepTitle(e.target.value)}
                    ></input>
                  </div>
                  <div className="step-input">
                    <label>Step {instruction.stepOrder} Instructions</label>
                    <textarea
                      disabled={true}
                      type="text"
                      name="stepInstructions"
                      value={instruction.instructions}
                      onChange={(e) => setStepInstructions(e.target.value)}
                    ></textarea>
                  </div>
                  {/* <div className="step-input">
                                    </div> */}
                </div>
              </div>
            ))}
            <div className="title-img-catt">
              <div className="titleImage-preview">
                <img
                  src={photoUrl}
                  style={{ width: "310px", height: "245px", opacity: "0.6" }}
                  alt=""
                ></img>
              </div>
              <div>
                <div className="step-title">
                  <label>Step {stepOrder}:</label>
                  <input
                    placeholder="ENTER STEP TITLE"
                    type="text"
                    name="stepTitle"
                    value={stepTitle}
                    onChange={(e) => setStepTitle(e.target.value)}
                  ></input>
                </div>
                <div className="step-input">
                  <label>Step {stepOrder} Instructions</label>
                  <textarea
                    placeholder="Fill in the instructions for this step"
                    type="text"
                    name="stepInstructions"
                    value={stepInstructions}
                    onChange={(e) => setStepInstructions(e.target.value)}
                  ></textarea>
                </div>
                <h4 className="photo-header">Click to choose a photo</h4>
                <div className="step-photo">
                  <UploadPicture
                    className={"uploadPictureInput"}
                    setTitleImagee={setPhotoUrl}
                  />
                </div>
                {showInstructionErrors && (
                  <>
                    <ul>
                      {instructionErrors.map((error) => (
                        <li>{error}</li>
                      ))}
                    </ul>
                  </>
                )}
              </div>
            </div>
            <div className="create-btns">
              <div className="add-step-btn">
                <button className="submitt-comment" onClick={addAnotherStep}>
                  Add another Step
                </button>
              </div>
              <div className="submit-project-btn">
                <button className="submitt-comment" type="submit">
                  Submit your Project
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
      {showErrors && (
        <>
          <ul>
            {errors.map((error) => (
              <li key={error}>{error}</li>
            ))}
          </ul>
        </>
      )}
      {/* {showSupplyErrors &&
                <>
                    <ul>
                        {supplyErrors.map(error => (
                            <li>{error}</li>
                        ))}
                    </ul>
                </>
            } */}
    </div>
  );
};

export default CreateProject;
