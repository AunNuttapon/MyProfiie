import React from 'react'

function InfoOne() {
  return (
    <div className='container mx-auto flex items-center py-16'>
        <div className="w-1/2">
            <img src="https://images.unsplash.com/photo-1629904853716-f0bc54eea481?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="" className='w-full h-auto rounded-lg ' />
        </div>
        <div className="w-1/2 px-6">
            <h2 className='text-3xl font-semibold'>Welcome to Our Website</h2>
            <p className='text-gray-600 mt-4'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum harum, est sit modi ut deleniti quod facilis explicabo libero eveniet voluptatem dignissimos laborum nostrum praesentium.</p>
        </div>
    </div>
  )
}

export default InfoOne