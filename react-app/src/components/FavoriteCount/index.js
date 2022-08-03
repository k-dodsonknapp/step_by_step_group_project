import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { getAllFavorites } from '../../store/favortie';

function FavoriteCount({ project }) {

    const dispatch = useDispatch();
    const favorites = useSelector(state => state?.favorites?.favorite).filter(favorite => favorite?.projectId === project?.id)
    const [favoriteCount, setFavoriteCount] = useState(0)

    useEffect(() => {
        dispatch(getAllFavorites())
        if (favorites?.length){
            setFavoriteCount(favorites?.length)
        }
    }, [dispatch])

    return (
        <div id='favorite-count'>
            ❤ {favoriteCount}
        </div>
    )
}

export default FavoriteCount