import React, { useState } from "react";
// import { useHistory } from "react-router-dom";
// import "../CreatePost/createPost.css"


const UploadPicture = ({ className, setTitleImagee }) => {
    // const history = useHistory(); // so that we can redirect after the image upload is successful
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("image", image);

        // aws uploads can be a bit slow—displaying
        // some sort of loading message is a good idea
        setImageLoading(true);

        const res = await fetch('/api/images', {
            method: "POST",
            body: formData,
        });
        if (res.ok) {
            const data = await res.json();
            setImageLoading(false);
            setTitleImagee(data.url);
        }
        else {
            setImageLoading(false);
            // a real app would probably use more advanced
            // error handling
        }
    }

    const updateImage = (e) => {
        const file = e.target.files[0];
        setImage(file);
    }

    return (
        <div className={!className ? "uploadPictureInput" : className}>
            <input
                type="file"
                accept="image/*"
                onChange={updateImage}
            />
            <button onClick={handleSubmit} type="submit">Upload Photo</button>
            {(imageLoading) && <p>Loading...</p>}
        </div>
    )
}

export default UploadPicture;