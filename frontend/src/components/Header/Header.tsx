import React from 'react';
import classes from "./header.module.scss";

const Title: React.FC = () => {
  return (
    <header className={classes.siteHeader}><h1>PyPet</h1></header>
  );
};

export default Title;
