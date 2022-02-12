import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

function EditProject () {
    const {projectId} = useParams();
    console.log("-----------",projectId)
    const userId = useSelector(state => state.session.user['id'])
    const dispatch = useDispatch()
    const history = useHistory()
    const project = useSelector(state => state.projects[projectId])
    console.log("---------", project)

    const [title, setTitle] = useState('')
    const [titleImage, setTitleImage] = useState('')
    const [overview, setOverview] = useState('')
    const [category, setCategory] = useState('')

    return (
        <>
        {projectId}
        </>
    )
}

export default EditProject;