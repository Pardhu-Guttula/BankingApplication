import React, { useId, useMemo, useState } from 'react';
import { useIntl } from 'react-intl';
import { LabeledInput } from '../ui/LabeledInput';
import { RememberRow } from '../ui/RememberRow';
import { PrimaryButton } from '../ui/PrimaryButton';
import { validateEmailOrUsername, validatePassword } from '../../utils/validators';
import { noop } from '../../utils/noop';

export function LoginForm({
  emailOrUsername,
  password,
  rememberMe,
  onEmailOrUsernameChange = noop,
  onPasswordChange = noop,
  onRememberMeChange = noop,
  onForgotPassword = noop,
  onSubmit = noop,
  loading = false,
}) {
  const intl = useIntl();
  const emailId = useId();
  const passwordId = useId();

  const [touched, setTouched] = useState({ email: false, password: false });
  const [submitAttempted, setSubmitAttempted] = useState(false);

  const errors = useMemo(() => {
    return {
      email: validateEmailOrUsername(emailOrUsername),
      password: validatePassword(password),
    };
  }, [emailOrUsername, password]);

  const showEmailError = (touched.email || submitAttempted) && errors.email;
  const showPasswordError =
    (touched.password || submitAttempted) && errors.password;

  const canSubmit = !errors.email && !errors.password && !loading;

  return (
    <form
      className="flex flex-col gap-4"
      onSubmit={(e) => {
        e.preventDefault();
        setSubmitAttempted(true);

        const emailErr = validateEmailOrUsername(emailOrUsername);
        const passErr = validatePassword(password);

        if (emailErr || passErr) return;

        onSubmit({
          emailOrUsername: String(emailOrUsername || "").trim(),
          password: String(password || ""),
          rememberMe: Boolean(rememberMe),
        });
      }}
    >
      <LabeledInput
        id={emailId}
        label={intl.formatMessage({ id: 'loginForm.usernameOrEmail' })}
        type="text"
        value={emailOrUsername}
        placeholder="john.doe@email.com"
        autoComplete="username"
        onChange={onEmailOrUsernameChange}
        error={showEmailError}
      />

      <LabeledInput
        id={passwordId}
        label={intl.formatMessage({ id: 'loginForm.password' })}
        type="password"
        value={password}
        placeholder="••••••••"
        autoComplete="current-password"
        onChange={onPasswordChange}
        error={showPasswordError}
      />

      <RememberRow
        checked={rememberMe}
        onCheckedChange={onRememberMeChange}
        onForgotPassword={onForgotPassword}
      />

      <PrimaryButton
        label={loading ? intl.formatMessage({ id: 'common.continuing' }) : intl.formatMessage({ id: 'loginForm.submitButton' })}
        disabled={!canSubmit}
      />
    </form>
  );
}
