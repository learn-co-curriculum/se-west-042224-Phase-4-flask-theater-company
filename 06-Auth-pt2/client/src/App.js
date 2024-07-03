import { Route, Routes } from "react-router-dom";
import { createGlobalStyle } from "styled-components";
import { useEffect, useState } from "react";
import Home from "./components/Home";
import ProductionForm from "./components/ProductionForm";
import Navigation from "./components/Navigation";
import ProductionDetail from "./components/ProductionDetail";
import NotFound from "./components/NotFound";
import Authentication from "./components/Authentication";

function App() {
  const [productions, setProductions] = useState([]);
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser();
    fetchProductions();
  }, []);

  const fetchProductions = () =>
    fetch("/productions")
      .then((res) => res.json())
      .then(setProductions);

  const fetchUser = () =>
    fetch("/authorized").then((res) => {
      if (res.ok) {
        res.json().then((data) => {
          setUser(data);
        });
      } else {
        setUser(null);
      }
    });

  const addProduction = (production) =>
    setProductions((current) => [...current, production]);

  const updateUser = (user) => setUser(user);
  if (!user)
    return (
      <>
        <GlobalStyle />
        <Navigation updateUser={updateUser}/>
        <Authentication updateUser={updateUser} />
      </>
    );

  return (
    <>
      <GlobalStyle />
      <Navigation updateUser={updateUser} />
      <Routes>
        <Route
          path="/productions/new"
          element={<ProductionForm addProduction={addProduction} />}
        />
        <Route
          path="/productions/:id"
          element={<ProductionDetail />}
        />
        <Route
          path="/authentication"
          element={<Authentication updateUser={updateUser} />}
        />
        <Route
          path="/"
          element={<Home productions={productions} />}
        />
        <Route
          path="*"
          element={<NotFound />}
        />
        {/* This acts as a fallback route */}
      </Routes>
    </>
  );
}

export default App;

const GlobalStyle = createGlobalStyle`
    body{
      background-color: black; 
      color:white;
    }
    `;
