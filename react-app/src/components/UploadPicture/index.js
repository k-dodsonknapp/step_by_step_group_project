import React, { useState } from "react";
import { useHistory } from "react-router-dom";
// import "../CreatePost/createPost.css"


const UploadPicture = ({ setTitleImagee }) => {
    const history = useHistory(); // so that we can redirect after the image upload is successful
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);
    console.log(">>>>>>>>", image)


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
            console.log("PPPPPPPPPPPP", data);
            setImageLoading(false);
            setTitleImagee(data.url);
            // history.push("/images");
        }
        else {
            setImageLoading(false);
            // a real app would probably use more advanced
            // error handling
            console.log("error");
        }
    }

    const updateImage = (e) => {
        const file = e.target.files[0];
        setImage(file);
    }

    return (
        // <form onSubmit={handleSubmit}>
        <div className="uploadPictureInput">
            <input
                type="file"
                accept="image/*"
                onChange={updateImage}
            />
            <button onClick={handleSubmit} type="submit">Submit</button>
            {(imageLoading) && <p>Loading...</p>}
        </div>
        // </form>
    )
}

export default UploadPicture;