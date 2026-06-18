const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('is-open');
        navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
}

const platformBadges = document.querySelectorAll('.platform-badge');
const platformInput = document.querySelector('#id_platform');

if (platformBadges.length && platformInput) {
    const syncSelectedBadges = () => {
        const selectedPlatforms = platformInput.value
            .split(',')
            .map((platform) => platform.trim())
            .filter(Boolean);

        platformBadges.forEach((badge) => {
            if (selectedPlatforms.includes(badge.dataset.platform)) {
                badge.classList.add('is-selected');
            } else {
                badge.classList.remove('is-selected');
            }
        });
    };

    platformBadges.forEach((badge) => {
        badge.addEventListener('click', () => {
            const selectedPlatforms = platformInput.value
                .split(',')
                .map((platform) => platform.trim())
                .filter(Boolean);

            const platform = badge.dataset.platform;
            const platformIndex = selectedPlatforms.indexOf(platform);

            if (platformIndex >= 0) {
                selectedPlatforms.splice(platformIndex, 1);
            } else {
                selectedPlatforms.push(platform);
            }

            platformInput.value = selectedPlatforms.join(', ');
            syncSelectedBadges();
        });
    });

    platformInput.addEventListener('input', syncSelectedBadges);
    syncSelectedBadges();
}