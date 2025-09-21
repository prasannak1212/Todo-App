import React, { useMemo } from "react";
import Particles, { initParticlesEngine } from "@tsparticles/react";
import { loadSlim } from "@tsparticles/slim";

export default function BackgroundParticles() {
  const options = useMemo(
    () => ({
      background: {
        color: { value: "transparent" }, // let your page gradient show
      },
      fullScreen: {
        enable: true,
        zIndex: -1,
      },
      particles: {
        number: {
          value: 120,
          density: { enable: true, area: 800 },
        },
        color: { value: ["#ffffff", "#a0c4ff"] },
        shape: { type: "circle" },
        opacity: { value: 0.8, random: true },
        size: { value: { min: 1, max: 3 }, random: true },
        move: {
          enable: true,
          speed: 0.5,
          direction: "bottom",
          outModes: { default: "out" },
        },
      },
    }),
    []
  );

  return <Particles id="tsparticles" options={options} init={initParticlesEngine(loadSlim)} />;
}
