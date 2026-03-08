import React, { useState } from 'react';
import { useIntl } from 'react-intl';
import { BrandHeader } from './sections/BrandHeader';
import { AuthCard } from './sections/AuthCard';
import { LoginForm } from './sections/LoginForm';
import { SecurityNote } from './sections/SecurityNote';
import { noop } from '../utils/noop';

export function BankingLoginPage({
  loading = false,
  onSubmit = noop,
  onForgotPassword = noop,
}) {
  const intl = useIntl();
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
        <BrandHeader
          title={intl.formatMessage({ id: 'brandHeader.title' })}
          subtitle={intl.formatMessage({ id: 'brandHeader.subtitle' })}
        />

        <AuthCard
          title={intl.formatMessage({ id: 'authCard.signIn' })}
          description={intl.formatMessage({ id: 'authCard.enterCredentials' })}
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

        <SecurityNote text={intl.formatMessage({ id: 'securityNote.text' })} />
      </section>
    </main>
  );
}
