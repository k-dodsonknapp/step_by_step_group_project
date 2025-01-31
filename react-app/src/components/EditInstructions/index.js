import { useState } from "react";
import UploadPicture from "../UploadPicture";

function EditInstructions({
  instructions,
  setInstructions,
  instruction,
  index,
}) {

  const [editedStepTitle, setEditedStepTitle] = useState(
    instructions[index]?.stepTitle
  );

  const [editedInstruction, setEditedInstruction] = useState(
    instructions[index]?.instructions
  );

  const [editedPhotoUrl, setEditedPhotoUrl] = useState(
    instructions[index].photoUrl
  );

  instructions[index].stepTitle = editedStepTitle;
  instructions[index].instructions = editedInstruction;
  instructions[index].photoUrl = editedPhotoUrl;
  setInstructions(instructions);

  return (
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
          <label>Step {instruction.stepOrder} Title: </label>
          <input
            type="text"
            name="stepTitle"
            value={editedStepTitle}
            onChange={(e) => setEditedStepTitle(e.target.value)}
          />
        </div>
        <div className="step-input">
          <label>Step {instruction.stepOrder} Instruction</label>
          <textarea
            type="text"
            name="stepInstructions"
            value={editedInstruction}
            onChange={(e) => setEditedInstruction(e.target.value)}
          ></textarea>
        </div>
        <div className="step-input">
          <label>Step {instruction.stepOrder} Photo</label>
          <UploadPicture setTitleImagee={setEditedPhotoUrl} />
        </div>
      </div>
    </div>
  );
}

export default EditInstructions;
