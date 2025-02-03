import React from "react";
// import { useDispatch, useSelector } from 'react-redux';
// import { getAllFavorites } from '../../store/favortie';

function FavoriteCount({ project }) {
  // const dispatch = useDispatch();
  // const favorites = useSelector(state => state?.favorites?.favorite)?.filter(favorite => favorite?.projectId === project?.id)

  // useEffect(() => {
  //     dispatch(getAllFavorites())
  // }, [dispatch])

  return <div id="favorite-count">❤ {project.favorites}</div>;
}

export default FavoriteCount;
