const fill = document.querySelector('#progress-fill');
const chapters = [...document.querySelectorAll('.chapter')];
const chapterLinks = [...document.querySelectorAll('.masthead nav a')];

const update = () => {
  const max = document.documentElement.scrollHeight - innerHeight;
  fill.style.width = `${max > 0 ? (scrollY / max) * 100 : 0}%`;
  let active = chapters[0].id;
  for (const chapter of chapters) {
    if (chapter.getBoundingClientRect().top <= innerHeight * .35) active = chapter.id;
  }
  for (const link of chapterLinks) {
    const current = link.hash === `#${active}`;
    link.classList.toggle('active', current);
    if (current) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
};
addEventListener('scroll', update, {passive: true});
addEventListener('resize', update);
update();
