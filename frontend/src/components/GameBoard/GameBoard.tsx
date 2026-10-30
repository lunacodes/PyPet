import React from 'react';
import classes from "./gameboard.module.scss";

const GameBoard: React.FC = () => {
  return (
    <main className={classes.gameBoard}>
      <div className={classes.moodIcons}>
        <span className={classes.single}>Mood Icon(s)</span>
      </div>
      <div className={classes.petIcon}><p>Pet Icon</p></div>
      <div className={classes.actionRow}>
        <button className={classes.actionItem}>Action</button>
        <button className={classes.actionItem}>Action</button>
        <button className={classes.actionItem}>Action</button>
        <button className={classes.actionItem}>Action</button>
      </div>
    </main>
  );
};

export default GameBoard;
