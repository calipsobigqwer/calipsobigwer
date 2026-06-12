import styles from './About.module.css'

const About = () => {
  return (
    <section id="about" className={styles.about}>
      <div className="container">
        <h2 className="section-title">About Me</h2>
        <div className={styles.grid}>
          <div className={styles.imagePlaceholder}>
            {/* You can replace this with an actual image later */}
            <div className={styles.img}>Portrait</div>
          </div>
          <div className={styles.content}>
            <p>
              Hello! I'm a passionate web developer based in your city. I enjoy 
              building things that live on the internet, whether that be websites, 
              applications, or anything in between.
            </p>
            <p>
              My goal is to always build products that provide pixel-perfect, 
              performant experiences. I'm currently focused on expanding my 
              knowledge in full-stack development and cloud technologies.
            </p>
            <p>
              When I'm not coding, you can find me exploring new technologies, 
              contributing to open-source projects, or enjoying a good book.
            </p>
          </div>
        </div>
      </div>
    </section>
  )
}

export default About
