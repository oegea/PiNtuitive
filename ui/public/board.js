
    const React = window.React;
    const { useState, useEffect } = React;
    const { closeApp, startProcess } = window.electronAPI;

    window.export = () => {
        const [currentTime, setCurrentTime] = useState(new Date());
        const [clickedApp, setClickedApp] = useState(null);
      
        useEffect(() => {
          const timer = setInterval(() => {
            setCurrentTime(new Date());
          }, 30000); // Update every minute
      
          return () => clearInterval(timer);
        }, []);
      
        const apps = [
          /*{ name: 'Text', icon: '💬', color: 'from-green-400 to-green-600' },
          { name: 'Calendar', icon: '9', color: 'from-gray-300 to-gray-500' },
          { name: 'Photos', icon: '🌻', color: 'from-purple-400 to-purple-600' },
          { name: 'Camera', icon: '📷', color: 'from-gray-600 to-gray-800' },
          { name: 'YouTube', icon: '▶️', color: 'from-red-500 to-red-700' },
          { name: 'Stocks', icon: '📈', color: 'from-blue-400 to-blue-600' },
          { name: 'Maps', icon: '🗺️', color: 'from-green-500 to-green-700' },
          { name: 'Weather', icon: '☀️', color: 'from-blue-300 to-blue-500' },
          { name: 'Clock', icon: '🕰️', color: 'from-gray-300 to-gray-500' },
          { name: 'Calculator', icon: '🧮', color: 'from-gray-600 to-gray-800' },
          { name: 'Notes', icon: '📝', color: 'from-yellow-300 to-yellow-500' },
          { name: 'Settings', icon: '⚙️', color: 'from-gray-400 to-gray-600' },*/
        ];
      
        /*const bottomApps = [
          { name: 'Phone', icon: <Phone size={28} />, color: 'from-green-400 to-green-600' },
          { name: 'Mail', icon: <Mail size={28} />, color: 'from-blue-400 to-blue-600' },
          { name: 'Safari', icon: <Compass size={28} />, color: 'from-blue-300 to-blue-500' },
          { name: 'iPod', icon: <Music size={28} />, color: 'from-pink-400 to-pink-600' },
        ];*/
      
        const bottomApps = [
            { name: 'Desktop', icon: '🖥️', color: 'from-gray-400 to-gray-600', onClick: () => closeApp() },
            { name: 'Terminal', icon: '>_', color: 'from-gray-400 to-gray-600', onClick: () => startProcess('lxterminal') },
        ];
      
        const handleClick = (appName) => {
            const app = apps.find(app => app.name === appName) || bottomApps.find(app => app.name === appName);
            if (app && app.onClick) {
                app.onClick();
            }
            setClickedApp(appName);
            setTimeout(() => setClickedApp(null), 300);
        };
      
        const AppIcon = ({ app, isBottom = false }) => (
          <div 
            className="flex flex-col items-center"
            onClick={() => handleClick(app.name)}
          >
            <div 
              className={`
                ${isBottom ? 'w-12 h-12 rounded-xl' : 'w-14 h-14 rounded-2xl'} 
                bg-gradient-to-br ${app.color} 
                flex items-center justify-center text-2xl shadow-lg
                cursor-pointer
                transition-all duration-200 ease-in-out
                hover:brightness-110
                active:brightness-90 active:scale-95
                ${clickedApp === app.name ? 'brightness-75 scale-90' : ''}
              `}
            >
              {typeof app.icon === 'string' ? app.icon : React.cloneElement(app.icon, { className: 'text-white' })}
            </div>
            <span className="mt-1 text-xs">{app.name}</span>
          </div>
        );
      
        return (
          <div className="flex flex-col h-screen bg-black text-white font-sans">
            <div className="flex justify-center items-center p-2 text-sm">
              <span>{currentTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
            </div>
            
            <div className="flex-grow grid grid-cols-4 gap-4 p-4">
              {apps.map((app, index) => (
                <AppIcon key={index} app={app} />
              ))}
            </div>
            
            <div className="h-20 bg-gray-800 bg-opacity-50 flex justify-around items-center px-2">
              {bottomApps.map((app, index) => (
                <AppIcon key={index} app={app} isBottom={true} />
              ))}
            </div>
          </div>
        );
      
    };