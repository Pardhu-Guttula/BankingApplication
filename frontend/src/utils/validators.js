export function validateEmailOrUsername(value) {
  const v = String(value || "").trim();
  if (!v) return "Username or email is required.";
  if (v.includes("@")) {
    const ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
    if (!ok) return "Enter a valid email address.";
  }
  return "";
}

export function validatePassword(value) {
  const v = String(value || "");
  if (!v) return "Password is required.";
  if (v.length < 8) return "Password must be at least 8 characters.";
  return "";
}