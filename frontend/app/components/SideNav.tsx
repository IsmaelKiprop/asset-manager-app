/** @format */
'use client'
import React, {useState} from "react";
import Link from "next/link";
import Image from "next/image";
import logo from "../../public/logo.svg";
import {
  FaHome,
  FaBell,
  FaComments,
  FaFolder,
  FaCog,
  FaSearch,
  FaPowerOff,
  FaHeadphones,
} from "react-icons/fa";
import { MdAddchart, MdInbox, MdInsights } from "react-icons/md";

const SideNav = () => {
   const [isAccordionOpen, setIsAccordionOpen] = useState(false);

  const toggleAccordion = () => {
    setIsAccordionOpen(!isAccordionOpen);
  };

  return (
    <nav className="bg-[#14ae5c] text-white h-screen m-1 rounded-xl overflow-auto fixed top-0 left-0 w-64 flex flex-col justify-between">
      <div className="px-4 ">
        <div className="py-6">
          <Image src={logo} alt="Logo" width={250} height={200} priority />
        </div>
        <div className="py-2 font-medium text-sm">Central</div>
        <ul className="">
          <li className="hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
            <FaHome />
            <a href="#" className="ml-4">
              Dashboard
            </a>
          </li>
          <li className="hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
            <FaBell />
            <a href="#" className="ml-4">
              Notifications
              <span className="bg-red-500 text-white px-1 rounded-full ml-4">
                10
              </span>
            </a>
          </li>
          <li className="hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
            <FaComments />
            <a href="#" className="ml-4">
              Chat
            </a>
          </li>
          <div className="py-2 font-medium text-sm">Workplace</div>
          <li className="hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
            <FaSearch />
            <a href="#" className="ml-4">
              Assets
            </a>
          </li>
          <li
        className={`relative hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full ${
          isAccordionOpen ? "bg-[#eeeeee]/10" : ""
        }`}
        onClick={toggleAccordion}
      >
        <MdAddchart />
        <p className="ml-4">Finances</p>
        <div
          data-collapse="collapse-1"
          className={`h-0 overflow-hidden transition-all duration-300 ease-in-out ${
            isAccordionOpen ? "h-auto" : ""
          }`}
        >
          <div className="py-2 ">
            <a href="#" className="ml-4">
              Invoices
            </a>
          </div>
          <div className="py-2 pl-4">
            <a href="#" className="ml-4">
              Payments
            </a>
          </div>
        </div>
      </li>
          <li className="hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
            <MdInsights />
            <a href="#" className="ml-4">
              Analytics
            </a>
          </li>
          <div className="py-2 font-medium text-sm">General</div>
          <li className="hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
            <FaFolder />
            <a href="#" className="ml-4">
              Files
            </a>
          </li>
          <li className="hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
            <FaCog />
            <a href="#" className="ml-4">
              Settings
            </a>
          </li>
        </ul>
        {/* <li>
  <Link href="/" className="border hover:bg-red-600 p-2">
    <div className="grid grid-cols-2">
      <div>
        <FaHome />
      </div>
      <div>Dashboard</div>
    </div>
  </Link>
</li>; */}
      </div>
      <div className="flex items-center mb-4">
        <button className="bg-slate-900/10 hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center">
          <FaHeadphones />
          <a href="/support" className="ml-4">
            Contact Support
          </a>
        </button>
        <FaPowerOff className="ml-4" />
      </div>
    </nav>
  );
};

export default SideNav;
