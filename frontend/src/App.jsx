import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { BankingLoginPage } from "./components/BankingLoginPage";
import { LoginPage } from "./components/LoginPage";

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/banking-login" element={<BankingLoginPage />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
}
