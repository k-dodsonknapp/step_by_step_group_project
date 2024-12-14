import React from "react";
// import { useDispatch, useSelector } from 'react-redux'
// import { getView } from '../../store/views';
// import FavoriteCount from '../FavoriteCount';

function ViewCount({ project }) {

  return (
    <div>
      <div id="favorite-views">
        <div>👁 {project?.views}</div>
      </div>
    </div>
  );
}

export default ViewCount;
