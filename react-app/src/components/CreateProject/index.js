
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { addOneProject } from "../../store/project";
import { useHistory } from "react-router-dom";
import "./createProject.css"
import UploadPicture from "../UploadPicture";

const CreateProject = () => {
    const userId = useSelector(state => state.session.user['id'])
    const dispatch = useDispatch()
    const history = useHistory()

    const [showErrors, setShowErrors] = useState(false)
    const [errors, setErrors] = useState([])
    const [title, setTitle] = useState('')
    const [titleImage, setTitleImage] = useState('')
    console.log("DDDDDDD", titleImage)
    const [overview, setOverview] = useState('')
    const [category, setCategory] = useState('')

    const [showSupplyErrors, setShowSupplyErrors] = useState(false)
    const [supplyErrors, setSupplyErrors] = useState([])
    const [supplies, setSupplies] = useState([])
    console.log(supplies, "GGGGGGGGGGGGGGG")
    const [supply, setSupply] = useState('')
    console.log(supply, "LLLLLLLLLLLLLLLL")
    const [amount, setAmount] = useState(0)

    const [showInstructionErrors, setShowInstructionErrors] = useState(false)
    const [instructionErrors, setInstructionErrors] = useState([])
    const [instructions, setInstructions] = useState([])
    // console.log(instructions, "YYYYYYYYYYYYYYYY")
    const [stepOrder, setStepOrder] = useState(1)
    const [stepTitle, setStepTitle] = useState('')
    const [stepInstructions, setStepInstructions] = useState('')
    const [photoUrl, setPhotoUrl] = useState('')
    const [videoUrl, setVideoUrl] = useState('')

    const [showProjectForm, setShowProjectForm] = useState(true)
    const [showSupplyForm, setShowSupplyForm] = useState(false)
    const [showInstructionForm, setShowInstructionForm] = useState(false)
    const [imagePreview, setImagePreview] = useState('https://www.elmhurst.edu/wp-content/uploads/2018/12/5-skills-project-management-degree-elmhurst-college-infographic-thumb.jpg')
    // const [showEmptyFields, setShowEmptyFields] = useState(false)

    useEffect(() => {
        const newSupply = { supply, amount }
        console.log("FFFFFFFFFFF", newSupply)
        setSupplies([newSupply])
    }, [supply])

    const handleProjectSubmit = async (e) => {
        e.preventDefault()
        addAnotherStep(e)
        // if (supplyErrors.length === 0) {
        // const newSupply = { supply }
        // console.log("FFFFFFFFFFF", newSupply)
        // setSupplies([newSupply])
        // }
        if (instructionErrors.length === 0) {
            const newInstruction = {
                stepOrder,
                stepTitle,
                'instructions': stepInstructions,
                photoUrl,
                videoUrl
            }
            const project = {
                userId,
                title,
                'titleImage': imagePreview,
                overview,
                category,
                supplies,
                'instructions': [
                    ...instructions,
                    newInstruction
                ],
            }
            const data = await dispatch(addOneProject(project))
            const projectId = data.projectId
            history.push(`/projects/${projectId}`)
        } else {
            setShowInstructionErrors(true)
        }
    }

    useEffect(() => {
        const inFuncErrors = []
        if (title.length < 6 || title === '') {
            inFuncErrors.push('Please provide a longer title')
        }
        // if (!(titleImage.includes('.png') || titleImage.includes('.jpg') || titleImage.includes('.jpeg')) || titleImage === '') {
        //     inFuncErrors.push('Please use .png, .jpg, or .jpeg file type')
        // }
        if (overview.length < 20 || overview === '') {
            inFuncErrors.push('Please provide a longer overview')
        }
        setErrors(inFuncErrors)
    }, [title, titleImage, overview, showErrors])

    useEffect(() => {
        const inFuncErrors = []
        if (supply.length < 3) {
            inFuncErrors.push('Please provide a longer supply name')
        }
        setSupplyErrors(inFuncErrors)
    }, [supply, showSupplyErrors])

    useEffect(() => {
        const inFuncErrors = []
        if (stepInstructions.length < 10) {
            inFuncErrors.push('Please provide more instructions')
        }
        if (stepTitle.length < 5) {
            inFuncErrors.push('Please provide a longer title')
        }
        // if (!(photoUrl.includes('.png') || photoUrl.includes('.jpg') || photoUrl.includes('.jpeg'))) {
        //     inFuncErrors.push('Please use .png, .jpg, or .jpeg file type')
        // }
        setInstructionErrors(inFuncErrors)
    }, [stepTitle, stepInstructions, photoUrl, showInstructionErrors])

    // const moveOntoSupplies = (e) => {
    //     e.preventDefault()
    //     console.log(errors)
    //     if (errors.length > 0 || title === '' || overview === '') {
    //         setShowErrors(true)
    //     } else {
    //         setShowProjectForm(false)
    //         setShowSupplyForm(true)
    //         setShowErrors(false)
    //     }
    // }

    const addMoreSupplies = (e) => {
        e.preventDefault()
        if (supplyErrors.length === 0) {
            const newSupply = { supply, amount }
            setSupplies([...supplies, newSupply])
            setSupply('')
            setAmount(0)
            setShowSupplyErrors(false)
        } else {
            setShowSupplyErrors(true)
        }
    }

    // const moveOnToInstructions = (e) => {
    //     addMoreSupplies(e)
    //     if (supplyErrors.length === 0) {
    //         setShowSupplyForm(false)
    //         setShowInstructionForm(true)
    //     }
    // }

    const addAnotherStep = (e) => {
        e.preventDefault()
        if (instructionErrors.length === 0) {

            const newInstruction = {
                stepOrder,
                stepTitle,
                'instructions': stepInstructions,
                photoUrl,
                videoUrl
            }
            setInstructions([...instructions, newInstruction])
            setStepOrder(stepOrder + 1)
            setStepTitle('')
            setStepInstructions('')
            setPhotoUrl('')
            setVideoUrl('')
            setShowInstructionErrors(false)
        } else {
            setShowInstructionErrors(true)
        }
    }

    return (
        <div className="create-page">
            <div className="edit-project-form">
                {showProjectForm && (
                    <form className="create-form" onSubmit={handleProjectSubmit}>
                        <div className="label-input-container">
                            <div className="submit-project">
                                <button className="submitt-comment" type='submit'>Submit your Project</button>
                            </div>
                            <div className="title-img-cat">
                                <div className="titleImage-preview">
                                    <img src={imagePreview} style={{ width: '310px', height: '245px', opacity: "0.6" }}></img>
                                </div>
                                <div className="title-category">
                                    <div className="project-title-input">
                                        <h3>Layout the Basics</h3>
                                        <label>Project Title</label>
                                        <input
                                            placeholder="Title?!  We need a title!"
                                            type='text'
                                            name='title'
                                            value={title}
                                            required="required"
                                            onChange={(e) => setTitle(e.target.value)}
                                            maxLength={150}
                                        ></input>
                                        <div className="char-count">{title.length}/150</div>
                                    </div>
                                    <div className="category-input">
                                        <label>Category</label>
                                        {/* <div className="dropdown-cat"> */}
                                        <select name='category' onChange={(e) => setCategory(e.target.value)}>
                                            <option style={{ display: "none", color: "gray" }}>Select your option</option>
                                            <option value='Circuits'>Circuits</option>
                                            <option value='Workshop'>Workshop</option>
                                            <option value='Craft'>Craft</option>
                                            <option value='Cooking'>Cooking</option>
                                            <option value='Living'>Living</option>
                                            <option value='Outside'>Outside</option>
                                            <option value='Teachers'>Teachers</option>
                                        </select>
                                        {/* </div> */}
                                    </div>
                                    <div>
                                        <UploadPicture setTitleImagee={setImagePreview} />
                                    </div>
                                </div>
                            </div>
                            <div className="label-input">
                                {/* <label>Image:</label>
                                <input
                                    type='text'
                                    name='titleImage'
                                    value={titleImage}
                                    onChange={(e) => setTitleImage(e.target.value)}
                                ></input> */}
                            </div>
                            <div className="title-img-cat">
                                {/* <div className="titleImage-preview">
                                    <img src={imagePreview} style={{ width: '310px', height: '245px', opacity: "0.4" }}></img>
                                </div> */}
                                <div className="overview-input">
                                    <label>Overview</label>
                                    <input
                                        placeholder="Tell us a bit about the project!"
                                        type='text'
                                        name='overview'
                                        value={overview}
                                        onChange={(e) => setOverview(e.target.value)}
                                    ></input>
                                </div>
                                <div>
                                    {/* <UploadPicture setTitleImagee={setTitleImage}/> */}
                                </div>
                            </div>
                            <div className="title-img-cat">
                                <div className="supply-input">
                                    <label>Supplies</label>
                                    <input
                                        placeholder="List all supplies needed for this project"
                                        type='text'
                                        name='supply'
                                        value={supply}
                                        required
                                        onChange={(e) => setSupply(e.target.value)}
                                    ></input>
                                </div>
                            </div>

                            {instructions.map(instruction => (
                                <div className="title-img-catt">
                                    <div className="titleImage-preview">
                                        <img src={instruction.photoUrl} style={{ width: '310px', height: '245px', opacity: "0.6" }}></img>
                                    </div>
                                    <div>
                                        <div className="step-title">
                                            <label>Step {instruction.stepOrder}:</label>
                                            <input
                                                disabled={true}
                                                placeholder="ENTER STEP TITLE"
                                                type='text'
                                                name='stepTitle'
                                                value={instruction.stepTitle}
                                                onChange={(e) => setStepTitle(e.target.value)}
                                            ></input>
                                        </div>
                                        <div className="step-input">
                                            <label>Step {instruction.stepOrder} Instructions</label>
                                            <textarea
                                                disabled={true}
                                                type='text'
                                                name='stepInstructions'
                                                value={instruction.instructions}
                                                onChange={(e) => setStepInstructions(e.target.value)}
                                            ></textarea>
                                        </div>
                                        <div className="step-input">
                                            {/* <UploadPicture setTitleImagee={setPhotoUrl} /> */}
                                        </div>
                                    </div>
                                    {/* <div className="step-input">
                                <label>Step {stepOrder} Video</label>
                                <input
                                type='text'
                                    name='videoUrl'
                                    value={videoUrl}
                                    onChange={(e) => setVideoUrl(e.target.value)}
                                    ></input>
                                </div> */}
                                    {/* <button className="submit-comment" type='submit'>Submit your Project</button> */}
                                </div>
                            ))}
                            {/* <button className="submit-comment" type='submit' onClick={moveOntoSupplies}>Move on to Supplies</button> */}
                            <div className="title-img-catt">
                                <div className="titleImage-preview">
                                    <img src={photoUrl} style={{ width: '310px', height: '245px', opacity: "0.6" }}></img>
                                </div>
                                <div>
                                    <div className="step-title">
                                        <label>Step {stepOrder}:</label>
                                        <input
                                            placeholder="ENTER STEP TITLE"
                                            type='text'
                                            name='stepTitle'
                                            value={stepTitle}
                                            onChange={(e) => setStepTitle(e.target.value)}
                                        ></input>
                                    </div>
                                    <div className="step-input">
                                        <label>Step {stepOrder} Instructions</label>
                                        <textarea
                                            placeholder="Fill in the instructions for this step"
                                            type='text'
                                            name='stepInstructions'
                                            value={stepInstructions}
                                            onChange={(e) => setStepInstructions(e.target.value)}
                                        ></textarea>
                                    </div>
                                    <h4 className="photo-header">Click to choose a photo</h4>
                                    <div className="step-photo">
                                        <UploadPicture className="step-photo" setTitleImagee={setPhotoUrl} />
                                    </div>
                                    {/* <div className="step-input">
                                <label>Step {stepOrder} Video</label>
                                <input
                                type='text'
                                name='videoUrl'
                                value={videoUrl}
                                onChange={(e) => setVideoUrl(e.target.value)}
                                ></input>
                            </div> */}
                                    {/* <button className="submit-comment" type='submit'>Submit your Project</button> */}
                                </div>
                            </div>
                            <div className="create-btns">
                                <div className="add-step-btn">
                                    <button className="submitt-comment" onClick={addAnotherStep}>Add another Step</button>
                                </div>
                                <div className="submit-project-btn">
                                    <button className="submitt-comment" type='submit'>Submit your Project</button>
                                </div>
                            </div>
                            {/* {instructions.map(instruction => {
                                <div key={instruction.id}>
                                <h1>hello</h1>
                                </div>
                            })} */}
                        </div>
                    </form>
                )}
            </div>
            <div className="edit-project-form">
                {/* {showSupplyForm && ( */}

                <form>
                    {/* <div className="label-input-container">
                            <div className="label-input">
                                <label>Supply:</label>
                                <input
                                    type='text'
                                    name='supply'
                                    value={supply}
                                    required
                                    onChange={(e) => setSupply(e.target.value)}
                                ></input>
                            </div>
                            <div className="label-input">
                                <label>Amount:</label>
                                <input
                                    type='number'
                                    name='amount'
                                    value={amount}
                                    onChange={(e) => setAmount(e.target.value)}
                                ></input>
                            </div>
                            <button className="submit-comment" type='submit' onClick={addMoreSupplies}>Add more Supplies</button>
                            <button className="submit-comment" onClick={moveOnToInstructions}>Move on to Instructions</button>
                        </div> */}
                </form>
                {/* )} */}
            </div>
            <div className="edit-project-form">
                {showInstructionForm && (
                    <form onSubmit={handleProjectSubmit}>
                        {/* <div className="label-input-container"> */}
                        {/* <div className="label-input">
                                <label>Step {stepOrder} Title:</label>
                                <input
                                    type='text'
                                    name='stepTitle'
                                    value={stepTitle}
                                    onChange={(e) => setStepTitle(e.target.value)}
                                ></input>
                            </div> */}
                        {/* <div className="label-input">
                                <label>Step {stepOrder} Instructions:</label>
                                <textarea
                                    type='text'
                                    name='stepInstructions'
                                    value={stepInstructions}
                                    onChange={(e) => setStepInstructions(e.target.value)}
                                ></textarea>
                            </div> */}
                        {/* <div className="label-input"> */}
                        {/* <label>Step {stepOrder} Photo:</label>
                                <input
                                    type='text'
                                    name='photoUrl'
                                    value={photoUrl}
                                    onChange={(e) => setPhotoUrl(e.target.value)}
                                ></input> */}
                        {/* <UploadPicture setTitleImagee={setPhotoUrl} /> */}
                        {/* </div> */}
                        {/* <div className="label-input">
                                <label>Step {stepOrder} Video</label>
                                <input
                                    type='text'
                                    name='videoUrl'
                                    value={videoUrl}
                                    onChange={(e) => setVideoUrl(e.target.value)}
                                ></input>
                            </div> */}
                        {/* <button className="submit-comment" onClick={addAnotherStep}>Add another Step</button> */}
                        {/* </div> */}
                    </form>
                )}
            </div>
            {showErrors &&
                <>
                    <ul>
                        {errors.map(error => (
                            <li>{error}</li>
                        ))}
                    </ul>
                </>
            }
            {showSupplyErrors &&
                <>
                    <ul>
                        {supplyErrors.map(error => (
                            <li>{error}</li>
                        ))}
                    </ul>
                </>
            }
            {showInstructionErrors &&
                <>
                    <ul>
                        {instructionErrors.map(error => (
                            <li>{error}</li>
                        ))}
                    </ul>
                </>
            }
        </div>
    )
}

export default CreateProject;
