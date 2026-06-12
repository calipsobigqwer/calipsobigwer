const Skills = () => {
  return (
    <section id="skills" className="section">
      <div className="container">
        <h2>Skills</h2>
        <ul style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', marginTop: '1rem' }}>
          <li style={{ background: '#f1f5f9', padding: '0.5rem 1rem', borderRadius: '4px' }}>React</li>
          <li style={{ background: '#f1f5f9', padding: '0.5rem 1rem', borderRadius: '4px' }}>TypeScript</li>
          <li style={{ background: '#f1f5f9', padding: '0.5rem 1rem', borderRadius: '4px' }}>CSS Modules</li>
          <li style={{ background: '#f1f5f9', padding: '0.5rem 1rem', borderRadius: '4px' }}>Vite</li>
        </ul>
      </div>
    </section>
  )
}

export default Skills
