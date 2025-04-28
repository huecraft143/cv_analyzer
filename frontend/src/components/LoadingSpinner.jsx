import React from 'react';

function LoadingSpinner() {
    return (
        <div className="flex justify-center w-full py-8 items-center space-x-2">
        <div className="w-4 h-4 bg-primary rounded-full animate-bounce" style={{animationDelay: '0ms'}}></div>
        <div className="w-4 h-4 bg-primary rounded-full animate-bounce" style={{animationDelay: '150ms'}}></div>
        <div className="w-4 h-4 bg-primary rounded-full animate-bounce" style={{animationDelay: '300ms'}}></div>
</div>
      );
}

export default LoadingSpinner;

