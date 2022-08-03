import React, { useEffect, useState } from 'react'

function UserPhoto({userId}) {
  const [userPhoto, setUserPhoto] = useState(null)
  useEffect(() => {
    async function fetchData(){
      const response = await fetch(`/api/users/${userId}`);
      if (response.ok) {
        const data = await response.json();
        if (data.errors) {
          return;
        };
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