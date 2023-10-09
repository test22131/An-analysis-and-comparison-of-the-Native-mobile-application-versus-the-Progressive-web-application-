import React, { useState, useEffect } from 'react';
import styles from './Gallery.module.css'

const Gallery = () => {
  const [images, setImages] = useState([]);

  useEffect(() => {
    const imagesFromLocalStorage = JSON.parse(localStorage.getItem('images') || '[]');
    setImages(imagesFromLocalStorage);
  }, []);

  const handleDelete = (index) => {
    const updatedImages = [...images];
    updatedImages.splice(index, 1);
    setImages(updatedImages);
    localStorage.setItem('images', JSON.stringify(updatedImages));
  };

  return (
    <div className={styles.Gallery}>
      {images.map((image, index) => (
        <div key={index}>
          <img src={image} alt={`Image ${index}`} />
          <button className={styles.button} onClick={() => handleDelete(index)}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default Gallery;
