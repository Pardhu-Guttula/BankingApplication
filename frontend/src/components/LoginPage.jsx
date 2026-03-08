import React, { useState } from 'react';
import { useIntl } from 'react-intl';
import { LoginForm } from './sections/LoginForm';
import { RememberRow } from './ui/RememberRow';
import { noop } from '../utils/noop';

export function LoginPage({
  loading = false,
  onSubmit = noop,
  onForgotPassword = noop,
}) {
  const intl = useIntl();
  const [emailOrUsername, setEmailOrUsername] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  return (
    <main className="min-h-screen w-full flex flex-col items-center justify-center px-4">
      <section className="w-full max-w-[448px] flex flex-col gap-6 items-stretch">
        <h1 className="text-2xl font-bold text-center">
          {intl.formatMessage({ id: 'authCard.signIn' })}
        </h1>
        <p className="text-center text-gray-500">
          {intl.formatMessage({ id: 'authCard.enterCredentials' })}
        </p>

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
      </section>
    </main>
  );
}
