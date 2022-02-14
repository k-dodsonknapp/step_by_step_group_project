import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { updateOnePost } from "../../store/project"
import "./editProject.css"

function EditProject() {
    const userId = useSelector(state => state.session.user["id"]);
    let { projectId } = useParams();
    projectId = parseInt(projectId)
    // console.log(typeof(projectId))
    const project = useSelector(state => state.projects[projectId])
    const dispatch = useDispatch();
    const history = useHistory();
    const owner = useSelector(state => state.user)
    // console.log(owner)

    // if (project) {
    //     console.log("PROJECT1", project)
    // }
    // const dispatch = useDispatch();
    // const history = useHistory();

    // if(project) {
    //     // console.log("session______",session.user.id)
    //     // console.log("project__________)",project.owner.id)

    // project overview
    const [title, setTitle] = useState(project.title);
    const [titleImage, setTitleImage] = useState(project.titleImage);
    const [category, setCategory] = useState(project.category);
    const [overview, setOverview] = useState(project.overview);

    //project supplies
    const [supplies, setSupplies] = useState(project.supplies);
    const [fixedSupplies, setFixedSupplies] = useState([...supplies])
    const [supply, setSupply] = useState(supplies[0].supply);
    const [amount, setAmount] = useState(supplies[0].amount);
    const [newSupplies, setNewSupplies] = useState([])


    // project instructions
    const [instructions, setInstructions] = useState(project.instructions);
    // console.log("instructions", instructions)
    const [fixedInstructions, setFixedInstructions] = useState([...instructions])
    const [fixedInstructionsId, setFixedInstructionsId] = useState(fixedInstructions[0].id)
    // console.log("fixed", fixedInstructions)
    const [newInstructions, setNewInstructions] = useState([])
    const [stepOrder, setStepOrder] = useState(instructions[0].stepOrder);
    const [stepTitle, setStepTitle] = useState(instructions[0].stepTitle);
    const [stepInstructions, setStepInstructions] = useState(instructions[0].instructions);
    // console.log(stepInstructions)
    const [photoUrl, setPhotoUrl] = useState(instructions[0].photoUrl);
    const [videoUrl, setVideoUrl] = useState(instructions[0].videoUrl);

    const [editProjectForm, setEditProjectForm] = useState(true);
    const [editSupplyForm, setEditSupplyForm] = useState(false);
    const [editInstructionsForm, setEditInstructionsForm] = useState(false);

    const handleEditProjectSubmit = async (e) => {
        // console.log("HELLO")
        e.preventDefault();
        const editedProject = {
            "id": projectId,
            "userId": userId,
            "title": title,
            "titleImage": titleImage,
            "overview": overview,
            "category": category,
            "instructions": [...newInstructions],
            "supplies":[...newSupplies]
        }
        // console.log("EDITED PROJECT", editedProject)
        const data = await dispatch(updateOnePost(editedProject))
        // const projectId = data.projectId
        history.push(`/projects/${projectId}`)

    }
    useEffect(() => {
        if (newSupplies.length === supplies.length) {
            setEditSupplyForm(false);
            setEditInstructionsForm(true);
        }
    }, [newSupplies, supplies]);

    // useEffect(() => {
    //     if (newInstructions.length === instructions.length){
    //         handleEditProjectSubmit();
    //     }
    // }, [newInstructions, instructions])


    const editSupplies = (e) => {
        e.preventDefault();
        setEditProjectForm(false);
        setEditSupplyForm(true);
    }

    const editInstructions = (e) => {
        e.preventDefault();
        setEditSupplyForm(false);
        setEditInstructionsForm(true);
    }

    const editMoreSupplies = (e) => {
        e.preventDefault();
        const newSupply = { supply, amount };
        setNewSupplies([...newSupplies, newSupply]);
        fixedSupplies.shift();
        setFixedSupplies([...fixedSupplies, { idk: "idk" }]);
        // console.log("fixed", fixedSupplies);
        setSupply(fixedSupplies[0].supply);
        setAmount(fixedSupplies[0].amount);
    }

    const editMoreInstructions = (e) => {
        e.preventDefault();
        const editedInstructions = {
            "stepOrder": stepOrder,
            "stepTitle": stepTitle,
            "instructions": stepInstructions,
            "photoUrl": photoUrl,
            "videoUrl": "videoUrl",
        }
        setNewInstructions([...newInstructions, editedInstructions])
        // console.log("newINSTRUCTIONS", newInstructions)
        fixedInstructions.shift();
        setFixedInstructions([...fixedInstructions, { idk: "idk" }]);
        // console.log("fixed", fixedInstructions)
        setStepTitle(fixedInstructions[0].stepTitle || "");
        setStepOrder(fixedInstructions[0].stepOrder || "")
        setStepInstructions(fixedInstructions[0].instructions || "");
        // console.log("reassigned stepInstructions",stepInstructions)
        setPhotoUrl(fixedInstructions[0].photoUrl || "");
        setVideoUrl(fixedInstructions[0].setVideoUrl || "");
    }

    // console.log("NEW INSTRUCTIONS",newInstructions)

    // const editNextStep = (e) => {
    //     e.preventDefault();
    //     const newInstruction = {
    //         stepOrder,
    //         stepTitle,
    //         'instructions': stepInstructions,
    //         photoUrl,
    //         videoUrl,
    //     }
    //     setInstructions([...instructions, newInstruction])
    //     instructions.shift()
    //     setStepTitle(instructions[0].stepTitle)

    //     setStepInstructions(instructions[0].stepInstructions)
    //     setPhotoUrl(instructions[0].photoUrl)
    //     setVideoUrl(instructions[0].videoUrl)
    // }


    return (
        <div className="editPage">
            <div className="edit-project-form">
                {editProjectForm && (
                    <form>
                        <div className="label-input-container">
                            <div className="label-input">
                                <label>Title:</label>
                                <input
                                    type="text"
                                    name="title"
                                    value={title}
                                    onChange={e => setTitle(e.target.value)}
                                ></input>
                            </div>
                            <div className="label-input">
                                <label>Image:</label>
                                <input
                                    type="text"
                                    name="titleImage"
                                    value={titleImage}
                                    onChange={e => setTitleImage(e.target.value)}
                                />
                            </div>
                            <div className="label-input">
                                <label>Overview</label>
                                <input
                                    type="text"
                                    name="overview"
                                    value={overview}
                                    onChange={e => setOverview(e.target.value)}
                                />
                            </div>
                            <div className="label-input">
                                <select name="category" onChange={e => setCategory(e.target.value)}>
                                    <option value='Circuits'>Circuits</option>
                                    <option value='Workshop'>Workshop</option>
                                    <option value='Craft'>Craft</option>
                                    <option value='Cooking'>Cooking</option>
                                    <option value='Living'>Living</option>
                                    <option value='Outside'>Outside</option>
                                    <option value='Teachers'>Teachers</option>
                                </select>
                            </div>
                            <div className="btn-div">
                                <button onClick={editSupplies}>Edit Supplies</button>
                            </div>
                        </div>
                    </form>
                )}
            </div>
            <div className="edit-project-form">
                {editSupplyForm && (
                    <form>
                        <div className="label-input-container">
                            <div className="label-input">
                                <label>Supply:</label>
                                <input
                                    type="text"
                                    name="supply"
                                    value={supply}
                                    onChange={e => setSupply(e.target.value)}
                                />
                            </div>
                            <div className="label-input">
                                <label>Amount:</label>
                                <input
                                    type="number"
                                    name="amount"
                                    value={amount}
                                    onChange={e => setAmount(e.target.value)}
                                />
                            </div>
                            <div className="btn-div">
                                <button onClick={editMoreSupplies}>Edit next supply</button>
                                <button onClick={editInstructions}>Edit Instructions</button>
                            </div>
                        </div>
                    </form>
                )}
            </div>
            <div className="edit-project-form">
                {editInstructionsForm && (
                    <form onSubmit={handleEditProjectSubmit}>
                        <div className="label-input-container">
                            <div className="label-input">
                                <label>Step {stepOrder} Title </label>
                                <input
                                    type="text"
                                    name="stepTitle"
                                    value={stepTitle}
                                    onChange={e => setStepTitle(e.target.value)}
                                />
                            </div>
                            <div className="label-input">
                                <label>Step {stepOrder} Instructions</label>
                                <textarea
                                    type="text"
                                    name="stepInstructions"
                                    value={stepInstructions}
                                    onChange={e => setStepInstructions(e.target.value)}
                                >
                                </textarea>
                            </div>
                            <div className="label-input">
                                <label>Step {stepOrder} Photo</label>
                                <input
                                    type="text"
                                    name="photoUrl"
                                    value={photoUrl}
                                    onChange={e => setPhotoUrl(e.target.value)}
                                />
                            </div>
                            <div className="label-input">
                                <label>Step {stepOrder} Video</label>
                                <input
                                    type="text"
                                    name="videoUrl"
                                    value={videoUrl}
                                    onChange={e => setVideoUrl(e.target.value)}
                                />
                            </div>
                            <button onClick={editMoreInstructions}>Edit next step instructions</button>
                            {newInstructions.length === instructions.length && (
                                <button onClick={handleEditProjectSubmit}>Submit Edit</button>
                            )}
                        </div>
                    </form>
                )}
            </div>
        </div>
    )
}

export default EditProject;