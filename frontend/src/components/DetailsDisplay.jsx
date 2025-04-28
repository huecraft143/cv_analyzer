import React from 'react';

function formatValue(value, parentKey = "") {
  if (typeof value === "string" || typeof value === "number") {
    return value || "—";
  }

  if (Array.isArray(value)) {
    if (value.length === 0) return "—";
    if (typeof value[0] === "object") {
      return value.map((item, index) => (
        <div key={index} className="mb-2 p-3 bg-gray-50 rounded shadow text-left">
          {Object.entries(item).map(([k, v]) => (
            <div key={k}>
              <strong className="capitalize">{k}:</strong> {formatValue(v)}
            </div>
          ))}
        </div>
      ));
    }
    return value.join(", ");
  }

  if (typeof value === "object" && value !== null) {
    // 👇 Eccezione per "languages": oggetto di oggetti -> trattalo come array visuale
    if (parentKey === "languages") {
      return Object.entries(value).map(([langKey, langData]) => (
        <div key={langKey} className="mb-2 p-3 bg-gray-50 rounded shadow text-left">
          <div className="font-semibold text-gray-800 capitalize mb-1">{langKey}</div>
          {Object.entries(langData).map(([k, v]) => (
            v ? (
              <div key={k}>
                <strong className="capitalize">{k}:</strong> {formatValue(v)}
              </div>
            ) : null
          ))}
        </div>
      ));
    }

    // 👇 fallback standard per oggetti normali
    return (
      <div className="text-left">
        {Object.entries(value).map(([k, v]) => (
          <div key={k}>
            <strong className="capitalize">{k}:</strong> {formatValue(v)}
          </div>
        ))}
      </div>
    );
  }

  return "—";
}


function DetailsDisplay({ details }) {
  const { name, email, phone, address, ...rest } = details;

  return (
    <div className="flex flex-col mt-6 p-6 bg-white rounded-lg shadow-md w-full max-w-2xl mx-auto">
      <h2 className="text-2xl text-primary mb-4 text-center">Dettagli Estratti</h2>

      {/* 🧍‍♂️ Blocco info personali */}
      <div className="mb-6 p-4 bg-gray-50 rounded shadow text-left">
        <div className="mb-2 text-black"><strong>Name:</strong> {name || "—"}</div>
        <div className="mb-2 text-black"><strong>Email:</strong> {email || "—"}</div>
        <div className="mb-2 text-black"><strong>Phone:</strong> {phone || "—"}</div>
        <div className="mb-2 text-black"><strong>Address:</strong> {address || "—"}</div>
      </div>

      {/* 🔁 Ciclo su tutto il resto */}
      <ul className="space-y-4 w-full">
        {Object.entries(rest).map(([key, value]) => (
          <li key={key} className="flex flex-col text-left">
            <span className="font-medium text-gray-700 mb-1 capitalize">{key}:</span>
            <span className="text-gray-900">{formatValue(value, key)}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}


export default DetailsDisplay;


