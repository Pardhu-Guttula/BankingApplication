import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import FloatingChatPanel from "../ui/FloatingChatPanel";
import FloatingChatFab from "../ui/FloatingChatFab";

export default function AssistanceWidget({
  defaultOpen = false,
  onToggle = () => {},
  onOpen = () => {},
  onClose = () => {},
  onFabClick = () => {},
  onStartChat = () => {},
  useImageIcon = true,
  assets,
}) {
  const intl = useIntl();
  const [open, setOpen] = useState(defaultOpen);

  const handlers = useMemo(() => {
    return {
      handleToggle: (next) => {
        setOpen(next);
        onToggle(next);
        if (next) onOpen();
        else onClose();
      },
      handleClose: () => {
        setOpen(false);
        onToggle(false);
        onClose();
      },
    };
  }, [onToggle, onOpen, onClose]);

  return (
    <>
      <FloatingChatPanel
        isOpen={open}
        onClose={handlers.handleClose}
        onPrimaryAction={onStartChat}
        title={intl.formatMessage({ id: "assistanceWidget.title" })}
        subtitle={intl.formatMessage({ id: "assistanceWidget.subtitle" })}
        primaryActionLabel={intl.formatMessage({ id: "assistanceWidget.primaryAction" })}
      />

      <FloatingChatFab
        isOpen={open}
        onToggle={handlers.handleToggle}
        onOpen={onOpen}
        onClose={onClose}
        onClick={onFabClick}
        useImageIcon={useImageIcon}
        iconImageSrc={assets?.imgChatbotIcon1}
        label={open ? intl.formatMessage({ id: "assistanceWidget.closeLabel" }) : intl.formatMessage({ id: "assistanceWidget.openLabel" })}
      />
    </>
  );
}