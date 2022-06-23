import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getView } from '../../store/views';

function ViewCount({ project }) {

    const dispatch = useDispatch();

    const views = useSelector(state => state?.views?.views)

    const [projectViews, setProjectViews] = useState()

    useEffect(() => {
        dispatch(getView())
        setProjectViews(views?.filter(view => view?.projectId === project?.id)[0])
    }, [dispatch])

    return (
        <div>
            <p>
                ❤ 5  👁 {projectViews?.viewCount}
            </p>
        </div>
    )
}

export default ViewCount;