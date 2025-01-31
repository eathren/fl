import * as React from 'react'
import { Outlet, createRootRoute } from '@tanstack/react-router'

export const Route = createRootRoute({
  component: RootComponent,
})

function RootComponent() {
  return (
      <React.Fragment>
          
      <div className="text-3xl text-red-500 font-bold underline">Hello "__root"!</div>
      <Outlet />
    </React.Fragment>
  )
}
