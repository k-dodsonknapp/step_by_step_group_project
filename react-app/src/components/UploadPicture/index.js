import React, { useState } from "react";
// import { useHistory } from "react-router-dom";
// import "../CreatePost/createPost.css"
import "./uploadPicture.css";

const UploadPicture = ({ uploadType, setPhoto }) => {
  // const history = useHistory(); // so that we can redirect after the image upload is successful
  const [image, setImage] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [fileName, setFileName] = useState("");

  // const handleSubmit = async (e) => {
  //     e.preventDefault();
  //     const formData = new FormData();
  //     formData.append("image", image);

  //     // aws uploads can be a bit slow—displaying
  //     // some sort of loading message is a good idea
  //     setImageLoading(true);
  //     console.log(image)

  //     const res = await fetch(`${process.env.REACT_APP_API_URL}/api/images`, {
  //         method: "POST",
  //         body: formData,
  //     });
  //     if (res.ok) {
  //         const data = await res.json();
  //         setImageLoading(false);
  //         setTitleImagee(data.url);
  //     }
  //     // else {
  //     setImageLoading(false);
  //         // a real app would probably use more advanced
  //         // error handling
  //     // }
  // }

  // const [fileName, setFileName] = useState("No file chosen")

  const updateImage = (e) => {
    const file = e.target.files[0];
    if (file) {
      setPhoto(e.target.files[0])
      setFileName(file.name);
      const imageUrl = URL.createObjectURL(file);
      setImage(imageUrl);
    }
  };

  return (
    <div className={!uploadType ? "uploadPictureInput" : uploadType}>
      {!image && (
        <>
          <label htmlFor="file-upload" className="customFileUpload">
            Custom Upload
          </label>
          <input
            type="file"
            id="file-upload"
            accept="image/*"
            onChange={updateImage}
            hidden
          />
          {/* <label htmlFor="fileInput" className="file-label">
            Choose an image
          </label>  */}
        </>
      )}
      {image && (
        <div className="image-preview-container">
          <img
            className="image-preview"
            src={image}
            alt="Preview profile"
            style={{ margeTop: "10px" }}
          />
          <input
            type="file"
            id="reupload-file"
            accept="image/*"
            onChange={updateImage}
            hidden
          />
          {uploadType === "addProfilePhoto" && (
            <label htmlFor="reupload-file" class="custom-file-reupload">
              Try a different angle?
            </label>
          )}
        </div>
        // </div>
      )}
      {/* <button onClick={handleSubmit} type="submit">Upload Photo</button> */}
      {imageLoading && <p>Loading...</p>}
    </div>
  );
};

export default UploadPicture;
