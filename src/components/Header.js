import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Box } from '@mui/material';

const Header = () => {
  const location = useLocation();

  return (
    <header>
      <Box display="flex" justifyContent="flex-start" alignItems="center" height="100%" paddingLeft="1rem">
        {location.pathname !== '/' && (
          <Link to="/" style={{ textDecoration: 'none', color: 'blue' }}>
            <span style={{ fontSize: '1.5rem', position: 'relative', top: '2rem' }}>&lt; Back</span>
          </Link>
        )}
      </Box>
    </header>
  );
};

export default Header;
