# HybriSim: A Hybrid Simulation System for Distributed Learning in Mobile Environments

**Paper Link**: [HybriSim: Bridging Real and Simulated Devices for Distributed Learning](https://dl.acm.org/doi/10.1145/3625687.3628379)  

## Motivation
Traditional simulation tools often face challenges in scalability and accuracy:  
- **Simulated Environments**: Do not adequately reflect the operation of real devices.  
- **Real Devices**: Difficult to scale for larger use cases.  

**HybriSim** bridges this gap by introducing a hybrid simulation system that combines real and simulated environments. It focuses on evaluating distributed learning algorithms in mobile environments, particularly urban mobility scenarios with vehicles and pedestrians.


## Key Contributions
1. **Hybrid Simulation**:  
   HybriSim enables distributed learning in hybrid systems, allowing integration with real devices to measure:  
   - Energy consumption  
   - Temperature  
   - Communication methods  

   These capabilities provide a more accurate representation of real-world conditions while maintaining scalability.

2. **Dynamic Mobility Handling**:  
   Supports testing a range of mobility scenarios, simplifying encounter simulations and addressing changing mobility situations.

3. **Extensibility**:  
   Demonstrated on Raspberry Pi and Jetson Nano as real-world elements, with a laptop serving as the simulation server and controller.



## Methodology
HybriSim integrates simulation configuration and execution through:  
1. **Setup**:  
   - **Simulation Tools**: Uses SUMO for defining mobility scenarios.  
   - **Device Configuration**: Includes specifications like GPU and communication methods.  

2. **Execution**:  
   - A simulation controller manages real devices.  
   - Launches monitoring components.  
   - Oversees hybrid simulation processes.  

3. **Testing Framework**:  
   Extensive testing was performed to validate robustness and scalability in distributed learning scenarios.



## Positive Aspects
- **Balanced Design**:  
  Supports both real and simulated devices, adapting to varying conditions.  
- **Practical Utility**:  
  Real-time evaluation metrics make it valuable for academic and industrial applications.  
- **Scalability**:  
  Demonstrates robustness in simulating large-scale distributed learning scenarios.  



## Limitations
1. **Dependency on External Frameworks**:  
   - Relies heavily on SUMO, limiting its application to urban mobility.  

2. **Scalability Challenges**:  
   - Managing a large number of real devices remains a concern.  

3. **Static Configuration**:  
   - Device specifications are static and do not adapt to changing real-world conditions.  

4. **Small-Scale Testbed**:  
   - Focus on Raspberry Pi raises concerns about feasibility for large-scale setups.



## Future Directions
1. **Non-Urban Scenarios**:  
   Expand to maritime and rural mobility environments.  

2. **Improved Device Management**:  
   Develop methods for better integration and scaling of real devices.  

3. **Dynamic Configuration**:  
   Introduce mechanisms to update device configurations in real-time based on environmental changes.  

4. **Integration with Diverse Tools**:  
   Support additional simulation tools for broader mobility and communication scenarios.
