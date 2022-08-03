import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { getAllFavorites } from '../../store/favortie';

function FavoriteCount({ project }) {

    const dispatch = useDispatch();
    const favorites = useSelector(state => state?.favorites?.favorite)?.filter(favorite => favorite?.projectId === project?.id)
    // const [favoriteCount, setFavoriteCount] = useState(0);
    // const [favoriteArr, setFavoriteArr] = useState([]);
    // console.log("ASDFASDFASDF",favoriteArr)
    
    useEffect(() => {
        dispatch(getAllFavorites())
        // const favoriteList = favorites?.filter(favorite => favorite?.projectId === project?.id)
        // if (favoriteList !== undefined){
        //     setFavoriteCount(favoriteList)
        // } else {
        //     setFavoriteArr(0)
        // }
        // if (favorites?.length){
        //     setFavoriteCount(favoriteList?.length)
        //     console.log("yuio",favoriteCount)
        // }else {
        //     setFavoriteCount(0)
        //     console.log("yuio",favoriteCount)
        // }
    }, [dispatch])

    return (
        <div id='favorite-count'>
            ❤ {favorites?.length}
        </div>
    )
}

export default FavoriteCount