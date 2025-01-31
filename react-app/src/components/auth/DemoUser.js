import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import "./auth.css";

const DemoButton = ({ className }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const handleDemo = async (e) => {
    e.preventDefault();
    const email = "demo@aa.io";
    const password = "password";
    await dispatch(login(email, password));
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <button
      className={!className ? "demo-user" : className}
      onClick={handleDemo}
    >
      Demo User
    </button>
  );
};

export default DemoButton;
