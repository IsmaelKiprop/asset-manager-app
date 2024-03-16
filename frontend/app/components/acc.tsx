/** @format */

import React, { useState } from "react";
import { MdAddchart } from "react-icons/md";

const SideNav = () => {
  const [isAccordionOpen, setIsAccordionOpen] = useState(false);

  const toggleAccordion = () => {
    setIsAccordionOpen(!isAccordionOpen);
  };

  return (
    <nav className="bg-[#14ae5c] text-white h-screen m-1 rounded-xl overflow-auto fixed top-0 left-0 w-64 flex flex-col justify-between">
      {/* ...existing code... */}
      <li
        className={`relative hover:bg-[#eeeeee]/10 hover:text-[#fec300] py-2 px-4 rounded-full flex items-center ${
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
          <div className="py-2 pl-4">
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
      {/* ...existing code... */}
    </nav>
  );
};
