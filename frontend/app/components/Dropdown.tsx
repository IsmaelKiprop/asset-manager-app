// generate a component for the following, it should take a list of links as a prop which is an array
'use client'
import React, { useState } from "react"

export default function Dropdown({links, icon, title}: {links: any[], icon: any, title: string}) {
    const [isDropdownOpen, setDropdownOpen] = useState(false);

    const toggleDropdown = () => {
        setDropdownOpen(!isDropdownOpen);
    };

    return (
        <nav>
            <div className="flex items-center mb-4">
                <button
                    className="bg-slate-900/10 hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center"
                    onClick={toggleDropdown}
                >
                    {icon}
                    <a href="#" className="ml-4">
                        title={title}
                    </a>
                </button>
            </div>
            {isDropdownOpen && (
                <div className="dropdown-content">
                    <div className="border-l border-white h-full"></div>
                    <ul className="ml-auto">
                        {links.map((link: any, index: number) => (
                            <li key={index}>
                                <a href={link.url}>{link.label}</a>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </nav>
    );
}
// import { FaHome } from 'react-icons/fa';

// const links = [
//     { url: '/link1', label: 'Link 1' },
//     { url: '/link2', label: 'Link 2' },
//     { url: '/link3', label: 'Link 3' },
// ];

// <Dropdown links={links} icon={<FaHome />} title="Home" />;

{/* <li>
            
                <div className="dropdown-content">
                  <div className="border-l border-white h-full"></div>
                  <ul className="ml-auto">
                    {links.map((link, index) => (
                      <li key={index}>
                        <a href={link.url}>{link.label}</a>
                      </li>
                    )<div className="flex items-center mb-4">
              <button
                className="bg-slate-900/10 hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center"
                onClick={toggleDropdown}
              >
                <FaHeadphones />
                <a href="#" className="ml-4">
                  Contact Support
                </a>
              </button>
              <FaPowerOff className="ml-4" />
            </div>
            {isDropdownOpen && (
              <div className="dropdown-content">
                <div className="border-l border-white h-full"></div>
                <ul className="ml-auto">
                  <li>
                    <a href="#">Link 1</a>
                  </li>
                  <li>
                    <a href="#">Link 2</a>
                  </li>
                  <li>
                    <a href="#">Link 3</a>
                  </li>
                </ul>
              </div>
            )}
          </li> */}