import type React from 'react';
import { useState } from 'react';

import type { ApiParameterDocs, ApiSource } from '../../types/api';

type ParamValue = string | number | boolean | string[];
type ParamRecord = Record<string, ParamValue>;

interface ApiConfigPanelProps {
  source: ApiSource;
  currentParams: ParamRecord;
  onUpdateParams: (params: ParamRecord) => void;
  onSaveDefaults: (params: ParamRecord) => void;
}

const ConfigInput: React.FC<{
  param: ApiParameterDocs;
  value: ParamValue;
  onChange: (value: ParamValue) => void;
}> = ({ param, value, onChange }) => {
  if (param.type === 'array' && param.options) {
    return (
      <select
        multiple
        value={(value as string[]) || []}
        onChange={(e) => {
          const values = Array.from(e.target.selectedOptions).map(
            (opt) => opt.value
          );
          onChange(values);
        }}
        className="w-full p-2 border rounded"
      >
        {param.options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    );
  }

  if (param.type === 'boolean') {
    return (
      <input
        id={`param-${param.name}`}
        type="checkbox"
        checked={Boolean(value)}
        onChange={(e) => onChange(e.target.checked)}
        className="rounded border-gray-300"
      />
    );
  }

  if (param.options) {
    return (
      <select
        id={`param-${param.name}`}
        value={String(value) || ''}
        onChange={(e) => onChange(e.target.value)}
        className="w-full p-2 border rounded"
      >
        <option value="">Select...</option>
        {param.options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    );
  }

  return (
    <input
      id={`param-${param.name}`}
      type={param.type === 'number' ? 'number' : 'text'}
      value={value === undefined ? '' : String(value)}
      onChange={(e) => {
        const newValue =
          param.type === 'number' ? Number(e.target.value) : e.target.value;
        onChange(newValue);
      }}
      className="w-full p-2 border rounded"
      placeholder={`Enter ${param.name}...`}
    />
  );
};

export const ApiConfigPanel: React.FC<ApiConfigPanelProps> = ({
  source,
  currentParams,
  onUpdateParams,
  onSaveDefaults,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [params, setParams] = useState<ParamRecord>(currentParams);

  const handleParamChange = (param: ApiParameterDocs, value: ParamValue) => {
    const newParams = { ...params, [param.name]: value };
    setParams(newParams);
    onUpdateParams(newParams);
  };

  const handleSaveDefaults = () => {
    onSaveDefaults(params);
  };

  if (!isOpen) {
    return (
      <button
        type="button"
        onClick={() => setIsOpen(true)}
        className="fixed bottom-4 right-4 bg-blue-500 text-white p-2 rounded-full shadow-lg hover:bg-blue-600"
        title="Configure API Parameters"
      >
        <svg
          className="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          aria-labelledby="configIconTitle"
        >
          <title id="configIconTitle">Configure API Parameters</title>
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
          />
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
          />
        </svg>
      </button>
    );
  }

  return (
    <div className="fixed bottom-4 right-4 bg-white p-4 rounded-lg shadow-xl border w-96">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-semibold">{source.name} Configuration</h3>
        <button
          type="button"
          onClick={() => setIsOpen(false)}
          className="text-gray-500 hover:text-gray-700"
        >
          ×
        </button>
      </div>

      <div className="space-y-4 max-h-96 overflow-y-auto">
        {source.parameterDocs.map((param) => (
          <div key={param.name} className="space-y-1">
            <label
              htmlFor={`param-${param.name}`}
              className="block text-sm font-medium"
            >
              {param.name}
              {param.required && <span className="text-red-500">*</span>}
            </label>
            <div className="text-xs text-gray-500 mb-1">
              {param.description}
            </div>
            <ConfigInput
              param={param}
              value={params[param.name] || ''}
              onChange={(value) => handleParamChange(param, value)}
            />
          </div>
        ))}
      </div>

      <div className="mt-4 flex justify-end space-x-2">
        <button
          type="button"
          onClick={handleSaveDefaults}
          className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
        >
          Save as Defaults
        </button>
      </div>
    </div>
  );
};
