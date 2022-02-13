import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { updateOnePost } from "../../store/project"

function EditProject() {
    const userId = useSelector(state => state.session.user["id"]);
    const { projectId } = useParams();
    const project = useSelector(state => state.projects[projectId])

    // if (project) {
    //     console.log(project)
    // }
    // const dispatch = useDispatch();
    // const history = useHistory();

    // if(project) {
    //     // console.log("session______",session.user.id)
    //     // console.log("project__________)",project.owner.id)

    // project overview
    const [title, setTitle] = useState(project.title);
    const [titleImg, setTitleImg] = useState(project.titleImage);
    const [category, setCategory] = useState(project.category);
    const [overview, setOverview] = useState(project.overview);

    // }
    //project supplies
    const [supplies, setSupplies] = useState(project.supplies);
    const [fixedSupplies, setFixedSupplies] = useState([...supplies])
    // const [suppliesLength, setSuppliesLength] = useState(supplies.length);
    // console.log("SUPPLY LENGTH FROM DATABASE", suppliesLength)
    console.log("SUPPLIES", supplies)
    const [supply, setSupply] = useState(supplies[0].supply); // not sure how to use this state
    const [amount, setAmount] = useState(supplies[0].amount);
    const [newSupplies, setNewSupplies] = useState([])
    console.log("NEW SUPPLIES", newSupplies)

    // project instructions
    const [instructions, setInstructions] = useState(project.instructions);
    const [stepOrder, setStepOrder] = useState(instructions[0].stepOrder);
    const [stepTitle, setStepTitle] = useState(instructions[0].stepTitle);
    const [stepInstructions, setStepInstructions] = useState(instructions[0].instructions);
    const [photoUrl, setPhotoUrl] = useState(instructions[0].photoUrl);
    const [videoUrl, setVideoUrl] = useState(instructions[0].videoUrl);

    const [editProjectForm, setEditProjectForm] = useState(true);
    const [editSupplyForm, setEditSupplyForm] = useState(false);
    const [editInstructionsForm, setEditInstructionsForm] = useState(false);

    useEffect(() => {
        if (newSupplies.length === supplies.length) {
            setEditSupplyForm(false);
            setEditInstructionsForm(true);
            // setSupply
        }
    }, [newSupplies, supplies])

    // useEffect(() => {

    // }, [])

    const handleEditProjectSubmit = (e) => {
        // console.log("HELLO")
        e.preventDefault();

    }

    const editSupplies = (e) => {
        e.preventDefault()
        setEditProjectForm(false)
        setEditSupplyForm(true)
    }

    const editInstructions = (e) => {
        e.preventDefault()
        setEditSupplyForm(false)
        setEditInstructionsForm(true)
    }

    const editMoreSupplies = (e) => {
        e.preventDefault();
        const newSupply = { supply, amount }
        let num = 1

        setNewSupplies([...newSupplies, newSupply])
        fixedSupplies.shift()
        setFixedSupplies([...fixedSupplies, {idk: "idk"}])
        console.log("fixed", fixedSupplies)
        setSupply(fixedSupplies[0].supply)
        setAmount(fixedSupplies[0].amount)

    }

    const editNextStep = (e) => {
        e.preventDefault();
        const newInstruction = {
            stepOrder,
            stepTitle,
            'instructions': stepInstructions,
            photoUrl,
            videoUrl,
        }
        setInstructions([...instructions, newInstruction])
        instructions.shift()
        setStepTitle(instructions[0].stepTitle)
        setStepInstructions(instructions[0].stepInstructions)
        setPhotoUrl(instructions[0].photoUrl)
        setVideoUrl(instructions[0].videoUrl)
    }


    return (
        <div>
            {editProjectForm && (
                <form>
                    <label>Title:</label>
                    <input
                        type="text"
                        name="title"
                        value={title}
                        onChange={e => setTitle(e.target.value)}
                    ></input>
                    <label>Image:</label>
                    <input
                        type="text"
                        name="titleImg"
                        value={titleImg}
                        onChange={e => setTitleImg(e.target.value)}
                    />
                    <label>Overview</label>
                    <input
                        type="text"
                        name="overview"
                        value={overview}
                        onChange={e => setOverview(e.target.value)}
                    />
                    <select name="category" onChange={e => setCategory(e.target.value)}>
                        <option value='Circuits'>Circuits</option>
                        <option value='Workshop'>Workshop</option>
                        <option value='Craft'>Craft</option>
                        <option value='Cooking'>Cooking</option>
                        <option value='Living'>Living</option>
                        <option value='Outside'>Outside</option>
                        <option value='Teachers'>Teachers</option>
                    </select>
                    <button onClick={editSupplies}>Edit Supplies</button>
                </form>
            )}
            {editSupplyForm && (
                <form>
                    <label>Supply:</label>
                    <input
                        type="text"
                        name="supply"
                        value={supply}
                        onChange={e => setSupply(e.target.value)}
                    />
                    <label>Amount:</label>
                    <input
                        type="number"
                        name="amount"
                        value={amount}
                        onChange={e => setAmount(e.target.value)}
                    />
                    <button onClick={editMoreSupplies}>Edit next supply</button>
                    <button onClick={editInstructions}>Edit Instructions</button>
                </form>
            )}
            {editInstructionsForm && (
                <form onSubmit={handleEditProjectSubmit}>
                    <label>Step {stepOrder} Title </label>
                    <input
                        type="text"
                        name="stepTitle"
                        value={stepTitle}
                        onChange={e => setStepTitle(e.target.value)}
                    />
                    <label>Step {stepOrder} Instructions</label>
                    <textarea
                        type="text"
                        name="stepIPnstructions"
                        value={stepInstructions}
                        onChange={e => setStepInstructions(e.target.value)}
                    >
                    </textarea>
                    <label>Step {stepOrder} Photo</label>
                    <input
                        type="text"
                        name="photoUrl"
                        value={photoUrl}
                        onChange={e => setPhotoUrl(e.target.value)}
                    />
                    <label>Step {stepOrder} Video</label>
                    <input
                        type="text"
                        name="videoUrl"
                        value={videoUrl}
                        onChange={e => setVideoUrl(e.target.value)}
                    />
                    <button onClick={editNextStep}>Edit next step instructions</button>
                </form>
            )}
        </div>
    )
}

export default EditProject;