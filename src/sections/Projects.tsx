const Projects = () => {
  return (
    <section id="projects" className="section">
      <div className="container">
        <h2>My Projects</h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem', marginTop: '2rem' }}>
          <div style={{ border: '1px solid #e2e8f0', padding: '1.5rem', borderRadius: '8px' }}>
            <h3>Project 1</h3>
            <p>Description of project 1.</p>
          </div>
          <div style={{ border: '1px solid #e2e8f0', padding: '1.5rem', borderRadius: '8px' }}>
            <h3>Project 2</h3>
            <p>Description of project 2.</p>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Projects
