import React, { useEffect, useState } from 'react'

function UserPhoto({userId}) {
  console.log(userId)
  const [userPhoto, setUserPhoto] = useState(null)
  console.log(userPhoto)
  useEffect(() => {
    async function fetchData(){
      const response = await fetch(`/api/users/${userId}`);
      if (response.ok) {
        const data = await response.json();
        console.log(data)
        if (data.errors) {
          return;
        };
        // dispatch(getProjects(data));
        // return data;
        setUserPhoto(data.userPhoto)
      }
    };
    fetchData()
  }, [userId])
  return (
    <>
    <img id='comment-user-photo' src={userPhoto} alt={""}></img>
    </>
  )
}

export default UserPhoto