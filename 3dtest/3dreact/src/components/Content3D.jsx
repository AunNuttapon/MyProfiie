import React from 'react'
import { Canvas } from '@react-three/fiber'
import { useGLTF, OrbitControls } from '@react-three/drei'


const Content3D = () => {
    const phone = useGLTF('./iphone/scene.gltf')

  return (
    <div className='content'>
      <Canvas>
        <OrbitControls enableRotate autoRotate/>
        <ambientLight intensity={3}/>
        <directionalLight intensity={3} position={[-5,0,0]} />
        <directionalLight intensity={3} position={[5,0,0]} />
        <directionalLight intensity={3} position={[0,5,0]} />
        <directionalLight intensity={3} position={[0,-5,0]} />
        <directionalLight intensity={3} position={[0,0,5]} />
        <directionalLight intensity={3} position={[0,0,-5]} />
        <mesh>
          <primitive
          scale={0.005} 
          object={phone.scene}
          position={[0,-1,0]}
          />
        </mesh>

      </Canvas>
    </div>
  )
}

export default Content3D