import React, { useState, useRef, useEffect } from 'react';
import { Link } from 'react-router-dom';
import styles from './Camera.module.css';

const Camera = () => {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [images, setImages] = useState([]);

  useEffect(() => {
    const startVideo = async () => {
      try {
        const constraints = { video: true };
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (err) {
        console.error('Error accessing camera: ', err);
      }
    };

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      startVideo();
    } else {
      console.error('getUserMedia not supported in this browser');
    }

    return () => {
      if (videoRef.current && videoRef.current.srcObject) {
        videoRef.current.srcObject.getTracks().forEach(track => track.stop());
      }
    };
  }, []);

  const captureImage = () => {
    if (videoRef.current) {
      const canvas = canvasRef.current;
      canvas.width = videoRef.current.videoWidth;
      canvas.height = videoRef.current.videoHeight;
      canvas.getContext('2d').drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
      const imageSrc = canvas.toDataURL('image/jpeg');
      setImages([...images, imageSrc]);
      localStorage.setItem('images', JSON.stringify([...images, imageSrc]));
    }
  };

  return (
    <div className={styles.Camera}>
      <video ref={videoRef} autoPlay playsInline />
      <button className={styles.button} onClick={captureImage}>Capture Image</button>
      <Link to="/gallery">
        <button className={styles.button}>View Gallery</button>
      </Link>
      <canvas ref={canvasRef} style={{ display: 'none' }} />
    </div>
  );
};

export default Camera;
