import React from "react";
import { Check, Clock, FileSearch2 } from "lucide-react";

export default function RequestIcon({ variant }) {
  const config =
    {
      completed: {
        wrap: "bg-[#DCFCE7]",
        icon: <Check className="h-4 w-4 text-[#16A34A]" strokeWidth={2.5} />,
      },
      pending: {
        wrap: "bg-[#FEF9C2]",
        icon: <Clock className="h-4 w-4 text-[#CA8A04]" strokeWidth={2.5} />,
      },
      review: {
        wrap: "bg-[#DBEAFE]",
        icon: <FileSearch2 className="h-4 w-4 text-[#2563EB]" strokeWidth={2.5} />,
      },
    }[variant] || {
      wrap: "bg-[#DBEAFE]",
      icon: <FileSearch2 className="h-4 w-4 text-[#2563EB]" strokeWidth={2.5} />,
    };

  return (
    <div className={["h-8 w-8 rounded-full grid place-items-center", config.wrap].join(" ")}>
      {config.icon}
    </div>
  );
}