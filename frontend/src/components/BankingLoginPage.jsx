import React, { useState } from 'react';
import { useIntl } from 'react-intl';
import { BrandHeader } from './sections/BrandHeader';
import { AuthCard } from './sections/AuthCard';
import { LoginForm } from './sections/LoginForm';
import { SecurityNote } from './sections/SecurityNote';
import { noop } from '../utils/noop';

export function BankingLoginPage({
  title = "SecureBank Portal",
  subtitle = "Your banking, simplified",
  securityText = "Secured with 256-bit encryption",
  loading = false,
  onSubmit = noop,
  onForgotPassword = noop,
}) {
  const [emailOrUsername, setEmailOrUsername] = useState("john.doe@email.com");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);

  return (
    <main
      className="min-h-screen w-full flex flex-col items-center justify-center px-4"
      style={{
        backgroundImage:
          "linear-gradient(145.03869956590015deg, rgb(239, 246, 255) 0%, rgb(255, 255, 255) 50%, rgb(239, 246, 255) 100%)",
      }}
    >
      <section className="w-full max-w-[448px] flex flex-col gap-[24px] items-stretch">
        <BrandHeader title={title} subtitle={subtitle} />

        <AuthCard
          title="Sign In"
          description="Enter your credentials to access your account"
        >
          <LoginForm
            emailOrUsername={emailOrUsername}
            password={password}
            rememberMe={rememberMe}
            onEmailOrUsernameChange={setEmailOrUsername}
            onPasswordChange={setPassword}
            onRememberMeChange={setRememberMe}
            onForgotPassword={onForgotPassword}
            onSubmit={onSubmit}
            loading={loading}
          />
        </AuthCard>

        <SecurityNote text={securityText} />
      </section>
    </main>
  );
}