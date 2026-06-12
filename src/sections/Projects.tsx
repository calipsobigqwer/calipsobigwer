import styles from './Projects.module.css'

const projects = [
  {
    title: 'E-commerce Platform',
    description: 'A full-featured online store built with React and Node.js.',
    tags: ['React', 'Node.js', 'MongoDB'],
    link: '#'
  },
  {
    title: 'Task Management App',
    description: 'A productivity tool to manage daily tasks and team collaboration.',
    tags: ['TypeScript', 'React', 'Firebase'],
    link: '#'
  },
  {
    title: 'Weather Dashboard',
    description: 'Real-time weather data visualization using OpenWeather API.',
    tags: ['JavaScript', 'CSS Modules', 'API'],
    link: '#'
  }
]

const Projects = () => {
  return (
    <section id="projects" className={styles.projects}>
      <div className="container">
        <h2 className="section-title">My Projects</h2>
        <div className={styles.grid}>
          {projects.map((project, index) => (
            <div key={index} className={styles.card}>
              <div className={styles.cardImage}>Project Screenshot</div>
              <div className={styles.cardContent}>
                <h3>{project.title}</h3>
                <p>{project.description}</p>
                <div className={styles.tags}>
                  {project.tags.map(tag => <span key={tag}>{tag}</span>)}
                </div>
                <a href={project.link} className={styles.link}>View Project &rarr;</a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Projects
