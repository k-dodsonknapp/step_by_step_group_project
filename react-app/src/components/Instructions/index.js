import React, { useEffect, useState } from "react";
import EditInstructions from "../EditInstructions";
import UploadPicture from "../UploadPicture";

function Instructions({ instructions, setInstructions }) {
  // const [sortedInstructions, setSortedInstructions] = useState(instructions.sort((a, b) => a.stepOrder - b.stepOrder))
  const [showInstructionErrors, setShowInstructionErrors] = useState(false);
  const [instructionErrors, setInstructionErrors] = useState([]);
  // const [instructions, setInstructions] = useState([])
  const [stepOrder, setStepOrder] = useState(instructions.length + 1);
  const [stepTitle, setStepTitle] = useState("");
  const [stepInstructions, setStepInstructions] = useState("");
  const [photoUrl, setPhotoUrl] = useState(
    "https://www.elmhurst.edu/wp-content/uploads/2018/12/5-skills-project-management-degree-elmhurst-college-infographic-thumb.jpg"
  );
  const [videoUrl, setVideoUrl] = useState("");

  // const [imagePreview, setImagePreview] = useState('https://www.elmhurst.edu/wp-content/uploads/2018/12/5-skills-project-management-degree-elmhurst-college-infographic-thumb.jpg')

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

  return (
    <>
      {instructions?.map((instruction, i) => (
        <EditInstructions
          instructions={instructions}
          setInstructions={setInstructions}
          instruction={instruction}
          index={i}
        />
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
      <div className="edit-submit-project">
        <button className="submitt-comment" onClick={addAnotherStep}>
          Add Step
        </button>
        <button className="submitt-comment" type="submit">
          Submit your Project
        </button>
      </div>
    </>
  );
}

export default Instructions;
