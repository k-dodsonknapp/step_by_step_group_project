import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { addOneProject } from "../../store/project";
import { Redirect, useHistory  } from "react-router-dom";
import "./createProject.css"

const CreateProject = () => {
    const userId = useSelector(state => state.session.user['id'])
    const dispatch = useDispatch()
    const history = useHistory()

    const [title, setTitle] = useState('')
    const [titleImage, setTitleImage] = useState('')
    const [overview, setOverview] = useState('')
    const [category, setCategory] = useState('')

    const [supplies, setSupplies] = useState([])
    const [supply, setSupply] = useState('')
    const [amount, setAmount] = useState(0)

    const [instructions, setInstructions] = useState([])
    const [stepOrder, setStepOrder] = useState(1)
    const [stepTitle, setStepTitle] = useState('')
    const [stepInstructions, setStepInstructions] = useState('')
    const [photoUrl, setPhotoUrl] = useState('')
    const [videoUrl, setVideoUrl] = useState('')

    const [showProjectForm, setShowProjectForm] = useState(true)
    const [showSupplyForm, setShowSupplyForm] = useState(false)
    const [showInstructionForm, setShowInstructionForm] = useState(false)

    const handleProjectSubmit = async (e) => {
        e.preventDefault()
        addAnotherStep(e)
        const newInstruction = { stepOrder,
                                stepTitle,
                                'instructions': stepInstructions,
                                photoUrl,
                                videoUrl }
        const project = { userId, title, titleImage, overview, category, supplies,
                        'instructions': [...instructions, newInstruction] }
        const data = await dispatch(addOneProject(project))
        const projectId = data.projectId
        history.push(`/projects/${projectId}`)
    }

    const moveOntoSupplies = (e) => {
        e.preventDefault()
        setShowProjectForm(false)
        setShowSupplyForm(true)
    }

    const addMoreSupplies = (e) => {
        e.preventDefault()
        const newSupply = { supply, amount }
        setSupplies([...supplies, newSupply])
        setSupply('')
        setAmount(0)
    }

    const moveOnToInstructions = (e) => {
        addMoreSupplies(e)
        setShowSupplyForm(false)
        setShowInstructionForm(true)
    }

    const addAnotherStep = (e) => {
        e.preventDefault()
        const newInstruction = { stepOrder,
                                stepTitle,
                                'instructions': stepInstructions,
                                photoUrl,
                                videoUrl }
        setInstructions([...instructions, newInstruction])
        setStepOrder(stepOrder + 1)
        setStepTitle('')
        setStepInstructions('')
        setPhotoUrl('')
        setVideoUrl('')
    }

    return (
        <div className="create-page">
            <h1>Hello from Create project page</h1>
            {showProjectForm && (
            <form>
                <label>Title:</label>
                <input
                    type='text'
                    name='title'
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                ></input>
                <label>Image:</label>
                <input
                    type='text'
                    name='titleImage'
                    value={titleImage}
                    onChange={(e) => setTitleImage(e.target.value)}
                ></input>
                <label>Overview:</label>
                <textarea
                    type='text'
                    name='overview'
                    value={overview}
                    onChange={(e) => setOverview(e.target.value)}
                ></textarea>
                <label>Category:</label>
                <select name='category' onChange={(e) => setCategory(e.target.value)}>
                    <option value='Circuits'>Circuits</option>
                    <option value='Workshop'>Workshop</option>
                    <option value='Craft'>Craft</option>
                    <option value='Cooking'>Cooking</option>
                    <option value='Living'>Living</option>
                    <option value='Outside'>Outside</option>
                    <option value='Teachers'>Teachers</option>
                </select>
                <button onClick={moveOntoSupplies}>Move on to Supplies</button>
            </form>
            )}
            {showSupplyForm && (
            <form>
                <label>Supply:</label>
                <input
                    type='text'
                    name='supply'
                    value={supply}
                    onChange={(e) => setSupply(e.target.value)}
                ></input>
                <label>Amount:</label>
                <input
                    type='number'
                    name='amount'
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                ></input>
                <button onClick={addMoreSupplies}>Add more Supplies</button>
                <button onClick={moveOnToInstructions}>Move on to Instructions</button>
            </form>
            )}
            {showInstructionForm && (
            <form onSubmit={handleProjectSubmit}>
                <label>Step {stepOrder} Title:</label>
                <input
                    type='text'
                    name='stepTitle'
                    value={stepTitle}
                    onChange={(e) => setStepTitle(e.target.value)}
                ></input>
                <label>Step {stepOrder} Instructions:</label>
                <textarea
                    type='text'
                    name='stepInstructions'
                    value={stepInstructions}
                    onChange={(e) => setStepInstructions(e.target.value)}
                ></textarea>
                <label>Step {stepOrder} Photo:</label>
                <input
                    type='text'
                    name='photoUrl'
                    value={photoUrl}
                    onChange={(e) => setPhotoUrl(e.target.value)}
                ></input>
                <label>Step {stepOrder} Video</label>
                <input
                    type='text'
                    name='videoUrl'
                    value={videoUrl}
                    onChange={(e) => setVideoUrl(e.target.value)}
                ></input>
                <button onClick={addAnotherStep}>Add another Step</button>
                <button type='submit'>Submit your Project</button>
            </form>
            )}
        </div>
    )
}

export default CreateProject;
