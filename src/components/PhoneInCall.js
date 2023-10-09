import React, { useState, useEffect } from 'react';
import styles from './PhoneInCall.module.css';
import PhoneCallbackIcon from '@mui/icons-material/PhoneCallback';

function PhoneInCall() {
  const [isInCall, setIsInCall] = useState(false);

  useEffect(() => {
    async function checkInCallStatus() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const tracks = stream.getTracks();
        const isAudioInUse = tracks.some(
          (track) => track.kind === 'audio' && track.readyState === 'live'
        );
        const isVideoInUse = tracks.some(
          (track) => track.kind === 'video' && track.readyState === 'live'
        );
        setIsInCall(isAudioInUse && !isVideoInUse);
        tracks.forEach((track) => track.stop());
      } catch (error) {
        setIsInCall(false);
      }
    }

    checkInCallStatus();
  }, []);

  return (
    <div className={styles.container}>
      <PhoneCallbackIcon className={styles.phoneIcon} />
      <h2 className={styles.callStatus}>
        {isInCall ? 'The device is in call' : 'The device is not in call'}
      </h2>
      {!isInCall && <p className={styles.centerText}>The Device is not in call</p>}
    </div>
  );
}

export default PhoneInCall;
